#!/usr/bin/env bash
# =============================================================================
# MoPoTools — GCP Deployment Script
# Run this from the root of the MoPoTools directory on your local machine.
# Prerequisites: gcloud CLI, terraform >= 1.6, docker, git, node >= 18
# =============================================================================
set -euo pipefail

# ── Colours ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; RESET='\033[0m'

info()    { echo -e "${BLUE}▶${RESET} $*"; }
success() { echo -e "${GREEN}✓${RESET} $*"; }
warn()    { echo -e "${YELLOW}⚠${RESET} $*"; }
error()   { echo -e "${RED}✗${RESET} $*"; exit 1; }
header()  { echo -e "\n${BOLD}━━━ $* ━━━${RESET}"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# =============================================================================
# 1. PREREQUISITES
# =============================================================================
header "Checking prerequisites"

check_cmd() {
  if ! command -v "$1" &>/dev/null; then
    error "$1 is not installed. $2"
  fi
  success "$1 found"
}

check_cmd gcloud   "Install from https://cloud.google.com/sdk/docs/install"
check_cmd terraform "Install from https://developer.hashicorp.com/terraform/install"
check_cmd docker   "Install from https://docs.docker.com/get-docker/"
check_cmd git      "Install from https://git-scm.com/"
check_cmd node     "Install from https://nodejs.org/ (v18+)"

# Check terraform version >= 1.6
TF_VERSION=$(terraform version -json | python3 -c "import sys,json; print(json.load(sys.stdin)['terraform_version'])")
TF_MAJOR=$(echo "$TF_VERSION" | cut -d. -f1)
TF_MINOR=$(echo "$TF_VERSION" | cut -d. -f2)
if [[ "$TF_MAJOR" -lt 1 ]] || { [[ "$TF_MAJOR" -eq 1 ]] && [[ "$TF_MINOR" -lt 6 ]]; }; then
  error "Terraform >= 1.6 required (found $TF_VERSION)"
fi
success "Terraform $TF_VERSION"

# =============================================================================
# 2. GATHER INPUTS
# =============================================================================
header "Configuration"

read -rp "$(echo -e "${BOLD}GitHub username${RESET}: ")" GITHUB_USER
read -rp "$(echo -e "${BOLD}GitHub repo name${RESET} [mopotools]: ")" GITHUB_REPO
GITHUB_REPO="${GITHUB_REPO:-mopotools}"

read -rp "$(echo -e "${BOLD}GCP project ID${RESET} (leave blank to auto-generate): ")" PROJECT_ID
if [[ -z "$PROJECT_ID" ]]; then
  PROJECT_ID="mopotools-$(LC_ALL=C tr -dc 'a-z0-9' < /dev/urandom | head -c 6)"
  info "Generated project ID: $PROJECT_ID"
fi

read -rp "$(echo -e "${BOLD}GCP region${RESET} [europe-west1]: ")" REGION
REGION="${REGION:-europe-west1}"

read -rp "$(echo -e "${BOLD}Admin email${RESET}: ")" ADMIN_EMAIL

echo ""
echo -e "${BOLD}Summary:${RESET}"
echo "  GCP Project : $PROJECT_ID"
echo "  Region      : $REGION"
echo "  GitHub repo : github.com/$GITHUB_USER/$GITHUB_REPO"
echo "  Admin email : $ADMIN_EMAIL"
echo ""
read -rp "Continue? [y/N] " CONFIRM
[[ "$(echo "$CONFIRM" | tr '[:upper:]' '[:lower:]')" == "y" ]] || { echo "Aborted."; exit 0; }

# =============================================================================
# 3. GCP PROJECT
# =============================================================================
header "Setting up GCP project"

# Check if project already exists
if gcloud projects describe "$PROJECT_ID" &>/dev/null; then
  warn "Project $PROJECT_ID already exists — using it"
else
  info "Creating GCP project $PROJECT_ID ..."
  gcloud projects create "$PROJECT_ID" \
    --name="MoPoTools Wiki" \
    --labels="app=mopotools"
  success "Project created: $PROJECT_ID"
fi

gcloud config set project "$PROJECT_ID"
success "Active project set to $PROJECT_ID"

# Check billing — must be linked manually before APIs can be enabled
echo ""
warn "Billing check: ensure billing is enabled for project $PROJECT_ID"
echo "  → https://console.cloud.google.com/billing/linkedaccount?project=$PROJECT_ID"
read -rp "Press Enter once billing is linked (or it's already linked)... "

# =============================================================================
# 4. TERRAFORM STATE BUCKET
# =============================================================================
header "Terraform remote state bucket"

STATE_BUCKET="${PROJECT_ID}-1029254416121-tfstate"
if gsutil ls -b "gs://$STATE_BUCKET" &>/dev/null; then
  warn "State bucket gs://$STATE_BUCKET already exists"
else
  info "Creating Terraform state bucket ..."
  gsutil mb -p "$PROJECT_ID" -l "$REGION" "gs://$STATE_BUCKET"
  gsutil versioning set on "gs://$STATE_BUCKET"
  gsutil ubla set on "gs://$STATE_BUCKET"
  success "State bucket created: gs://$STATE_BUCKET"
fi

# =============================================================================
# 5. TERRAFORM TFVARS
# =============================================================================
header "Terraform variables"

TFVARS="infra/terraform.tfvars"
if [[ -f "$TFVARS" ]]; then
  warn "$TFVARS already exists — skipping (delete it to regenerate)"
else
  cat > "$TFVARS" <<EOF
project_id  = "$PROJECT_ID"
region      = "$REGION"
admin_email = "$ADMIN_EMAIL"
wiki_repo   = "$GITHUB_USER/$GITHUB_REPO"
EOF
  success "Created $TFVARS"
fi

# Update backend bucket in main.tf
sed -i.bak "s/mopotools-tfstate/$STATE_BUCKET/" infra/main.tf
rm -f infra/main.tf.bak
success "Updated Terraform backend to gs://$STATE_BUCKET"

# =============================================================================
# 6. TERRAFORM APPLY
# =============================================================================
header "Terraform — init + apply"

cd infra
terraform init \
  -backend-config="bucket=$STATE_BUCKET" \
  -backend-config="prefix=terraform/state" \
  -reconfigure

terraform plan -var-file=terraform.tfvars -out=tfplan
echo ""
read -rp "Apply this plan? [y/N] " TF_CONFIRM
TF_CONFIRM_LC="$(echo "$TF_CONFIRM" | tr '[:upper:]' '[:lower:]')"
[[ "$TF_CONFIRM_LC" == "y" ]] || { echo "Skipped terraform apply."; cd ..; }

if [[ "$TF_CONFIRM_LC" == "y" ]]; then
  terraform apply tfplan
  success "Terraform apply complete"
  rm -f tfplan
  cd ..
fi

# =============================================================================
# 7. GITHUB REPOSITORY
# =============================================================================
header "GitHub repository"

if git remote get-url origin &>/dev/null; then
  warn "Git remote 'origin' already set: $(git remote get-url origin)"
else
  echo ""
  echo "  Create a new GitHub repository:"
  echo "  1. Go to https://github.com/new"
  echo "  2. Name it: $GITHUB_REPO"
  echo "  3. Keep it private (recommended)"
  echo "  4. Do NOT initialise with README"
  echo ""
  read -rp "Press Enter once the repository is created... "

  git init
  git add .
  git commit -m "chore: initial MoPoTools commit"
  git branch -M main
  git remote add origin "https://github.com/$GITHUB_USER/$GITHUB_REPO.git"
  git push -u origin main
  success "Pushed to github.com/$GITHUB_USER/$GITHUB_REPO"
fi

# =============================================================================
# 8. DOCUMENT AI PROCESSOR
# =============================================================================
header "Document AI processor"

echo ""
warn "You need to create a Document AI processor manually (one-time):"
echo "  1. Go to https://console.cloud.google.com/ai/document-ai?project=$PROJECT_ID"
echo "  2. Click 'Create Processor'"
echo "  3. Choose 'Document OCR' (General)"
echo "  4. Region: $REGION"
echo "  5. Note the Processor ID (looks like: abc1234567890def)"
echo ""
read -rp "Enter your Document AI Processor ID: " DOCAI_PROCESSOR_ID

# =============================================================================
# 9. SECRETS
# =============================================================================
header "Populating Secret Manager"

echo ""
echo "You will be prompted for each secret value."
echo "For Vertex AI — you can use Application Default Credentials instead of an API key."
echo "Press Enter to skip a secret and set it later via setup-secrets.sh"
echo ""

set_secret() {
  local SECRET_NAME="$1"
  local PROMPT="$2"
  read -rsp "$(echo -e "${BOLD}$PROMPT${RESET} (input hidden): ")" SECRET_VAL
  echo ""
  if [[ -n "$SECRET_VAL" ]]; then
    echo -n "$SECRET_VAL" | gcloud secrets versions add "$SECRET_NAME" \
      --project="$PROJECT_ID" --data-file=-
    success "Secret '$SECRET_NAME' set"
  else
    warn "Skipped '$SECRET_NAME' — set it later with: ./setup-secrets.sh"
  fi
}

# Document AI processor ID (from step above)
if [[ -n "$DOCAI_PROCESSOR_ID" ]]; then
  echo -n "$DOCAI_PROCESSOR_ID" | gcloud secrets versions add "document-ai-processor-id" \
    --project="$PROJECT_ID" --data-file=-
  success "Secret 'document-ai-processor-id' set"
fi

set_secret "vertex-ai-api-key"  "Vertex AI API key (from GCP Console → APIs → Credentials)"
set_secret "github-token"       "GitHub Personal Access Token (needs repo + contents:write scope)"
set_secret "sendgrid-api-key"   "SendGrid API key (for weekly lint report emails)"

# =============================================================================
# 10. BUILD & PUSH DOCKER IMAGES
# =============================================================================
header "Building Docker images"

# Configure Docker to use gcloud credentials
gcloud auth configure-docker --quiet

# Enable Container Registry (or Artifact Registry)
gcloud services enable containerregistry.googleapis.com --project="$PROJECT_ID" --quiet

# Build frontend image
info "Building frontend image ..."
gcloud builds submit ./frontend \
  --tag "gcr.io/$PROJECT_ID/mopotools-frontend:latest" \
  --project="$PROJECT_ID"
success "Frontend image pushed: gcr.io/$PROJECT_ID/mopotools-frontend:latest"

# Build initial wiki site image (uses current wiki/ content)
info "Building wiki site image ..."
gcloud builds submit . \
  --config wiki-site/cloudbuild.yaml \
  --project="$PROJECT_ID" \
  --substitutions="_PROJECT_ID=$PROJECT_ID"
success "Wiki site image built and deployed"

# =============================================================================
# 11. DEPLOY CLOUD RUN (update images after build)
# =============================================================================
header "Deploying Cloud Run services"

info "Deploying frontend ..."
gcloud run deploy mopotools-frontend \
  --image "gcr.io/$PROJECT_ID/mopotools-frontend:latest" \
  --region "$REGION" \
  --service-account "mopotools-frontend@$PROJECT_ID.iam.gserviceaccount.com" \
  --set-env-vars "GCP_PROJECT=$PROJECT_ID,RAW_BUCKET=${PROJECT_ID}-mopotools-raw,STAGING_BUCKET=${PROJECT_ID}-mopotools-staging,WIKI_REPO=$GITHUB_USER/$GITHUB_REPO" \
  --set-secrets "GITHUB_TOKEN=github-token:latest" \
  --no-allow-unauthenticated \
  --platform managed \
  --project="$PROJECT_ID" \
  --quiet
success "Frontend deployed"

# =============================================================================
# 12. DEPLOY CLOUD FUNCTIONS
# =============================================================================
header "Deploying Cloud Functions"

deploy_function() {
  local NAME="$1"
  local ENTRY="$2"
  local DIR="$3"
  local TIMEOUT="${4:-540}"
  local MEMORY="${5:-1024Mi}"
  local EXTRA_ENV="${6:-}"

  info "Deploying $NAME ..."
  gcloud functions deploy "$NAME" \
    --gen2 \
    --runtime=python312 \
    --region="$REGION" \
    --source="$DIR" \
    --entry-point="$ENTRY" \
    --trigger-http \
    --no-allow-unauthenticated \
    --service-account="mopotools-pipeline@$PROJECT_ID.iam.gserviceaccount.com" \
    --timeout="${TIMEOUT}s" \
    --memory="$MEMORY" \
    --set-env-vars "GCP_PROJECT=$PROJECT_ID,PROCESSED_BUCKET=${PROJECT_ID}-mopotools-processed,STAGING_BUCKET=${PROJECT_ID}-mopotools-staging,WIKI_REPO=$GITHUB_USER/$GITHUB_REPO,ADMIN_EMAIL=$ADMIN_EMAIL${EXTRA_ENV:+,$EXTRA_ENV}" \
    --set-secrets "DOCUMENT_AI_PROCESSOR_ID=document-ai-processor-id:latest,VERTEX_AI_API_KEY=vertex-ai-api-key:latest,SENDGRID_API_KEY=sendgrid-api-key:latest,GITHUB_TOKEN=github-token:latest" \
    --project="$PROJECT_ID" \
    --quiet
  success "$NAME deployed"
}

deploy_function "mopotools-extract-text"  "extract_text"   "functions/extract-text"  "540"  "1024Mi"
deploy_function "mopotools-generate-wiki" "generate_wiki"  "functions/generate-wiki" "1800" "2048Mi"
deploy_function "mopotools-run-lint"      "run_lint"       "functions/run-lint"       "540"  "512Mi"

# =============================================================================
# 13. UPDATE WORKFLOW WITH FUNCTION URLs
# =============================================================================
header "Wiring Cloud Workflows to function URLs"

EXTRACT_URL=$(gcloud functions describe mopotools-extract-text \
  --region="$REGION" --project="$PROJECT_ID" \
  --format="value(serviceConfig.uri)" 2>/dev/null)

GENERATE_URL=$(gcloud functions describe mopotools-generate-wiki \
  --region="$REGION" --project="$PROJECT_ID" \
  --format="value(serviceConfig.uri)" 2>/dev/null)

# Update the workflow with the actual function URLs
sed -i.bak \
  "s|sys.get_env(\"EXTRACT_TEXT_URL\")|\"$EXTRACT_URL\"|g;
   s|sys.get_env(\"GENERATE_WIKI_URL\")|\"$GENERATE_URL\"|g" \
  workflows/ingest.yaml
rm -f workflows/ingest.yaml.bak

# Redeploy workflow with updated URLs
gcloud workflows deploy mopotools-ingest \
  --location="$REGION" \
  --source="workflows/ingest.yaml" \
  --service-account="mopotools-pipeline@$PROJECT_ID.iam.gserviceaccount.com" \
  --project="$PROJECT_ID"
success "Cloud Workflow redeployed with function URLs"

# =============================================================================
# 14. CLOUD BUILD TRIGGER FOR WIKI SITE
# =============================================================================
header "Cloud Build trigger — wiki auto-rebuild"

gcloud builds triggers create github \
  --repo-name="$GITHUB_REPO" \
  --repo-owner="$GITHUB_USER" \
  --branch-pattern="^main$" \
  --build-config="wiki-site/cloudbuild.yaml" \
  --included-files="wiki/**,wiki-site/**" \
  --name="mopotools-wiki-rebuild" \
  --project="$PROJECT_ID" 2>/dev/null || warn "Trigger may already exist — skipping"

success "Cloud Build trigger configured"

# =============================================================================
# 15. FIRESTORE SECURITY RULES
# =============================================================================
header "Deploying Firestore security rules"

if command -v firebase &>/dev/null; then
  firebase deploy --only firestore:rules --project="$PROJECT_ID"
  success "Firestore rules deployed"
else
  warn "Firebase CLI not found — deploy Firestore rules manually:"
  echo "  npm install -g firebase-tools"
  echo "  firebase login"
  echo "  firebase deploy --only firestore:rules --project=$PROJECT_ID"
fi

# =============================================================================
# 16. SUMMARY
# =============================================================================
header "Deployment complete"

FRONTEND_URL=$(gcloud run services describe mopotools-frontend \
  --region="$REGION" --project="$PROJECT_ID" \
  --format="value(status.url)" 2>/dev/null || echo "(run: gcloud run services describe mopotools-frontend --region=$REGION)")

WIKI_URL=$(gcloud run services describe mopotools-wiki \
  --region="$REGION" --project="$PROJECT_ID" \
  --format="value(status.url)" 2>/dev/null || echo "(run: gcloud run services describe mopotools-wiki --region=$REGION)")

echo ""
echo -e "${GREEN}${BOLD}Your MoPoTools deployment is live!${RESET}"
echo ""
echo -e "  ${BOLD}Wiki site${RESET}    : $WIKI_URL"
echo -e "  ${BOLD}Upload UI${RESET}    : $FRONTEND_URL/upload"
echo -e "  ${BOLD}Review queue${RESET} : $FRONTEND_URL/review"
echo -e "  ${BOLD}GCP Console${RESET}  : https://console.cloud.google.com/home/dashboard?project=$PROJECT_ID"
echo ""
echo -e "${BOLD}Next steps:${RESET}"
echo "  1. Add permitted users: GCP Console → IAP → add email with 'IAP-Secured Web App User' role"
echo "  2. Set up a custom domain (optional): see DEPLOY_GCP.md § Custom Domain"
echo "  3. Run ./setup-secrets.sh if you skipped any secrets above"
echo ""
echo "  Lint reports will be emailed to $ADMIN_EMAIL every Monday at 08:00 UTC."
echo ""
