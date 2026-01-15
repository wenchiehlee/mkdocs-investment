# Request for Changes: Interactive Chart Support

**Goal:** Replace static SVG charts with interactive JSON-based charts (ApexCharts) in Margin Daily Reports to enable zooming (1M, 3M, 1Y, etc.).

## 1. Output Data Format
Modify the analyzer to generate a JSON file for each stock alongside (or instead of) the SVG.

*   **File Name:** `margin_daily-{stock_id}.json`
*   **Format:** A JSON array of arrays, where each inner array is `[timestamp_ms, value]`.
    *   `timestamp_ms`: Unix timestamp in milliseconds (integer).
    *   `value`: The numeric value (float/int).

**Example (`margin_daily-2330.json`):**
```json
[
  [1672531200000, 542.0],
  [1672617600000, 545.5],
  [1672704000000, 538.0]
]
```

## 2. Update Markdown Template
Modify the logic that generates the `stage2-cleaning-margin_daily-report-*.md` files.

*   **Old:**
    ```markdown
    ![Margin Chart](margin_daily-2330.svg)
    ```

*   **New:**
    Replace the image syntax with a placeholder `<div>` that the `charts.js` script will target. Use `../` prefix for the data URL if the report is in a subdirectory (which it is: `stage2-cleaning-margin_daily-report/`).

    ```html
    <div class="margin-chart" data-url="../margin_daily-{stock_id}.json" data-title="融資餘額"></div>
    ```

    *   `class="margin-chart"`: Required for the script to find the element.
    *   `data-url`: Relative path to the generated JSON file.
    *   `data-title`: Title to display on the chart.

## Summary
1.  **Serialize:** Dump time-series data to JSON.
2.  **Embed:** Output HTML `div` with `data-url` attribute instead of Markdown image.
