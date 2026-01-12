# Request for Changes: ROA/ROE Report Generator

**Target File:** `stage2-cleaning-roa-roe-report-all.md`
**Goal:** Align the visual style and functionality (sorting/filtering) with the Revenue Report (`stage2-cleaning-revenue-report-all.md`).

To achieve MkDocs compatibility and enable the DataTables features, please update the Python generation script to output the Markdown structure described below.

## 1. Frontmatter (YAML)
Include full metadata at the top of the file.

```yaml
---
authors: [wenchiehlee]
date: 2026-01-12  # Dynamic Date
categories:
  - 股票
  - ROE/ROA
tags:
  - 股票
  - ROE
  - ROA
  - 總覽
title: 📊 ROA/ROE 報告總覽 - 所有股票
comments: false
draft: false
description: ROA/ROE 報告總覽 - 所有股票 - 自動產生
---
```

## 2. Style Injection
Include the CSS block to ensure table font sizing matches other reports.

```html
<style>
.sortable-table, .sortable-table td, .sortable-table th {
    font-size: var(--md-text-size) !important;
}
</style>
```

## 3. Headers & Overview
Use emoji shortcodes or Unicode emojis in headers and include an overview block.

```markdown
# :chart: ROA/ROE 報告總覽 - 所有股票

!!! info "報告概覽"
    **:calendar: 產生時間**: 2026-01-12 12:00:00 CST
    **:building_construction: 處理股票總數**: 126
    **:chart_with_upwards_trend: 報告類型**: 各股盈利能力分析
```

## 4. Summary Cards (Optional but Recommended)
Add a summary grid to highlight key statistics.

```markdown
## :chart_with_upwards_trend: 市場概況

<div class="grid cards" markdown>

- :trophy: **高 ROE 股票 (>15%)**
    ---
    **XX** 檔

- :chart_with_downwards_trend: **負 ROE 股票**
    ---
    **XX** 檔

- :page_with_curl: **總處理股票**
    ---
    **126** 檔

</div>
```

## 5. Stock List Table (CRITICAL)
This is the most important section for sorting and filtering.

### Requirements:
1.  **Wrapper:** The table **MUST** be wrapped in `<div class="annotate" markdown>` to trigger the DataTables JavaScript (`tables.js`).
2.  **Headers:** Use `markdown="span"` on `<th>` tags (if using HTML) or just standard Markdown headers with emojis. Emojis help `tables.js` logic but `tables.js` now specifically detects "ROE" and "ROA" text.
3.  **Link Format:** The link **MUST** be on the **Stock Code** (first column) and follow the pattern `[**Code**](path)`. The bolding `**` is required for the regex parser in `tables.js`.
4.  **Path:** Use `../` prefix and trailing slash `/` for directory URLs.

### Example Markdown Output:

```markdown
## :material-view-list: 股票清單

<div class="annotate" markdown>

| :identification_card: 代號 | :building_construction: 公司 | :factory: 產業 | :chart: ROE | :chart_with_upwards_trend: ROA | :link: 連結 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| [**2330**](../stage2-cleaning-roa-roe-report/stage2-cleaning-roa-roe-report-2330/) | 台積電 | 半導體業 | 25.6% | 18.2% | [報告](../stage2-cleaning-roa-roe-report/stage2-cleaning-roa-roe-report-2330/) |
| [**2317**](../stage2-cleaning-roa-roe-report/stage2-cleaning-roa-roe-report-2317/) | 鴻海 | 其他電子業 | 12.1% | 5.4% | [報告](../stage2-cleaning-roa-roe-report/stage2-cleaning-roa-roe-report-2317/) |

</div>
```

*Note: The last "Link" column is redundant if the first column is linked, but can be kept for compatibility if desired.*

## Summary of Logic Changes
*   **Generate Links:** Change link text from `報告` to `**Code**` and move/duplicate to the first column.
*   **Wrap Table:** Enclose the Markdown table in `<div class="annotate" markdown> ... </div>`.
*   **Add Metadata:** Inject YAML frontmatter.
