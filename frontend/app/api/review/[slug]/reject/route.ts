/**
 * POST /api/review/[slug]/reject
 * Marks the paper as rejected and cleans up staging files.
 */
import { NextRequest, NextResponse } from "next/server";
import { Storage } from "@google-cloud/storage";
import { Firestore } from "@google-cloud/firestore";

const gcs            = new Storage();
const db             = new Firestore({ projectId: process.env.GCP_PROJECT });
const STAGING_BUCKET = process.env.STAGING_BUCKET!;

export async function POST(
  req: NextRequest,
  { params }: { params: { slug: string } }
) {
  const { slug } = params;
  const { note } = await req.json().catch(() => ({ note: "" }));

  // Delete all staging files for this slug
  const [files] = await gcs.bucket(STAGING_BUCKET).getFiles({ prefix: `${slug}/` });
  await Promise.all(files.map((f) => f.delete().catch(() => {})));

  // Update Firestore status
  await db.collection("papers").doc(slug).update({
    status:     "rejected",
    rejectedAt: new Date().toISOString(),
    reviewNote: note ?? "",
  });

  return NextResponse.json({ message: `Paper "${slug}" rejected.` });
}
