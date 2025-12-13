# Repository Guidelines
MkDocs Material site for Taiwan-focused investment content (zh-TW), centered on the 7-Level Stock Information Stack and published to GitHub Pages.

## Project Structure & Module Organization
- Root: `mkdocs.yml` controls nav/theme/plugins; `requirements.txt` pins MkDocs/Material plus macros/git/rss helpers.
- Content: `docs/` for pages (`index.md`, `about/`, `tag.md`), images in `docs/assets/images`, custom CSS/JS in `docs/stylesheets` and `docs/javascripts`.
- Blog: posts in `docs/blog/posts/`, authors in `docs/blog/.authors.yml`; keep zh-TW tone and stack terminology.
- Reports: `docs/reports/*` (often auto-generated—avoid manual edits) with DataTables behavior in `docs/javascripts/tables.js`.
- Overrides: `docs/overrides/` templates (e.g., `home.html`, `partials/footer.html`).

## Build, Test, and Development Commands
- `pip install -r requirements.txt` — install site dependencies.
- `mkdocs serve` — preview locally with live reload.
- `mkdocs build --strict` — validate nav, front matter, and links before merging.
- `mkdocs gh-deploy` — publish to GitHub Pages (requires access); CI deploys from `main`.

## Coding Style & Naming Conventions
- Markdown: use a single H1 per page; add YAML front matter when metadata matters (`title`, `date`, `tags`, `categories`, `draft`, `description`). Prefer concise sections and tables for structured data.
- Blog files: `YYYY-MM-DD-short-title.md`; keep tags/categories consistent (English or zh-TW), and set `draft: true` until ready.
- Links and assets: use relative links without `.md` extensions; place images in `docs/assets/images/` and reference them with relative paths.
- JavaScript: match `docs/javascripts/tables.js` style (4-space indent, semicolons, single quotes). Wire features via `document$.subscribe` so they survive instant navigation.
- CSS: scope additions in `docs/stylesheets/`; avoid broad overrides of Material defaults.

## Testing Guidelines
- Run `mkdocs build --strict` before opening PRs to catch missing assets, broken includes, and nav errors.
- For table or JS changes, preview `docs/reports/*` with `mkdocs serve` and check the browser console for DataTables initialization logs.
- For content changes, skim zh-TW pages to confirm tone stays consistent with the 7-Level stack.

## Commit & Pull Request Guidelines
- Use short, typed commit subjects: `feat:`, `fix:`, `docs:`, `chore:`, or `sync:` followed by an imperative summary (e.g., `feat: add disqus comments`).
- PRs should explain scope and intent, list impacted pages/assets, note new front-matter fields, and include screenshots for visual changes.
- Link related issues and state whether you ran `mkdocs build --strict` or deployed.

## Security & Configuration Tips
- Keep secrets out of the repo; analytics uses `GOOGLE_ANALYTICS_KEY` from the environment. Use placeholders in docs.
- New external JS/CSS should be version-pinned and registered in `mkdocs.yml` under `extra_javascript`/`extra_css`; avoid unpinned CDNs.
