#!/bin/bash
# Setup script for MoPoTools Wiki with Quartz + GitHub Pages
# Run this script from the MoPoTools directory

set -e

echo "=== MoPoTools Wiki: Quartz Setup ==="
echo ""

# Check prerequisites
command -v node >/dev/null 2>&1 || { echo "Error: Node.js is required. Install from https://nodejs.org/"; exit 1; }
command -v git >/dev/null 2>&1 || { echo "Error: Git is required."; exit 1; }

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "Error: Node.js 18+ required. You have $(node -v)"
    exit 1
fi

echo "Prerequisites OK (Node $(node -v), Git $(git --version | cut -d' ' -f3))"
echo ""

# Get GitHub username
read -p "Enter your GitHub username: " GITHUB_USER
if [ -z "$GITHUB_USER" ]; then
    echo "Error: GitHub username required"
    exit 1
fi

REPO_NAME="mopo-wiki"
WIKI_DIR="$(pwd)/wiki"

echo ""
echo "Will create: https://${GITHUB_USER}.github.io/${REPO_NAME}"
echo ""

# Clone Quartz
echo "=== Step 1/5: Cloning Quartz ==="
cd ..
if [ -d "$REPO_NAME" ]; then
    echo "Directory $REPO_NAME already exists. Remove it first or choose a different name."
    exit 1
fi

git clone https://github.com/jackyzha0/quartz.git "$REPO_NAME"
cd "$REPO_NAME"

echo ""
echo "=== Step 2/5: Installing dependencies ==="
npm i

echo ""
echo "=== Step 3/5: Copying wiki content ==="
rm -rf content/*
cp -r "$WIKI_DIR"/* content/

echo ""
echo "=== Step 4/5: Configuring Quartz ==="
# Update baseUrl in quartz.config.ts
sed -i.bak "s|baseUrl: \".*\"|baseUrl: \"${GITHUB_USER}.github.io/${REPO_NAME}\"|" quartz.config.ts
rm -f quartz.config.ts.bak

# Update page title
sed -i.bak 's|pageTitle: ".*"|pageTitle: "Monetary Policy Tools Wiki"|' quartz.config.ts
rm -f quartz.config.ts.bak

echo ""
echo "=== Step 5/5: Setting up GitHub repository ==="
rm -rf .git
git init
git add .
git commit -m "Initial commit: MoPoTools Wiki"

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo "   Name: ${REPO_NAME}"
echo "   Make it PUBLIC (required for free GitHub Pages)"
echo ""
echo "2. Push to GitHub:"
echo "   cd $(pwd)"
echo "   git remote add origin https://github.com/${GITHUB_USER}/${REPO_NAME}.git"
echo "   git push -u origin main"
echo ""
echo "3. Enable GitHub Pages:"
echo "   Go to: https://github.com/${GITHUB_USER}/${REPO_NAME}/settings/pages"
echo "   Source: GitHub Actions"
echo ""
echo "4. Deploy (Quartz will auto-deploy via GitHub Actions):"
echo "   npx quartz sync"
echo ""
echo "5. Your wiki will be live at:"
echo "   https://${GITHUB_USER}.github.io/${REPO_NAME}"
echo ""
echo "To preview locally: npx quartz build --serve"
echo ""
