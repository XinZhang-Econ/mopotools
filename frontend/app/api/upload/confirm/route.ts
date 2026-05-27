/**
 * POST /api/upload/confirm
 * Called after the browser finishes uploading to Cloud Storage.
 * Updates Firestore status to "uploaded" so the pipeline can pick it up.
 */
import { NextRequest, NextResponse } from "next/server";
import { Firestore } from "@google-cloud/firestore";

const db = new Firestore({ projectId: process.env.GCP_PROJECT });

export async function POST(req: NextRequest) {
  const { slug } = await req.json();
  if (!slug) {
    return NextResponse.json({ error: "Missing slug" }, { status: 400 });
  }

  await db.collection("papers").doc(slug).update({
    status:     "uploaded",
    uploadedAt: new Date().toISOString(),
  });

  return NextResponse.json({ status: "ok", slug });
}
