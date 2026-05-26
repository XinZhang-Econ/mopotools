/**
 * POST /api/upload/init
 * Creates a Firestore document for the paper and returns a signed upload URL
 * pointing directly at Cloud Storage raw/ bucket.
 */

import { NextRequest, NextResponse } from "next/server";
import { Storage } from "@google-cloud/storage";
import { Firestore } from "@google-cloud/firestore";

const gcs       = new Storage();
const db        = new Firestore({ projectId: process.env.GCP_PROJECT });
const RAW_BUCKET = process.env.RAW_BUCKET!;

function toSlug(filename: string, title: string, year: number): string {
  const base = title
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .slice(0, 60);
  return `${base}-${year}`;
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  const { filename, title, authors, year, tag } = body;

  if (!filename || !title || !authors || !year || !tag) {
    return NextResponse.json({ error: "Missing required fields" }, { status: 400 });
  }

  const ext  = filename.split(".").pop()?.toLowerCase() ?? "pdf";
  const slug = toSlug(filename, title, year);
  const gcsPath = `${slug}.${ext}`;

  // Create Firestore document
  await db.collection("papers").doc(slug).set({
    slug,
    title,
    authors,
    year,
    tag,
    rawPath:    `gs://${RAW_BUCKET}/${gcsPath}`,
    status:     "pending",
    uploadedAt: new Date().toISOString(),
  });

  // Generate signed URL valid for 15 minutes
  const [signedUrl] = await gcs.bucket(RAW_BUCKET).file(gcsPath).getSignedUrl({
    version:    "v4",
    action:     "write",
    expires:    Date.now() + 15 * 60 * 1000,
    contentType: ext === "pdf" ? "application/pdf"
                 : "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  });

  return NextResponse.json({ signedUrl, slug });
}
