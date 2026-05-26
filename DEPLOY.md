# Deploying MoPoTools Wiki to GitHub Pages

This guide walks you through hosting the wiki for free using Quartz + GitHub Pages.

## Prerequisites

- [Node.js](https://nodejs.org/) v18 or higher
- [Git](https://git-scm.com/)
- A GitHub account

## Quick Setup (Automated)

Run the setup script:

```bash
cd /Users/zhang/Documents/Obsidian\ Vault/Wiki/MoPoTools
chmod +x setup-quartz.sh
./setup-quartz.sh
```

Follow the prompts and instructions.

## Manual Setup

### Step 1: Clone Quartz

```bash
cd /Users/zhang/Documents/Obsidian\ Vault/Wiki
git clone https://github.com/jackyzha0/quartz.git mopo-wiki
cd mopo-wiki
npm i
```

### Step 2: Copy Wiki Content

```bash
rm -rf content/*
cp -r ../MoPoTools/wiki/* content/
```

### Step 3: Configure Quartz

Edit `quartz.config.ts`:

```typescript
configuration: {
  pageTitle: "Monetary Policy Tools Wiki",
  baseUrl: "YOUR_USERNAME.github.io/mopo-wiki",  // <-- Update this
  // ...
}
```

Or copy the pre-configured file:

```bash
cp ../MoPoTools/quartz.config.ts .
# Then edit baseUrl with your GitHub username
```

### Step 4: Preview Locally

```bash
npx quartz build --serve
```

Open http://localhost:8080 to preview.

### Step 5: Create GitHub Repository

1. Go to https://github.com/new
2. Create a **public** repository named `mopo-wiki`
3. Do NOT initialize with README

### Step 6: Push to GitHub

```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit: MoPoTools Wiki"
git remote add origin https://github.com/YOUR_USERNAME/mopo-wiki.git
git branch -M main
git push -u origin main
```

### Step 7: Enable GitHub Pages

1. Go to your repository Settings → Pages
2. Under "Build and deployment", select **GitHub Actions** as the source
3. Quartz includes a workflow that will auto-deploy

### Step 8: Deploy

```bash
npx quartz sync
```

Your wiki will be live at: `https://YOUR_USERNAME.github.io/mopo-wiki`

## Updating the Wiki

When you update wiki pages in the original location:

```bash
cd /Users/zhang/Documents/Obsidian\ Vault/Wiki/mopo-wiki

# Copy updated content
cp -r ../MoPoTools/wiki/* content/

# Deploy
npx quartz sync
```

## Custom Domain (Optional)

To use a custom domain like `wiki.yourdomain.com`:

1. Add a `CNAME` file in `content/` with your domain
2. Configure DNS with your domain registrar
3. Update `baseUrl` in `quartz.config.ts`

## Troubleshooting

### Build Errors

```bash
# Clean rebuild
rm -rf .quartz-cache
npx quartz build
```

### Wiki Links Not Working

Ensure links use the format `[[page-name]]` (with hyphens, lowercase).

### Images Not Showing

Place images in `content/` and reference with relative paths.

## Cost

- GitHub Pages: **Free** (for public repositories)
- Bandwidth: 100GB/month soft limit (more than enough for personal use)
- Custom domain: Optional, depends on registrar

## File Structure

```
mopo-wiki/
├── content/           # Your wiki markdown files go here
│   ├── index.md
│   ├── quantitative-easing.md
│   ├── qe-sweden.md
│   └── ...
├── quartz.config.ts   # Site configuration
├── quartz.layout.ts   # Layout configuration
└── quartz/            # Quartz source (don't modify)
```
