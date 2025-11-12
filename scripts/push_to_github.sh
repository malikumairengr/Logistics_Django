#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/malikumairengr/Logistics_Django.git"

if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "ERROR: Please set GITHUB_TOKEN environment variable before running this script."
  echo "You can create a token at https://github.com/settings/tokens (classic) or fine-grained tokens."
  exit 1
fi

echo "Initializing git repository (if not already initialized)..."
if [ ! -d .git ]; then
  git init
fi

echo "Adding files and creating commit..."
git add --all
if git show-ref --verify --quiet refs/heads/main; then
  git checkout main
else
  git checkout -b main
fi

if git diff --cached --quiet; then
  echo "No changes to commit."
else
  git commit -m "Initial commit: Logistics Django app"
fi

echo "Setting remote to repository: ${REPO_URL}"
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "https://${GITHUB_TOKEN}@github.com/malikumairengr/Logistics_Django.git"
else
  git remote add origin "https://${GITHUB_TOKEN}@github.com/malikumairengr/Logistics_Django.git"
fi

echo "Pushing to GitHub (main)..."
git push -u origin main

echo "Done. Consider removing the remote URL containing token afterward with:"
echo "  git remote set-url origin ${REPO_URL}"
