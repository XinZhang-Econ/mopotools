/**
 * GET /api/review/queue
 * Returns papers with status "awaiting-review", sorted by uploadedAt.
 */
import { NextResponse } from "next/server";
import { Firestore } from "@google-cloud/firestore";

const db = new Firestore({ projectId: process.env.GCP_PROJECT });

export async function GET() {
  const snapshot = await db
    .collection("papers")
    .where("status", "==", "awaiting-review")
    .orderBy("uploadedAt", "asc")
    .limit(50)
    .get();

  const papers = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
  return NextResponse.json({ papers });
}
