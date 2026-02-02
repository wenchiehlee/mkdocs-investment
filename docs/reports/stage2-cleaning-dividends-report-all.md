---
authors: [wenchiehlee]
date: 2026-02-02
categories:
  - 股票
  - 股利分配
tags:
  - 股票
  - 股利
  - 殖利率
  - 總覽
title: 股利分配總覽 - 所有股票
comments: false
draft: false
description: 股利分配總覽 - 所有 126 檔股票 (有效 103 檔) - 自動產生
---

<style>
.sortable-table, .sortable-table td, .sortable-table th {
    font-size: var(--md-text-size) !important;
}
</style>

# :bar_chart: 股利分配總覽 - 所有股票

!!! info "報告概覽"
    **:calendar: 產生時間**: 2026-02-02 19:25:00 CST  
    **:building_construction: 分析股票總數**: 126 檔 (有效 103 檔)  
    **:chart_with_upwards_trend: 報告類型**: 完整股利分配分析  
    **:file_folder: 資料來源**: Stage 2 cleaned_dividends.csv + cleaned_performance1.csv

---

## :globe_with_meridians: 投資組合股利總覽

| :chart: 指標 | :bar_chart: 平均值 | :1234: 中位數 | :trophy: 最佳股票 | :warning: 最弱股票 |
|:--------:|:-------------:|:--------:|:-----------:|:------------:|
| **現金殖利率 (5年平均)** | 3.82% | 3.61% | [**2603**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2603/): 17.98% | [**2646**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2646/): 0.00% |
| **穩定性評分** | 6.1/10 | 6.5/10 | [**3665**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3665/): 8.5/10 | [**2405**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2405/): 0.0/10 |

---

## :material-view-list: 股票清單

!!! tip "如何閱讀此表格"
    點擊表格中的股票代號可查看該股票的詳細股利分配報告。表格顯示每檔股票的最新股利資訊、殖利率區間與歷史資料範圍。
    💡 **提示**: 此表格支援排序與篩選功能，可依任何欄位排序查看資料。

!!! info "穩定性評級說明"
    - 🟢 **優質** (≥8.0): 股利發放非常穩定，波動低，可持續性高
    - 🟡 **良好** (6.0-7.9): 股利發放穩定，適合長期投資
    - 🔴 **警示** (<6.0): 股利波動較大或可持續性存在風險

!!! warning "價格資料時效性"
    表格中的「當日價時間」欄位顯示股價資料的下載時間。由於資料來源更新頻率限制，價格資料可能有數小時至一天的延遲。
    建議搭配即時報價系統確認最新股價，以獲得更準確的殖利率估算。

!!! tip "股利預測說明"
    **預測方法**: 預測股利 = TTM EPS (近4季) × 平均配息率(5年) × 平均現金比例(5年)
    **欄位說明**: 預測股利為 TTM + FactSet 動態整合結果；TTM預測股利為純 TTM 估算；Factset預測股利為 FactSet 時間加權估算

    **圖示說明**:

    - 🔼 **預測成長**: 預測股利 > 最新現金股利
    - 🔽 **預測衰退**: 預測股利 < 最新現金股利
    **重要**: 預測僅供參考，不構成投資建議。實際股利以公司公告為準。

!!! info "名詞定義"
    - **殖利率@當日價**: 預估配息 ÷ 當日股價
    - **現金殖利率**: 現金股利 ÷ 年均價
    - **總殖利率**: 以現金殖利率 ×（總股利/現金股利）估算
    - **殖利率@當年度最高/最低價**: 以年度最高價/最低價計算
    - **配息率**: 每股股利 ÷ 每股盈餘（EPS，股利年度對應前一年度EPS）

<table class="sortable-table">
<thead>
<tr>
<th>:identification_card: 股票代號</th>
<th>:building_construction: 公司名稱</th>
<th>:moneybag: 現金股利(元)</th>
<th>:crystal_ball: 預測股利(元)</th>
<th>:crystal_ball: TTM預測股利(元)</th>
<th>:crystal_ball: Factset預測股利(元)</th>
<th>:chart: 殖利率@當日價</th>
<th>:clock3: 當日價時間</th>
<th>:arrow_down: 殖利率@當年度最低價</th>
<th>:arrow_up: 殖利率@當年度最高價</th>
<th>:repeat: 配息率</th>
<th>:traffic_light: 穩定性</th>
</tr>
</thead>
<tbody>
<tr>
<td>[**2301**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2301/)</td>
<td>光寶科</td>
<td>4.51</td>
<td>🔼 5.38</td>
<td>🔼 5.40</td>
<td>🔼 5.53</td>
<td>2.76%</td>
<td>02/01 14:35</td>
<td>6.39%</td>
<td>2.29%</td>
<td>87%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2303**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2303/)</td>
<td>聯電</td>
<td>2.85</td>
<td>🔽 2.13</td>
<td>🔽 2.04</td>
<td>🔽 2.13</td>
<td>5.79%</td>
<td>02/01 14:42</td>
<td>7.22%</td>
<td>5.58%</td>
<td>75%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2308**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2308/)</td>
<td>台達電</td>
<td>7.00</td>
<td>🔼 12.33</td>
<td>🔼 11.12</td>
<td>🔼 12.33</td>
<td>0.73%</td>
<td>02/01 14:16</td>
<td>2.55%</td>
<td>0.65%</td>
<td>52%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2317**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2317/)</td>
<td>鴻海</td>
<td>5.80</td>
<td>🔼 7.39</td>
<td>🔼 7.22</td>
<td>🔼 7.39</td>
<td>2.52%</td>
<td>02/01 14:16</td>
<td>5.16%</td>
<td>2.19%</td>
<td>53%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**2324**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2324/)</td>
<td>仁寶</td>
<td>1.40</td>
<td>🔽 0.98</td>
<td>🔽 1.03</td>
<td>🔼 1.90</td>
<td>4.61%</td>
<td>02/01 14:17</td>
<td>5.91%</td>
<td>3.52%</td>
<td>61%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2330**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2330/)</td>
<td>台積電</td>
<td>6.00</td>
<td>🔼 20.77</td>
<td>🔼 21.83</td>
<td>🔼 25.96</td>
<td>1.35%</td>
<td>02/01 14:17</td>
<td>1.55%</td>
<td>1.31%</td>
<td>13%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2332**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2332/)</td>
<td>友訊</td>
<td>0.10</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.66%</td>
<td>02/01 14:57</td>
<td>0.71%</td>
<td>0.39%</td>
<td>167%</td>
<td>🔴 4.5</td>
</tr>
<tr>
<td>[**2345**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2345/)</td>
<td>智邦</td>
<td>11.00</td>
<td>🔼 23.50</td>
<td>🔼 24.78</td>
<td>-</td>
<td>0.93%</td>
<td>02/01 15:12</td>
<td>2.56%</td>
<td>0.89%</td>
<td>51%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2347**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2347/)</td>
<td>聯強</td>
<td>4.00</td>
<td>🔽 2.78</td>
<td>🔽 3.05</td>
<td>-</td>
<td>6.91%</td>
<td>02/01 14:18</td>
<td>7.33%</td>
<td>5.25%</td>
<td>72%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**2353**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2353/)</td>
<td>宏碁</td>
<td>1.70</td>
<td>🔽 1.04</td>
<td>🔽 1.15</td>
<td>-</td>
<td>6.44%</td>
<td>02/01 14:44</td>
<td>6.80%</td>
<td>4.15%</td>
<td>92%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2354**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2354/)</td>
<td>鴻準</td>
<td>1.40</td>
<td>🔽 1.17</td>
<td>🔽 1.23</td>
<td>-</td>
<td>2.27%</td>
<td>02/01 14:18</td>
<td>2.99%</td>
<td>1.75%</td>
<td>55%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2356**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2356/)</td>
<td>英業達</td>
<td>1.70</td>
<td>🔼 1.96</td>
<td>🔼 2.12</td>
<td>🔼 2.03</td>
<td>3.96%</td>
<td>02/01 14:19</td>
<td>5.11%</td>
<td>3.17%</td>
<td>84%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2357**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2357/)</td>
<td>華碩</td>
<td>34.00</td>
<td>🔼 39.94</td>
<td>🔼 35.44</td>
<td>🔼 40.62</td>
<td>6.20%</td>
<td>02/01 14:19</td>
<td>7.71%</td>
<td>4.56%</td>
<td>80%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2359**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2359/)</td>
<td>所羅門</td>
<td>0.00</td>
<td>🔽 -0.12</td>
<td>🔼 0.56</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:58</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**2360**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2360/)</td>
<td>致茂</td>
<td>9.00</td>
<td>🔼 17.50</td>
<td>🔼 18.04</td>
<td>-</td>
<td>1.16%</td>
<td>02/01 15:16</td>
<td>4.08%</td>
<td>1.04%</td>
<td>72%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2376**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2376/)</td>
<td>技嘉</td>
<td>10.00</td>
<td>🔼 12.12</td>
<td>🔼 12.40</td>
<td>🔼 13.84</td>
<td>4.01%</td>
<td>02/01 14:20</td>
<td>5.56%</td>
<td>3.15%</td>
<td>66%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2377**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2377/)</td>
<td>微星</td>
<td>5.00</td>
<td>🔽 3.58</td>
<td>🔽 3.21</td>
<td>-</td>
<td>5.20%</td>
<td>02/01 14:20</td>
<td>5.30%</td>
<td>2.38%</td>
<td>62%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2379**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2379/)</td>
<td>瑞昱</td>
<td>25.50</td>
<td>🔽 25.20</td>
<td>🔽 25.43</td>
<td>-</td>
<td>5.21%</td>
<td>02/01 14:20</td>
<td>5.90%</td>
<td>4.30%</td>
<td>86%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2382**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2382/)</td>
<td>廣達</td>
<td>13.00</td>
<td>🔼 14.77</td>
<td>🔼 14.46</td>
<td>🔼 14.77</td>
<td>4.78%</td>
<td>02/01 14:21</td>
<td>7.47%</td>
<td>4.14%</td>
<td>84%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2383**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2383/)</td>
<td>台光電</td>
<td>16.58</td>
<td>🔼 22.54</td>
<td>🔼 23.17</td>
<td>-</td>
<td>1.01%</td>
<td>02/01 15:03</td>
<td>4.07%</td>
<td>0.98%</td>
<td>60%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2395**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2395/)</td>
<td>研華</td>
<td>8.39</td>
<td>🔼 8.59</td>
<td>🔼 8.85</td>
<td>🔼 8.72</td>
<td>2.91%</td>
<td>02/01 14:21</td>
<td>3.10%</td>
<td>1.97%</td>
<td>80%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2405**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2405/)</td>
<td>輔信</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:22</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 0.0</td>
</tr>
<tr>
<td>[**2408**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2408/)</td>
<td>南亞科</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 15:16</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 3.0</td>
</tr>
<tr>
<td>[**2412**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2412/)</td>
<td>中華電</td>
<td>5.00</td>
<td>🔽 4.97</td>
<td>🔽 4.99</td>
<td>-</td>
<td>3.83%</td>
<td>02/01 14:22</td>
<td>4.10%</td>
<td>3.62%</td>
<td>104%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2449**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2449/)</td>
<td>京元電子</td>
<td>4.00</td>
<td>🔼 5.75</td>
<td>🔼 5.84</td>
<td>-</td>
<td>1.62%</td>
<td>02/01 15:12</td>
<td>5.71%</td>
<td>1.53%</td>
<td>63%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2450**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2450/)</td>
<td>神腦</td>
<td>1.65</td>
<td>🔽 1.26</td>
<td>🔽 1.36</td>
<td>-</td>
<td>5.70%</td>
<td>02/01 14:41</td>
<td>5.84%</td>
<td>4.76%</td>
<td>89%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2451**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2451/)</td>
<td>創見</td>
<td>6.09</td>
<td>🔼 6.60</td>
<td>🔼 6.77</td>
<td>-</td>
<td>3.11%</td>
<td>02/01 14:23</td>
<td>7.76%</td>
<td>2.82%</td>
<td>113%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2454**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2454/)</td>
<td>聯發科</td>
<td>29.00</td>
<td>🔼 60.54</td>
<td>🔼 60.77</td>
<td>🔼 52.09</td>
<td>3.30%</td>
<td>02/01 14:23</td>
<td>4.10%</td>
<td>3.19%</td>
<td>56%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2458**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2458/)</td>
<td>義隆</td>
<td>6.41</td>
<td>🔽 6.26</td>
<td>🔽 6.28</td>
<td>🔽 6.01</td>
<td>5.41%</td>
<td>02/01 14:24</td>
<td>6.38%</td>
<td>3.84%</td>
<td>67%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2474**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2474/)</td>
<td>可成</td>
<td>11.49</td>
<td>🔽 8.10</td>
<td>🔽 10.02</td>
<td>-</td>
<td>5.52%</td>
<td>02/01 14:24</td>
<td>6.53%</td>
<td>5.03%</td>
<td>59%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2480**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2480/)</td>
<td>敦陽科</td>
<td>7.42</td>
<td>🔽 7.25</td>
<td>🔽 7.36</td>
<td>-</td>
<td>4.92%</td>
<td>02/01 14:24</td>
<td>6.32%</td>
<td>4.01%</td>
<td>99%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2603**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2603/)</td>
<td>長榮</td>
<td>32.50</td>
<td>🔽 20.19</td>
<td>🔽 23.72</td>
<td>🔽 18.01</td>
<td>17.10%</td>
<td>02/01 15:00</td>
<td>19.00%</td>
<td>12.30%</td>
<td>50%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2646**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2646/)</td>
<td>星宇航空</td>
<td>0.00</td>
<td>🟠 0.00</td>
<td>⚪ 0.00</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:39</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🔴 0.5</td>
</tr>
<tr>
<td>[**2881**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2881/)</td>
<td>富邦金</td>
<td>4.25</td>
<td>🔽 2.86</td>
<td>🔽 3.31</td>
<td>-</td>
<td>4.42%</td>
<td>02/01 15:14</td>
<td>5.89%</td>
<td>4.30%</td>
<td>42%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2882**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2882/)</td>
<td>國泰金</td>
<td>3.50</td>
<td>🔽 2.33</td>
<td>🔽 2.40</td>
<td>🔽 2.92</td>
<td>4.62%</td>
<td>02/01 15:14</td>
<td>7.07%</td>
<td>4.53%</td>
<td>48%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**2884**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2884/)</td>
<td>玉山金</td>
<td>1.20</td>
<td>🔽 0.96</td>
<td>🔽 0.96</td>
<td>-</td>
<td>3.56%</td>
<td>02/01 15:15</td>
<td>4.71%</td>
<td>3.39%</td>
<td>79%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2891**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2891/)</td>
<td>中信金</td>
<td>2.30</td>
<td>🔽 2.05</td>
<td>🔽 2.16</td>
<td>-</td>
<td>4.58%</td>
<td>02/01 15:14</td>
<td>6.84%</td>
<td>4.52%</td>
<td>63%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**3014**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3014/)</td>
<td>聯陽</td>
<td>9.00</td>
<td>🔽 8.32</td>
<td>🔽 8.38</td>
<td>-</td>
<td>7.83%</td>
<td>02/01 14:47</td>
<td>8.37%</td>
<td>5.49%</td>
<td>89%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**3022**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3022/)</td>
<td>威強電</td>
<td>4.50</td>
<td>🔽 1.13</td>
<td>🔽 2.56</td>
<td>-</td>
<td>6.98%</td>
<td>02/01 14:25</td>
<td>7.26%</td>
<td>3.69%</td>
<td>52%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**3026**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3026/)</td>
<td>禾伸堂</td>
<td>5.50</td>
<td>🔽 5.16</td>
<td>🔽 5.18</td>
<td>-</td>
<td>5.39%</td>
<td>02/01 14:25</td>
<td>7.67%</td>
<td>4.35%</td>
<td>94%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**3029**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3029/)</td>
<td>零壹</td>
<td>5.00</td>
<td>🔼 5.45</td>
<td>🔼 5.59</td>
<td>-</td>
<td>4.42%</td>
<td>02/01 14:54</td>
<td>5.29%</td>
<td>3.05%</td>
<td>95%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3034**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3034/)</td>
<td>聯詠</td>
<td>28.00</td>
<td>🔽 23.16</td>
<td>🔽 23.45</td>
<td>🔽 25.37</td>
<td>7.49%</td>
<td>02/01 14:26</td>
<td>7.63%</td>
<td>4.96%</td>
<td>84%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3035**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3035/)</td>
<td>智原</td>
<td>3.00</td>
<td>🔽 1.91</td>
<td>🔽 2.08</td>
<td>🔽 1.92</td>
<td>1.76%</td>
<td>02/01 14:35</td>
<td>2.01%</td>
<td>1.14%</td>
<td>74%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**3045**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3045/)</td>
<td>台灣大</td>
<td>4.50</td>
<td>🔼 4.78</td>
<td>🔼 4.86</td>
<td>-</td>
<td>4.15%</td>
<td>02/01 14:26</td>
<td>4.33%</td>
<td>3.73%</td>
<td>98%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3048**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3048/)</td>
<td>益登</td>
<td>0.00</td>
<td>🔼 0.99</td>
<td>🔼 0.82</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:27</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**3150**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3150/)</td>
<td>鈺寶-創</td>
<td>1.00</td>
<td>🔽 0.25</td>
<td>🔽 0.15</td>
<td>-</td>
<td>5.08%</td>
<td>02/01 14:39</td>
<td>5.87%</td>
<td>2.54%</td>
<td>139%</td>
<td>🔴 3.5</td>
</tr>
<tr>
<td>[**3158**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3158/)</td>
<td>嘉實</td>
<td>6.00</td>
<td>🔽 5.00</td>
<td>🔽 4.98</td>
<td>-</td>
<td>6.47%</td>
<td>02/01 14:44</td>
<td>6.67%</td>
<td>5.80%</td>
<td>82%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**3231**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3231/)</td>
<td>緯創</td>
<td>3.80</td>
<td>🔼 5.57</td>
<td>🔼 5.29</td>
<td>🔼 5.57</td>
<td>2.52%</td>
<td>02/01 14:27</td>
<td>5.15%</td>
<td>2.40%</td>
<td>62%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**3260**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3260/)</td>
<td>威剛</td>
<td>0.00</td>
<td>🔼 5.20</td>
<td>🔼 5.16</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 15:07</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3293**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3293/)</td>
<td>鈊象</td>
<td>0.00</td>
<td>🔼 22.83</td>
<td>🔼 22.34</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:59</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3356**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3356/)</td>
<td>奇偶</td>
<td>4.00</td>
<td>🔽 2.22</td>
<td>🔽 3.95</td>
<td>-</td>
<td>8.51%</td>
<td>02/01 14:28</td>
<td>10.10%</td>
<td>5.94%</td>
<td>57%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**3558**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3558/)</td>
<td>神準</td>
<td>3.00</td>
<td>🔽 2.64</td>
<td>🔽 2.67</td>
<td>-</td>
<td>2.30%</td>
<td>02/01 14:41</td>
<td>2.37%</td>
<td>1.15%</td>
<td>62%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**3653**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3653/)</td>
<td>健策</td>
<td>14.50</td>
<td>🔼 20.62</td>
<td>🔼 21.52</td>
<td>-</td>
<td>0.53%</td>
<td>02/01 15:17</td>
<td>1.92%</td>
<td>0.46%</td>
<td>60%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3661**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3661/)</td>
<td>世芯-KY</td>
<td>36.48</td>
<td>🔽 33.06</td>
<td>🔼 36.55</td>
<td>-</td>
<td>1.04%</td>
<td>02/01 15:13</td>
<td>1.88%</td>
<td>0.82%</td>
<td>45%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**3665**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3665/)</td>
<td>貿聯-KY</td>
<td>10.51</td>
<td>🔼 20.47</td>
<td>🔼 21.61</td>
<td>-</td>
<td>0.69%</td>
<td>02/01 15:17</td>
<td>2.80%</td>
<td>0.60%</td>
<td>41%</td>
<td>🟢 8.5</td>
</tr>
<tr>
<td>[**3711**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3711/)</td>
<td>日月光投控</td>
<td>5.30</td>
<td>🔼 5.46</td>
<td>🔽 5.11</td>
<td>🔼 7.58</td>
<td>2.11%</td>
<td>02/01 15:15</td>
<td>4.61%</td>
<td>2.08%</td>
<td>70%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**4114**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4114/)</td>
<td>健喬</td>
<td>0.60</td>
<td>🔽 0.50</td>
<td>🔽 0.50</td>
<td>-</td>
<td>1.85%</td>
<td>02/01 15:07</td>
<td>2.07%</td>
<td>1.51%</td>
<td>92%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**4749**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4749/)</td>
<td>新應材</td>
<td>5.99</td>
<td>🔼 7.42</td>
<td>🔼 7.51</td>
<td>-</td>
<td>0.68%</td>
<td>02/01 14:51</td>
<td>1.63%</td>
<td>0.63%</td>
<td>70%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**4938**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4938/)</td>
<td>和碩</td>
<td>4.50</td>
<td>🔽 2.90</td>
<td>🔽 3.21</td>
<td>🔼 5.88</td>
<td>6.56%</td>
<td>02/01 14:28</td>
<td>6.67%</td>
<td>4.55%</td>
<td>71%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**4953**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4953/)</td>
<td>緯軟</td>
<td>3.99</td>
<td>🔼 4.61</td>
<td>🔼 4.23</td>
<td>-</td>
<td>3.24%</td>
<td>02/01 14:40</td>
<td>5.18%</td>
<td>2.93%</td>
<td>64%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**5203**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5203/)</td>
<td>訊連</td>
<td>3.90</td>
<td>🔽 1.84</td>
<td>🔽 3.64</td>
<td>-</td>
<td>4.37%</td>
<td>02/01 14:29</td>
<td>4.58%</td>
<td>2.69%</td>
<td>98%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**5269**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5269/)</td>
<td>祥碩</td>
<td>30.00</td>
<td>🔼 35.56</td>
<td>🔼 36.54</td>
<td>-</td>
<td>2.48%</td>
<td>02/01 14:36</td>
<td>2.65%</td>
<td>1.32%</td>
<td>58%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**5274**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5274/)</td>
<td>信驊</td>
<td>52.00</td>
<td>🔼 71.64</td>
<td>🔼 79.78</td>
<td>🔼 77.66</td>
<td>0.72%</td>
<td>02/01 15:00</td>
<td>2.29%</td>
<td>0.67%</td>
<td>76%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**5434**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5434/)</td>
<td>崇越</td>
<td>11.99</td>
<td>🔼 12.79</td>
<td>🔼 13.28</td>
<td>-</td>
<td>4.12%</td>
<td>02/01 14:34</td>
<td>5.83%</td>
<td>3.38%</td>
<td>62%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**5536**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5536/)</td>
<td>聖暉</td>
<td>5.50</td>
<td>🔼 15.37</td>
<td>🔼 15.83</td>
<td>-</td>
<td>1.75%</td>
<td>02/01 14:57</td>
<td>1.75%</td>
<td>1.30%</td>
<td>27%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**5904**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5904/)</td>
<td>寶雅</td>
<td>23.00</td>
<td>🔼 23.24</td>
<td>🔼 24.18</td>
<td>-</td>
<td>5.23%</td>
<td>02/01 14:45</td>
<td>5.36%</td>
<td>4.32%</td>
<td>86%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6035**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6035/)</td>
<td>悠遊卡</td>
<td>2.95</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>4.96%</td>
<td>02/01 14:44</td>
<td>5.18%</td>
<td>3.98%</td>
<td>-</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**6123**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6123/)</td>
<td>上奇</td>
<td>0.00</td>
<td>🔼 2.21</td>
<td>🔼 2.28</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:52</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**6125**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6125/)</td>
<td>廣運</td>
<td>0.70</td>
<td>🔽 0.21</td>
<td>🔽 0.09</td>
<td>-</td>
<td>0.97%</td>
<td>02/01 14:58</td>
<td>1.40%</td>
<td>0.67%</td>
<td>-</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6182**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6182/)</td>
<td>合晶</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:46</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 3.5</td>
</tr>
<tr>
<td>[**6214**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6214/)</td>
<td>精誠</td>
<td>5.20</td>
<td>🔼 5.78</td>
<td>🔼 6.12</td>
<td>-</td>
<td>4.41%</td>
<td>02/01 14:29</td>
<td>5.28%</td>
<td>3.44%</td>
<td>67%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6231**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6231/)</td>
<td>系微</td>
<td>6.50</td>
<td>🔽 4.83</td>
<td>🔽 5.19</td>
<td>-</td>
<td>3.04%</td>
<td>02/01 14:40</td>
<td>3.39%</td>
<td>1.44%</td>
<td>81%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6285**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6285/)</td>
<td>啟碁</td>
<td>4.80</td>
<td>🔽 3.87</td>
<td>🔽 4.23</td>
<td>-</td>
<td>4.85%</td>
<td>02/01 14:30</td>
<td>5.00%</td>
<td>2.94%</td>
<td>66%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**6425**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6425/)</td>
<td>易發</td>
<td>1.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1.18%</td>
<td>02/01 14:53</td>
<td>2.67%</td>
<td>1.05%</td>
<td>145%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6442**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6442/)</td>
<td>光聖</td>
<td>8.62</td>
<td>🔼 10.51</td>
<td>🔼 13.01</td>
<td>-</td>
<td>0.63%</td>
<td>02/01 14:56</td>
<td>2.94%</td>
<td>0.60%</td>
<td>60%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**6462**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6462/)</td>
<td>神盾</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:31</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 2.0</td>
</tr>
<tr>
<td>[**6506**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6506/)</td>
<td>雙邦</td>
<td>0.80</td>
<td>🔽 0.71</td>
<td>⚪ 0.80</td>
<td>-</td>
<td>5.21%</td>
<td>02/01 14:59</td>
<td>6.30%</td>
<td>4.53%</td>
<td>108%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6510**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6510/)</td>
<td>精測</td>
<td>7.80</td>
<td>🔼 13.84</td>
<td>🔼 15.32</td>
<td>-</td>
<td>0.34%</td>
<td>02/01 15:13</td>
<td>1.60%</td>
<td>0.31%</td>
<td>50%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**6526**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6526/)</td>
<td>達發</td>
<td>12.50</td>
<td>🔽 10.64</td>
<td>🔽 10.43</td>
<td>-</td>
<td>2.82%</td>
<td>02/01 14:34</td>
<td>2.96%</td>
<td>1.75%</td>
<td>78%</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**6561**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6561/)</td>
<td>是方</td>
<td>19.10</td>
<td>🔽 14.96</td>
<td>🔽 15.62</td>
<td>🔽 9.70</td>
<td>5.09%</td>
<td>02/01 14:38</td>
<td>5.63%</td>
<td>4.00%</td>
<td>138%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**6597**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6597/)</td>
<td>立誠</td>
<td>2.63</td>
<td>🔽 0.92</td>
<td>🔽 1.34</td>
<td>-</td>
<td>4.42%</td>
<td>02/01 15:08</td>
<td>5.16%</td>
<td>2.93%</td>
<td>57%</td>
<td>🔴 3.5</td>
</tr>
<tr>
<td>[**6613**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6613/)</td>
<td>朋億</td>
<td>3.00</td>
<td>🔼 8.43</td>
<td>🔼 9.51</td>
<td>-</td>
<td>3.11%</td>
<td>02/01 14:43</td>
<td>3.18%</td>
<td>2.76%</td>
<td>30%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**6669**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6669/)</td>
<td>緯穎</td>
<td>74.00</td>
<td>🔼 136.80</td>
<td>🔼 142.23</td>
<td>🔼 136.95</td>
<td>1.65%</td>
<td>02/01 14:36</td>
<td>5.05%</td>
<td>1.55%</td>
<td>58%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**6690**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6690/)</td>
<td>安碁資訊</td>
<td>6.00</td>
<td>🔽 5.61</td>
<td>🔼 6.08</td>
<td>-</td>
<td>3.45%</td>
<td>02/01 14:54</td>
<td>4.18%</td>
<td>2.75%</td>
<td>59%</td>
<td>🟢 8.5</td>
</tr>
<tr>
<td>[**6695**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6695/)</td>
<td>芯鼎</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 14:37</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 0.5</td>
</tr>
<tr>
<td>[**6720**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6720/)</td>
<td>久昌</td>
<td>3.80</td>
<td>🔽 1.80</td>
<td>🔽 2.28</td>
<td>-</td>
<td>3.07%</td>
<td>02/01 14:48</td>
<td>3.23%</td>
<td>1.99%</td>
<td>84%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6751**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6751/)</td>
<td>智聯服務</td>
<td>1.00</td>
<td>🔼 4.92</td>
<td>🔼 4.75</td>
<td>-</td>
<td>1.82%</td>
<td>02/01 14:55</td>
<td>2.54%</td>
<td>1.47%</td>
<td>120%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**6757**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6757/)</td>
<td>台灣虎航</td>
<td>6.05</td>
<td>🔽 2.20</td>
<td>🔽 2.42</td>
<td>-</td>
<td>9.38%</td>
<td>02/01 14:48</td>
<td>9.41%</td>
<td>5.55%</td>
<td>98%</td>
<td>🔴 2.5</td>
</tr>
<tr>
<td>[**6763**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6763/)</td>
<td>綠界科技</td>
<td>0.95</td>
<td>🔼 2.83</td>
<td>🔼 2.03</td>
<td>-</td>
<td>3.58%</td>
<td>02/01 14:55</td>
<td>3.61%</td>
<td>3.24%</td>
<td>25%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6811**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6811/)</td>
<td>宏碁資訊</td>
<td>9.50</td>
<td>🔽 8.93</td>
<td>🔽 8.74</td>
<td>-</td>
<td>4.49%</td>
<td>02/01 14:53</td>
<td>5.43%</td>
<td>3.06%</td>
<td>73%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**6850**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6850/)</td>
<td>光鼎生技</td>
<td>0.30</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.75%</td>
<td>02/01 15:10</td>
<td>0.79%</td>
<td>0.57%</td>
<td>-</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6902**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6902/)</td>
<td>GOGOLOOK</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>02/01 15:10</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 0.5</td>
</tr>
<tr>
<td>[**6918**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6918/)</td>
<td>愛派司</td>
<td>4.00</td>
<td>🔽 3.09</td>
<td>🔽 3.44</td>
<td>-</td>
<td>4.68%</td>
<td>02/01 15:10</td>
<td>4.80%</td>
<td>2.94%</td>
<td>80%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6925**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6925/)</td>
<td>意藍</td>
<td>2.00</td>
<td>🔽 1.94</td>
<td>🔽 1.77</td>
<td>-</td>
<td>2.27%</td>
<td>02/01 15:11</td>
<td>3.33%</td>
<td>1.04%</td>
<td>73%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**7547**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7547/)</td>
<td>碩網</td>
<td>1.35</td>
<td>🔼 1.86</td>
<td>🔼 1.90</td>
<td>-</td>
<td>2.36%</td>
<td>02/01 15:01</td>
<td>2.37%</td>
<td>0.88%</td>
<td>67%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**7712**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7712/)</td>
<td>博盛半導體</td>
<td>4.00</td>
<td>🔽 1.25</td>
<td>🔽 1.01</td>
<td>-</td>
<td>4.69%</td>
<td>02/01 14:53</td>
<td>4.88%</td>
<td>1.41%</td>
<td>48%</td>
<td>🔴 4.5</td>
</tr>
<tr>
<td>[**8016**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8016/)</td>
<td>矽創</td>
<td>12.00</td>
<td>🔽 10.38</td>
<td>🔽 9.85</td>
<td>-</td>
<td>6.69%</td>
<td>02/01 14:49</td>
<td>7.48%</td>
<td>5.12%</td>
<td>78%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**8045**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8045/)</td>
<td>達運光電</td>
<td>1.97</td>
<td>🔽 0.75</td>
<td>🔽 0.66</td>
<td>-</td>
<td>2.58%</td>
<td>02/01 14:50</td>
<td>3.22%</td>
<td>1.29%</td>
<td>80%</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**8299**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8299/)</td>
<td>群聯</td>
<td>31.31</td>
<td>🔽 16.54</td>
<td>🔽 18.35</td>
<td>🔽 17.69</td>
<td>2.16%</td>
<td>02/01 14:33</td>
<td>7.71%</td>
<td>2.13%</td>
<td>80%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**8454**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8454/)</td>
<td>富邦媒</td>
<td>12.80</td>
<td>🔽 9.36</td>
<td>🔽 10.36</td>
<td>-</td>
<td>6.17%</td>
<td>02/01 14:56</td>
<td>6.27%</td>
<td>3.25%</td>
<td>95%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**9914**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-9914/)</td>
<td>美利達</td>
<td>4.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>4.84%</td>
<td>02/01 14:31</td>
<td>4.91%</td>
<td>2.09%</td>
<td>-</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**9917**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-9917/)</td>
<td>中保科</td>
<td>5.20</td>
<td>🔼 5.72</td>
<td>🔼 5.73</td>
<td>-</td>
<td>4.81%</td>
<td>02/01 14:40</td>
<td>4.95%</td>
<td>4.08%</td>
<td>81%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**9921**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-9921/)</td>
<td>巨大</td>
<td>2.20</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>2.38%</td>
<td>02/01 14:33</td>
<td>2.44%</td>
<td>1.29%</td>
<td>68%</td>
<td>🟢 8.0</td>
</tr>
</tbody>
</table>

---

## :information_source: 資料來源與涵蓋範圍

!!! note "資料統計"
    - **分析股票數**: 103 檔
    - **略過股票數**: 23 檔 (資料不足: < 3 年)
    - **平均資料品質**: 9.5/10

!!! info "報告元資訊"
    - **報告產生時間**: 2026-02-02 19:25:00
    - **資料來源**: Stage 2 資料清理股利報告系統
    - **主要資料**: `cleaned_dividends.csv` (Type 1: DividendDetail)
    - **EPS資料**: `cleaned_performance1.csv` (Type 7: Quarterly Performance)

---

<div class="result" markdown>

:material-information-outline: **本報告僅供參考，投資決策請審慎評估**

</div>
