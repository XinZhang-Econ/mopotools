"use client";

import { useEffect, useState } from "react";

type Paper = {
  slug: string;
  title: string;
  authors: string[];
  year: number;
  tag: string;
  uploader: string;
  uploadedAt: string;
  status: string;
  pagesGenerated?: string[];
  conceptsCreated?: string[];
  conceptsUpdated?: string[];
  swedenCheck?: string;
};

type PageDiff = {
  slug: string;
  isNew: boolean;
  content: string;
  validationErrors: string[];
  validationWarnings: string[];
};

type ReviewDetail = {
  paper: Paper;
  pages: PageDiff[];
  logEntry: string;
  discussion: any;
  swedenCheck: { ok: boolean; violations: any[] };
};

export default function ReviewQueuePage() {
  const [papers, setPapers] = useState<Paper[]>([]);
  const [selected, setSelected] = useState<ReviewDetail | null>(null);
  const [activePageIdx, setActivePageIdx] = useState(0);
  const [loading, setLoading] = useState(false);
  const [actionMsg, setActionMsg] = useState("");

  useEffect(() => {
    fetchQueue();
  }, []);

  async function fetchQueue() {
    const res = await fetch("/api/review/queue");
    const data = await res.json();
    setPapers(data.papers ?? []);
  }

  async function openReview(slug: string) {
    setLoading(true);
    setActionMsg("");
    const res = await fetch(`/api/review/${slug}`);
    const data = await res.json();
    setSelected(data);
    setActivePageIdx(0);
    setLoading(false);
  }

  async function handleDecision(slug: string, decision: "approve" | "reject", note?: string) {
    setLoading(true);
    const res = await fetch(`/api/review/${slug}/${decision}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ note }),
    });
    const data = await res.json();
    setActionMsg(data.message ?? decision);
    setSelected(null);
    await fetchQueue();
    setLoading(false);
  }

  const statusColor: Record<string, string> = {
    "awaiting-review":      "bg-yellow-100 text-yellow-800",
    "sweden-check-failed":  "bg-red-100 text-red-800",
    "published":            "bg-green-100 text-green-800",
    "rejected":             "bg-gray-100 text-gray-600",
  };

  return (
    <main className="max-w-6xl mx-auto pt-10 px-4">
      <h1 className="text-2xl font-bold mb-1">Moderator Review Queue</h1>
      <p className="text-sm text-gray-500 mb-6">
        Review AI-generated wiki pages before they are published.
      </p>

      {actionMsg && (
        <div className="mb-4 px-4 py-3 bg-blue-50 border border-blue-200 rounded-lg text-sm text-blue-800">
          {actionMsg}
        </div>
      )}

      {/* Queue list */}
      {!selected && (
        <div className="space-y-3">
          {papers.length === 0 && (
            <p className="text-gray-400 text-sm">No papers awaiting review.</p>
          )}
          {papers.map((p) => (
            <div
              key={p.slug}
              className="border rounded-xl p-4 flex items-center justify-between hover:bg-gray-50"
            >
              <div>
                <p className="font-medium text-sm">{p.title}</p>
                <p className="text-xs text-gray-500 mt-0.5">
                  {p.authors?.join(", ")} · {p.year} ·{" "}
                  <span className="font-mono">{p.slug}</span>
                </p>
                <span className={`mt-1 inline-block text-xs px-2 py-0.5 rounded-full font-medium ${statusColor[p.status] ?? "bg-gray-100"}`}>
                  {p.status}
                </span>
              </div>
              {p.status === "awaiting-review" && (
                <button
                  onClick={() => openReview(p.slug)}
                  disabled={loading}
                  className="px-3 py-1.5 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700 disabled:opacity-50"
                >
                  Review
                </button>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Review detail panel */}
      {selected && (
        <div className="space-y-6">
          {/* Header */}
          <div className="flex items-start justify-between">
            <div>
              <h2 className="text-lg font-semibold">{selected.paper.title}</h2>
              <p className="text-sm text-gray-500">
                {selected.paper.authors?.join(", ")} · {selected.paper.year} · {selected.paper.tag}
              </p>
            </div>
            <button onClick={() => setSelected(null)} className="text-sm text-gray-400 hover:text-gray-700">
              ← Back to queue
            </button>
          </div>

          {/* Sweden check banner */}
          {selected.swedenCheck.ok ? (
            <div className="flex items-center gap-2 px-4 py-3 bg-green-50 border border-green-200 rounded-lg text-sm text-green-800">
              <span>✓</span> Sweden attribution check passed.
            </div>
          ) : (
            <div className="px-4 py-3 bg-red-50 border border-red-200 rounded-lg text-sm text-red-800">
              <p className="font-semibold mb-1">⚠ Sweden check violations</p>
              {selected.swedenCheck.violations.map((v, i) => (
                <p key={i} className="mt-1">
                  <span className="font-mono">{v.page_slug}</span>: {v.issue}
                </p>
              ))}
            </div>
          )}

          {/* Page tabs */}
          <div>
            <div className="flex gap-2 flex-wrap mb-3">
              {selected.pages.map((p, i) => (
                <button
                  key={p.slug}
                  onClick={() => setActivePageIdx(i)}
                  className={`px-3 py-1 rounded-lg text-sm ${
                    i === activePageIdx
                      ? "bg-blue-600 text-white"
                      : "bg-gray-100 text-gray-700 hover:bg-gray-200"
                  }`}
                >
                  {p.isNew ? "✦ " : ""}{p.slug}
                  {p.validationErrors.length > 0 && <span className="ml-1 text-red-400">!</span>}
                </button>
              ))}
            </div>

            {selected.pages[activePageIdx] && (
              <div className="border rounded-xl overflow-hidden">
                {/* Validation errors/warnings */}
                {selected.pages[activePageIdx].validationErrors.length > 0 && (
                  <div className="bg-red-50 border-b border-red-200 px-4 py-2">
                    {selected.pages[activePageIdx].validationErrors.map((e, i) => (
                      <p key={i} className="text-xs text-red-700">⚠ {e}</p>
                    ))}
                  </div>
                )}
                {selected.pages[activePageIdx].validationWarnings.length > 0 && (
                  <div className="bg-yellow-50 border-b border-yellow-200 px-4 py-2">
                    {selected.pages[activePageIdx].validationWarnings.map((w, i) => (
                      <p key={i} className="text-xs text-yellow-700">ⓘ {w}</p>
                    ))}
                  </div>
                )}
                {/* Page content */}
                <pre className="p-4 text-xs font-mono overflow-auto max-h-96 bg-gray-50 whitespace-pre-wrap">
                  {selected.pages[activePageIdx].content}
                </pre>
              </div>
            )}
          </div>

          {/* Log entry preview */}
          <div>
            <p className="text-sm font-medium mb-1 text-gray-600">log.md entry to be appended:</p>
            <pre className="bg-gray-50 border rounded-lg p-3 text-xs font-mono text-gray-700 whitespace-pre-wrap">
              {selected.logEntry}
            </pre>
          </div>

          {/* Actions */}
          <div className="flex gap-3 pt-2">
            <button
              onClick={() => handleDecision(selected.paper.slug, "approve")}
              disabled={loading || selected.pages.some(p => p.validationErrors.length > 0)}
              className="px-5 py-2.5 bg-green-600 text-white text-sm rounded-lg font-medium
                         hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? "Processing…" : "Approve & Publish"}
            </button>
            <button
              onClick={() => {
                const note = prompt("Rejection reason (optional):");
                handleDecision(selected.paper.slug, "reject", note ?? undefined);
              }}
              disabled={loading}
              className="px-5 py-2.5 bg-gray-200 text-gray-700 text-sm rounded-lg font-medium
                         hover:bg-gray-300 disabled:opacity-50"
            >
              Reject
            </button>
          </div>
          {selected.pages.some(p => p.validationErrors.length > 0) && (
            <p className="text-xs text-red-600">
              Cannot approve — fix validation errors in the flagged pages first.
            </p>
          )}
        </div>
      )}
    </main>
  );
}
