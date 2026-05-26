"use client";

import { useState } from "react";

const POLICY_TAGS = [
  { value: "conventional",      label: "Conventional monetary policy" },
  { value: "conventional-qe",   label: "Conventional — Quantitative Easing" },
  { value: "unconventional",     label: "Unconventional monetary policy" },
  { value: "forward-guidance",   label: "Forward Guidance" },
  { value: "negative-rates",     label: "Negative Interest Rates" },
  { value: "yield-curve-control",label: "Yield Curve Control" },
];

type UploadStatus = "idle" | "uploading" | "processing" | "done" | "error";

export default function UploadPage() {
  const [file, setFile]         = useState<File | null>(null);
  const [title, setTitle]       = useState("");
  const [authors, setAuthors]   = useState("");
  const [year, setYear]         = useState("");
  const [tag, setTag]           = useState("");
  const [status, setStatus]     = useState<UploadStatus>("idle");
  const [slug, setSlug]         = useState("");
  const [error, setError]       = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!file || !title || !authors || !year || !tag) return;

    setStatus("uploading");
    setError("");

    try {
      // Step 1: Request a signed upload URL from the backend
      const metaRes = await fetch("/api/upload/init", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          filename: file.name,
          title,
          authors: authors.split(";").map((a) => a.trim()),
          year: parseInt(year, 10),
          tag,
        }),
      });

      if (!metaRes.ok) throw new Error(await metaRes.text());
      const { signedUrl, slug: paperSlug } = await metaRes.json();
      setSlug(paperSlug);

      // Step 2: Upload directly to Cloud Storage
      const uploadRes = await fetch(signedUrl, {
        method: "PUT",
        headers: { "Content-Type": file.type },
        body: file,
      });
      if (!uploadRes.ok) throw new Error("Upload to Cloud Storage failed");

      // Step 3: Confirm upload to trigger the pipeline
      await fetch("/api/upload/confirm", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slug: paperSlug }),
      });

      setStatus("done");
    } catch (err: any) {
      setError(err.message ?? "Upload failed");
      setStatus("error");
    }
  }

  if (status === "done") {
    return (
      <main className="max-w-xl mx-auto pt-16 px-4">
        <div className="rounded-xl border border-green-200 bg-green-50 p-8 text-center">
          <p className="text-2xl font-semibold text-green-800 mb-2">Paper submitted</p>
          <p className="text-green-700 text-sm mb-4">
            Slug: <code className="font-mono bg-green-100 px-1 rounded">{slug}</code>
          </p>
          <p className="text-green-600 text-sm">
            The pipeline is extracting text and generating wiki pages. You will be notified when
            the paper is ready for moderator review.
          </p>
          <button
            onClick={() => { setStatus("idle"); setFile(null); setTitle(""); setAuthors(""); setYear(""); setTag(""); }}
            className="mt-6 px-4 py-2 bg-green-700 text-white rounded-lg text-sm hover:bg-green-800"
          >
            Upload another paper
          </button>
        </div>
      </main>
    );
  }

  return (
    <main className="max-w-xl mx-auto pt-12 px-4">
      <h1 className="text-2xl font-bold mb-1">Upload a paper</h1>
      <p className="text-sm text-gray-500 mb-8">
        PDF or DOCX. The pipeline will generate wiki pages and queue them for review.
      </p>

      <form onSubmit={handleSubmit} className="space-y-5">
        {/* File */}
        <div>
          <label className="block text-sm font-medium mb-1">Paper file</label>
          <input
            type="file"
            accept=".pdf,.docx,.doc"
            onChange={(e) => setFile(e.target.files?.[0] ?? null)}
            className="block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4
                       file:rounded-lg file:border-0 file:bg-gray-100 file:text-gray-700
                       hover:file:bg-gray-200 cursor-pointer"
            required
          />
        </div>

        {/* Title */}
        <div>
          <label className="block text-sm font-medium mb-1">Title</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Full paper title"
            className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Authors */}
        <div>
          <label className="block text-sm font-medium mb-1">Authors</label>
          <input
            type="text"
            value={authors}
            onChange={(e) => setAuthors(e.target.value)}
            placeholder="Last, First; Last, First"
            className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
          <p className="text-xs text-gray-400 mt-1">Separate multiple authors with a semicolon.</p>
        </div>

        {/* Year */}
        <div>
          <label className="block text-sm font-medium mb-1">Year</label>
          <input
            type="number"
            value={year}
            onChange={(e) => setYear(e.target.value)}
            placeholder="2024"
            min={1990}
            max={2030}
            className="w-32 border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Policy tag */}
        <div>
          <label className="block text-sm font-medium mb-1">Policy type</label>
          <select
            value={tag}
            onChange={(e) => setTag(e.target.value)}
            className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          >
            <option value="" disabled>Select a policy type…</option>
            {POLICY_TAGS.map((t) => (
              <option key={t.value} value={t.value}>{t.label}</option>
            ))}
          </select>
        </div>

        {error && (
          <p className="text-sm text-red-600 bg-red-50 border border-red-200 rounded-lg px-3 py-2">
            {error}
          </p>
        )}

        <button
          type="submit"
          disabled={status === "uploading" || !file}
          className="w-full py-2.5 bg-blue-600 text-white rounded-lg text-sm font-medium
                     hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {status === "uploading" ? "Uploading…" : "Submit paper"}
        </button>
      </form>
    </main>
  );
}
