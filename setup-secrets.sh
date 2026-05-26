#!/usr/bin/env bash
# =============================================================================
# MoPoTools — Secret Manager population script
# Run this after deploy.sh to add or rotate any secret values.
# =============================================================================
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; RESET='\033[0m'

info()    { echo -e "${BLUE}▶${RESET} $*"; }
success() { echo -e "${GREEN}✓${RESET} $*"; }
warn()    { echo -e "${YELLOW}⚠${RESET} $*"; }
error()   { echo -e "${RED}✗${RESET} $*"; exit 1; }

# Detect project from gcloud config or ask
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [[ -z "$PROJECT_ID" || "$PROJECT_ID" == "(unset)" ]]; then
  read -rp "GCP project ID: " PROJECT_ID
fi
info "Using project: $PROJECT_ID"

# ── Secret helper ─────────────────────────────────────────────────────────────
set_secret() {
  local SECRET_NAME="$1"
  local DESCRIPTION="$2"
  local HINT="$3"

  echo ""
  echo -e "${BOLD}$SECRET_NAME${RESET}"
  echo -e "  Description : $DESCRIPTION"
  echo -e "  Where to get: $HINT"
  read -rsp "  Value (hidden): " VALUE
  echo ""

  if [[ -z "$VALUE" ]]; then
    warn "Skipped (press Enter with a value to set it)"
    return
  fi

  # Create secret if it doesn't exist yet
  if ! gcloud secrets describe "$SECRET_NAME" --project="$PROJECT_ID" &>/dev/null; then
    gcloud secrets create "$SECRET_NAME" \
      --project="$PROJECT_ID" \
      --replication-policy="automatic" \
      --quiet
  fi

  echo -n "$VALUE" | gcloud secrets versions add "$SECRET_NAME" \
    --project="$PROJECT_ID" \
    --data-file=-

  success "Secret '$SECRET_NAME' updated (version added)"
}

# ── Secrets ───────────────────────────────────────────────────────────────────

echo -e "\n${BOLD}━━━ MoPoTools Secret Setup ━━━${RESET}"
echo "Leave any field blank to skip it."

set_secret \
  "vertex-ai-api-key" \
  "API key for Vertex AI Gemini (used by generate-wiki and run-lint functions)" \
  "GCP Console → APIs & Services → Credentials → Create API Key. Restrict to Vertex AI API."

set_secret \
  "document-ai-processor-id" \
  "Document AI processor resource ID for text extraction" \
  "GCP Console → Document AI → Processors → your processor → copy the ID from the URL"

set_secret \
  "github-token" \
  "GitHub Personal Access Token — allows moderator approval to commit wiki pages" \
  "github.com → Settings → Developer settings → Personal access tokens → Fine-grained token.
   Required permissions: Contents (read/write), Metadata (read). Scope: your wiki repo only."

set_secret \
  "sendgrid-api-key" \
  "SendGrid API key for weekly lint report emails" \
  "app.sendgrid.com → Settings → API Keys → Create API Key (Mail Send permission only)"

set_secret \
  "iap-client-secret" \
  "OAuth 2.0 client secret for Identity-Aware Proxy" \
  "GCP Console → APIs & Services → Credentials → OAuth 2.0 Client IDs → your IAP client"

# ── Verify ────────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}Current secret versions:${RESET}"
for SECRET in vertex-ai-api-key document-ai-processor-id github-token sendgrid-api-key iap-client-secret; do
  VERSION=$(gcloud secrets versions list "$SECRET" \
    --project="$PROJECT_ID" \
    --filter="state=ENABLED" \
    --format="value(name)" 2>/dev/null | tail -1)
  if [[ -n "$VERSION" ]]; then
    echo -e "  ${GREEN}✓${RESET} $SECRET  →  $VERSION"
  else
    echo -e "  ${YELLOW}–${RESET} $SECRET  →  not set"
  fi
done

echo ""
success "Done. Functions will pick up new secret versions on their next cold start."
