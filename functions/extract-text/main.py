"""
Stage 3 — Text Extraction Cloud Function
Triggered by Cloud Workflows after a new file lands in the raw/ bucket.
Calls Document AI to extract clean Markdown text and saves it to processed/.
"""

import os
import re
import json
import logging
from pathlib import Path

import functions_framework
from google.cloud import documentai, storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GCP_PROJECT       = os.environ["GCP_PROJECT"]
PROCESSED_BUCKET  = os.environ["PROCESSED_BUCKET"]
PROCESSOR_ID      = os.environ["DOCUMENT_AI_PROCESSOR_ID"]   # injected from Secret Manager
LOCATION          = "eu"                                        # Document AI EU endpoint


@functions_framework.http
def extract_text(request):
    """
    Expected JSON body:
    {
        "slug":     "bernanke-2020-new-tools",
        "raw_path": "gs://mopotools-raw/bernanke-2020-new-tools.pdf"
    }
    """
    body = request.get_json(force=True)
    slug     = body["slug"]
    raw_path = body["raw_path"]

    logger.info(f"Extracting text for {slug} from {raw_path}")

    # Download raw file
    gcs = storage.Client()
    bucket_name, blob_name = _parse_gcs_path(raw_path)
    bucket = gcs.bucket(bucket_name)
    blob   = bucket.blob(blob_name)
    file_bytes = blob.download_as_bytes()
    mime_type  = _infer_mime(blob_name)

    # Extract text via Document AI
    extracted = _call_document_ai(file_bytes, mime_type)

    # Build section-aware Markdown
    markdown = _to_sectioned_markdown(extracted, slug)

    # Save to processed/
    dest_blob = gcs.bucket(PROCESSED_BUCKET).blob(f"{slug}.md")
    dest_blob.upload_from_string(markdown, content_type="text/markdown")
    logger.info(f"Saved extracted text to gs://{PROCESSED_BUCKET}/{slug}.md")

    return {"status": "ok", "slug": slug, "chars": len(markdown)}, 200


def _parse_gcs_path(gcs_path: str) -> tuple[str, str]:
    """Parse gs://bucket/blob into (bucket, blob)."""
    path = gcs_path.removeprefix("gs://")
    bucket, _, blob = path.partition("/")
    return bucket, blob


def _infer_mime(filename: str) -> str:
    ext = Path(filename).suffix.lower()
    return {
        ".pdf":  "application/pdf",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".doc":  "application/msword",
        ".md":   "text/markdown",
        ".txt":  "text/plain",
    }.get(ext, "application/octet-stream")


def _call_document_ai(file_bytes: bytes, mime_type: str) -> documentai.Document:
    """Send file to Document AI and return the parsed Document."""
    client = documentai.DocumentProcessorServiceClient(
        client_options={"api_endpoint": f"{LOCATION}-documentai.googleapis.com"}
    )
    processor_name = (
        f"projects/{GCP_PROJECT}/locations/{LOCATION}/processors/{PROCESSOR_ID}"
    )
    response = client.process_document(
        request=documentai.ProcessRequest(
            name=processor_name,
            raw_document=documentai.RawDocument(content=file_bytes, mime_type=mime_type),
        )
    )
    return response.document


def _to_sectioned_markdown(doc: documentai.Document, slug: str) -> str:
    """
    Convert a Document AI Document to section-aware Markdown.

    For large documents, labels sections as:
      <!-- section: abstract -->
      <!-- section: body -->
      <!-- section: references -->

    This lets the Stage 4 prompt target specific sections for different tasks.
    """
    full_text = doc.text

    # If Document AI detected page layout, try to extract labelled sections
    sections = _extract_sections(full_text)

    lines = [
        f"<!-- source: {slug} -->",
        f"<!-- pages: {len(doc.pages)} -->",
        "",
    ]

    if sections:
        for section_name, content in sections.items():
            lines.append(f"<!-- section: {section_name} -->")
            lines.append(content.strip())
            lines.append("")
    else:
        # No section detection — emit full text as-is
        lines.append(full_text)

    return "\n".join(lines)


# Heuristic section splitter — looks for common academic paper headings
_SECTION_PATTERNS = [
    ("abstract",     r"(?i)\bAbstract\b"),
    ("introduction", r"(?i)\b(?:1\.?\s+)?Introduction\b"),
    ("conclusion",   r"(?i)\b(?:\d+\.?\s+)?Conclusion(?:s)?\b"),
    ("references",   r"(?i)\bReferences\b|\bBibliography\b"),
]


def _extract_sections(text: str) -> dict[str, str]:
    """
    Attempt to split text into labelled sections.
    Returns empty dict if no recognisable structure is found.
    """
    positions = {}
    for name, pattern in _SECTION_PATTERNS:
        match = re.search(pattern, text)
        if match:
            positions[name] = match.start()

    if len(positions) < 2:
        return {}

    # Sort by position and slice
    sorted_sections = sorted(positions.items(), key=lambda x: x[1])
    result = {}
    for i, (name, start) in enumerate(sorted_sections):
        end = sorted_sections[i + 1][1] if i + 1 < len(sorted_sections) else len(text)
        result[name] = text[start:end]

    # Everything before the first detected section → "preamble" (title, authors, etc.)
    first_pos = sorted_sections[0][1]
    if first_pos > 100:
        result = {"preamble": text[:first_pos], **result}

    return result
