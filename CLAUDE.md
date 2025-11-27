# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a MkDocs Material-based documentation site focused on investment analysis and strategy, specifically centered around Taiwan stock market analysis. The site is written primarily in Traditional Chinese (zh-TW) and published via GitHub Pages.

**Site URL**: https://wenchiehlee-investment.github.io
**Primary Language**: Traditional Chinese (zh-TW)

## Core Concept: 7-Level Stock Information Stack

The site documents a comprehensive investment analysis framework with 7 layers:

1. **Level 1 - Fundamentals (基本面)**: EPS, ROE, gross margin, P/E ratio, revenue YoY, valuation positioning
2. **Level 2 - Market Expectation (預期面)**: EPS consensus revisions, analyst ratings, institutional flows
3. **Level 3 - Ownership & Flow (籌碼面)**: Securities lending ratio, margin trading, institutional positioning
4. **Level 4 - Macro & Liquidity (總體與資金風向)**: VIX, JNK, interest rates, economic cycles
5. **Level 5 - Sentiment (市場情緒)**: Social media trends, keyword analysis, crowd sentiment
6. **Level 6 - Technical & Validation (技術驗證)**: EPS surprise, actual vs forecast variance, price-flow divergence
7. **Level 7 - Strategic Layer (策略應用)**: Opportunity cost, risk management, value investing principles

## Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with live reload (default: http://127.0.0.1:8000)
mkdocs serve

# Build static site
mkdocs build
```

### Deployment
The site automatically deploys to GitHub Pages on push to `main` branch via GitHub Actions workflow (`.github/workflows/mkdocs-deploy-gh-pages.yml`).

## Architecture & Key Files

### Configuration
- **`mkdocs.yml`**: Main configuration file with extensive Material theme customization
  - Theme: Material with custom overrides in `docs/overrides/`
  - Language: zh-TW (Traditional Chinese)
  - Features: Blog plugin, Git plugins (committers, revision dates), RSS, tags
  - Analytics: Google Analytics (configured via `GOOGLE_ANALYTICS_KEY` secret)

### Content Structure
```
docs/
├── blog/                    # Blog posts with investment analysis
│   ├── .authors.yml        # Author metadata (wenchiehlee, andylee-me, kohsin520)
│   ├── index.md            # Blog index
│   └── posts/              # Blog post markdown files
├── about/                   # About pages and friend links
├── assets/                  # Images and static assets
├── javascripts/            # Custom JavaScript (mathjax.js)
├── stylesheets/            # Custom CSS (timeline, cards, extra styling)
├── overrides/              # Material theme overrides
│   ├── partials/
│   │   └── comments.html   # Giscus comments integration
│   └── main.html           # Main template override
├── index.md                # Homepage with Investment Stack Vision diagram
└── tag.md                  # Tags index page
```

### Custom Features
- **Giscus Comments**: Integrated via `docs/overrides/partials/comments.html` for blog posts
- **PlantUML Diagrams**: Investment Stack Vision diagram rendered from `InvestmentStackVision.planuml`
- **React Components**: Custom React components for future bidding analysis (loaded via `react-loader.js`)
- **LaTeX Support**: MathJax integration for mathematical formulas

### Blog Post Format
Blog posts use YAML frontmatter with:
```yaml
---
authors: [wenchiehlee]
date: YYYY-MM-DD
categories:
  - 投資
tags:
  - 股票
title: Post Title
comments: true
draft: false
description: Post description
---
```

### MkDocs Plugins & Extensions

**Key Plugins**:
- `blog`: Blog functionality with archives, pagination, author profiles
- `git-committers`: Show contributors (requires GitHub token in CI)
- `git-revision-date-localized`: Display last update times
- `rss`: Generate RSS feed for blog posts
- `tags`: Tag system for content organization
- `search`: Enhanced search with Chinese character support

**Important Markdown Extensions**:
- `pymdownx.arithmatex`: LaTeX math support
- `pymdownx.superfences`: Code blocks with Mermaid diagram support
- `pymdownx.tabbed`: Tabbed content blocks
- `neoteroi.cards` & `neoteroi.timeline`: Card and timeline layouts

## Repository Sync Workflow

This repository syncs configuration files with other related repositories using GitHub Actions workflows:
- `.github/workflows/sync-up-配置檔案.yml`: Syncs `.gitignore` and workflow files
- `.github/workflows/sync-up-名單清單.yml`: Syncs CSV watchlists and stock lists

Related repositories include:
- `wenchiehlee/Python-Actions.GoodInfo.Analyzer`
- `wenchiehlee/Selenium-Actions.IPO`
- `wenchiehlee/Selenium-Actions.Auction`
- And others (see `.github/sync-配置檔案.yml`)

## Content Guidelines

### Language & Style
- All content should be in Traditional Chinese (zh-TW)
- Blog posts focus on Taiwan stock market analysis
- Investment philosophy influenced by Howard Marks and value investing principles
- Posts include data sources like FactSet, GoodInfo, MOPS, TWSE

### Adding Blog Posts
1. Create new markdown file in `docs/blog/posts/` with date prefix: `YYYY-MM-DD-title.md`
2. Include proper frontmatter (authors, date, categories, tags)
3. Set `comments: true` to enable Giscus comments
4. Use `draft: true` for work-in-progress posts

### Customization Areas
- **Theme colors**: Defined in `mkdocs.yml` under `theme.palette`
- **Navigation**: Configured in `nav:` section of `mkdocs.yml`
- **Custom CSS**: Add to `docs/stylesheets/extra.css`
- **Custom JavaScript**: Add to `docs/javascripts/` and reference in `extra_javascript`

## Auto-Generated Reports Organization

**Important**: The revenue and dividend reports are auto-generated from another repository and should NOT be manually edited in this repo.

### Navigation Structure
The reports are organized in a 2-level hierarchy in `mkdocs.yml`:

**Level 1** (shown in top navigation and left sidebar):
- 營收報告總覽 (`stage2-cleaning-revenue-report-all.md`)
- 股利分配總覽 (`stage2-cleaning-dividends-report-all.md`)

**Level 2** (individual stock reports - ~117 files):
- Individual stock reports (e.g., `stage2-cleaning-revenue-report-2357.md`) are NOT listed in the main navigation to avoid clutter
- Users access individual reports through links within the "all" summary pages
- These appear in the right sidebar TOC when viewing the summary pages

### TOC Configuration
The TOC is configured with `toc_depth: 3` to support 3-level heading hierarchy.

**For the auto-generation script in the other repository**, the markdown files should be structured as follows:

#### Current Structure (Flat - No Hierarchy):
```markdown
## Dividend Distribution Summary Report - All Stocks
## 華碩 (2357) 月營收報告
## 廣達 (2382) 月營收報告
## 完整營收報告總覽 - 所有股票
```

#### Required Structure (2-Level Hierarchy):
```markdown
## 📊 總覽報告 (Summary Reports)

### Dividend Distribution Summary Report - All Stocks
[Link or content]

### 完整營收報告總覽 - 所有股票
[Link or content]

## 📈 個股詳細報告 (Individual Stock Reports)

### 華碩 (2357) 月營收報告
[Link to individual report]

### 廣達 (2382) 月營收報告
[Link to individual report]

### 中華電 (2412) 月營收報告
[Link to individual report]
```

This structure will create a collapsible 2-level hierarchy in the right sidebar TOC where:
- Level 1 (`##`): Section headers (總覽報告, 個股詳細報告)
- Level 2 (`###`): Individual report links nested under sections

## Important Notes

- The site uses Traditional Chinese font: Noto Serif TC
- Comments system uses Giscus with repo: `wenchiehlee/mkdocs-investment`
- Custom domain configured: Uses GitHub Pages with custom setup
- Blog posts are auto-archived by year/month
- Draft posts with future dates are automatically marked as drafts
- Reading time is calculated at 200 words/minute for Chinese content
- **Auto-generated report files should never be manually edited** - they sync from another repository
