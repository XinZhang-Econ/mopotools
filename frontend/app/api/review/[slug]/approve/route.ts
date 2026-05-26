/**
 * POST /api/review/[slug]/approve
 * Copies staged pages from GCS to the wiki Git repository and triggers a
 * Cloud Build rebuild of the Quartz site.
 */

import { NextRequest, NextResponse } from "next/server";
import { Storage } from "@google-cloud/storage";
import { Firestore } from "@google-cloud/firestore";
import { Octokit } from "@octokit/rest";

const gcs            = new Storage();
const db             = new Firestore({ projectId: process.env.GCP_PROJECT });
const STAGING_BUCKET = process.env.STAGING_BUCKET!;
const WIKI_REPO      = process.env.WIKI_REPO!;          // "owner/repo"
const GITHUB_TOKEN   = process.env.GITHUB_TOKEN!;

export async function POST(
  req: NextRequest,
  { params }: { params: { slug: string } }
) {
  const { slug } = params;
  const { note } = await req.json().catch(() => ({ note: "" }));

  const octokit  = new Octokit({ auth: GITHUB_TOKEN });
  const [owner, repo] = WIKI_REPO.split("/");

  // List all staged files for this slug
  const [files] = await gcs.bucket(STAGING_BUCKET).getFiles({ prefix: `${slug}/wiki/` });

  if (files.length === 0) {
    return NextResponse.json({ error: "No staged files found" }, { status: 404 });
  }

  const committed: string[] = [];

  for (const file of files) {
    const content   = await file.download();
    const pageBytes = content[0];
    const filePath  = file.name.replace(`${slug}/`, "");   // wiki/page.md

    // Get current file SHA if it exists (needed for updates)
    let sha: string | undefined;
    try {
      const { data } = await octokit.repos.getContent({ owner, repo, path: filePath });
      if (!Array.isArray(data) && data.type === "file") {
        sha = data.sha;
      }
    } catch {
      // File doesn't exist yet — create it
    }

    await octokit.repos.createOrUpdateFileContents({
      owner,
      repo,
      path:    filePath,
      message: `ingest: ${slug} [auto]`,
      content: pageBytes.toString("base64"),
      sha,
    });

    committed.push(filePath);
  }

  // Append log entry to wiki/log.md
  const logBlob = gcs.bucket(STAGING_BUCKET).blob(`${slug}/log_entry.md`);
  try {
    const [logContent] = await logBlob.download();
    const logEntry = logContent.toString();

    let currentLogSha: string | undefined;
    let currentLog = "";
    try {
      const { data } = await octokit.repos.getContent({ owner, repo, path: "wiki/log.md" });
      if (!Array.isArray(data) && data.type === "file") {
        currentLogSha = data.sha;
        currentLog = Buffer.from(data.content, "base64").toString();
      }
    } catch {}

    const updatedLog = currentLog + "\n" + logEntry;
    await octokit.repos.createOrUpdateFileContents({
      owner,
      repo,
      path:    "wiki/log.md",
      message: `ingest: ${slug} — log [auto]`,
      content: Buffer.from(updatedLog).toString("base64"),
      sha:     currentLogSha,
    });
    committed.push("wiki/log.md");
  } catch (err) {
    console.warn(`Could not append log entry for ${slug}:`, err);
  }

  // Update Firestore
  await db.collection("papers").doc(slug).update({
    status:       "published",
    publishedAt:  new Date().toISOString(),
    reviewNote:   note ?? "",
    committedFiles: committed,
  });

  // Clean up staging files
  await Promise.all(files.map((f) => f.delete().catch(() => {})));

  return NextResponse.json({
    message: `Published ${committed.length} file(s) for "${slug}". Cloud Build will rebuild the wiki site shortly.`,
    committed,
  });
}
