/**
 * GET /api/review/[slug]
 * Returns the full review detail for a paper: staged pages, log entry,
 * discussion JSON, and Sweden check result.
 */
import { NextRequest, NextResponse } from "next/server";
import { Storage } from "@google-cloud/storage";
import { Firestore } from "@google-cloud/firestore";
import { validate_page } from "../../_lib/page_validator";

const gcs            = new Storage();
const db             = new Firestore({ projectId: process.env.GCP_PROJECT });
const STAGING_BUCKET = process.env.STAGING_BUCKET!;

export async function GET(
  _req: NextRequest,
  { params }: { params: { slug: string } }
) {
  const { slug } = params;

  // Load paper metadata from Firestore
  const doc = await db.collection("papers").doc(slug).get();
  if (!doc.exists) {
    return NextResponse.json({ error: "Paper not found" }, { status: 404 });
  }
  const paper = { id: doc.id, ...doc.data() };

  // Load all staged wiki pages
  const [files] = await gcs.bucket(STAGING_BUCKET).getFiles({ prefix: `${slug}/wiki/` });

  const pages = await Promise.all(
    files.map(async (file) => {
      const [content] = await file.download();
      const text = content.toString();
      const pageSlug = file.name
        .replace(`${slug}/wiki/`, "")
        .replace(".md", "");
      const { errors, warnings } = validate_page(pageSlug, text);
      const isNew = !((paper as any).conceptsUpdated ?? []).includes(pageSlug);
      return { slug: pageSlug, isNew, content: text, validationErrors: errors, validationWarnings: warnings };
    })
  );

  // Load log entry
  let logEntry = "";
  try {
    const [logContent] = await gcs.bucket(STAGING_BUCKET).file(`${slug}/log_entry.md`).download();
    logEntry = logContent.toString();
  } catch {}

  // Load Sweden check result
  let swedenCheck = { ok: true, violations: [] };
  try {
    const [sc] = await gcs.bucket(STAGING_BUCKET).file(`${slug}/sweden_check.json`).download();
    swedenCheck = JSON.parse(sc.toString());
  } catch {}

  // Load discussion JSON
  let discussion = {};
  try {
    const [disc] = await gcs.bucket(STAGING_BUCKET).file(`${slug}/discussion.json`).download();
    discussion = JSON.parse(disc.toString());
  } catch {}

  return NextResponse.json({ paper, pages, logEntry, swedenCheck, discussion });
}
