/**
 * Client-side port of page_writer.py — validates wiki page format
 * so the moderator UI can flag issues before approval.
 */

const REQUIRED_FIELDS = ["Summary", "Research classification", "Sources", "Last updated"];
const VALID_CLASSIFICATIONS = new Set(["empirical", "theoretical", "both"]);

export function validate_page(
  slug: string,
  content: string
): { errors: string[]; warnings: string[] } {
  const errors: string[] = [];
  const warnings: string[] = [];

  // 1. Must start with a # heading
  if (!content.trimStart().startsWith("# ")) {
    errors.push("Page must start with a # heading");
  }

  // 2. Required header fields
  for (const field of REQUIRED_FIELDS) {
    if (!content.includes(`**${field}**`)) {
      errors.push(`Missing required field: **${field}**`);
    }
  }

  // 3. Research classification value
  const clsMatch = content.match(/\*\*Research classification\*\*\s*:\s*(.+)/);
  if (clsMatch) {
    const cls = clsMatch[1].trim().toLowerCase();
    if (!VALID_CLASSIFICATIONS.has(cls)) {
      errors.push(`**Research classification** must be empirical, theoretical, or both — got "${cls}"`);
    }
  }

  // 4. Must have Related pages section
  if (!content.includes("## Related pages")) {
    errors.push("Missing ## Related pages section");
  }

  // 5. Warn on wiki-links with uppercase or spaces
  const wikiLinks = [...content.matchAll(/\[\[([^\]]+)\]\]/g)].map((m) => m[1]);
  for (const link of wikiLinks) {
    if (link !== link.toLowerCase()) {
      warnings.push(`Wiki-link [[${link}]] should be lowercase`);
    }
    if (link.includes(" ")) {
      warnings.push(`Wiki-link [[${link}]] contains spaces — use hyphens`);
    }
  }

  // 6. Warn on potentially bare numbers
  const bareNumbers = content.match(/(?<!\w)(\d+(?:\.\d+)?)(?!\s*(?:%|bp|bps|bn|billion|million|trillion|percent|pp|USD|GBP|EUR|SEK|JPY|\w))/g);
  if (bareNumbers && bareNumbers.length > 0) {
    warnings.push(`${bareNumbers.length} potentially bare numeric value(s) — ensure all numbers include units`);
  }

  return { errors, warnings };
}
