---
authors: [wenchiehlee]
date: 2026-04-25
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
description: 股利分配總覽 - 所有 126 檔股票 (有效 123 檔) - 自動產生
---

<style>
.sortable-table, .sortable-table td, .sortable-table th {
    font-size: var(--md-text-size) !important;
}
</style>

# :bar_chart: 股利分配總覽 - 所有股票

!!! info "報告概覽"
    **:calendar: 產生時間**: 2026-04-25 13:08:07 CST  
    **:building_construction: 分析股票總數**: 126 檔 (有效 123 檔)  
    **:chart_with_upwards_trend: 報告類型**: 完整股利分配分析  
    **:file_folder: 資料來源**: Stage 2 cleaned_dividends.csv + cleaned_performance1.csv

---

## :globe_with_meridians: 投資組合股利總覽

| :chart: 指標 | :bar_chart: 平均值 | :1234: 中位數 | :trophy: 最佳股票 | :warning: 最弱股票 |
|:--------:|:-------------:|:--------:|:-----------:|:------------:|
| **現金殖利率 (5年平均)** | 3.79% | 3.72% | [**2603**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2603/): 19.11% | [**2646**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2646/): 0.00% |
| **穩定性評分** | 5.9/10 | 6.0/10 | [**2301**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2301/): 8.5/10 | [**2405**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2405/): 0.0/10 |

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
<td>3.00</td>
<td>🔼 4.61</td>
<td>🔼 4.65</td>
<td>🔼 4.50</td>
<td>2.03%</td>
<td>04/01 12:08</td>
<td>2.15%</td>
<td>1.50%</td>
<td>45%</td>
<td>🟢 8.5</td>
</tr>
<tr>
<td>[**2303**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2303/)</td>
<td>聯電</td>
<td>2.60</td>
<td>🔽 2.20</td>
<td>🔽 2.21</td>
<td>🔽 2.20</td>
<td>4.53%</td>
<td>04/01 12:17</td>
<td>5.41%</td>
<td>3.26%</td>
<td>78%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2308**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2308/)</td>
<td>台達電</td>
<td>11.60</td>
<td>🔼 13.02</td>
<td>🔼 13.11</td>
<td>🔼 13.75</td>
<td>0.79%</td>
<td>04/01 11:48</td>
<td>1.20%</td>
<td>0.74%</td>
<td>50%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2317**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2317/)</td>
<td>鴻海</td>
<td>7.20</td>
<td>🔼 7.74</td>
<td>🔽 7.13</td>
<td>🔼 7.74</td>
<td>3.65%</td>
<td>04/01 11:49</td>
<td>3.84%</td>
<td>2.84%</td>
<td>53%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**2324**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2324/)</td>
<td>仁寶</td>
<td>1.10</td>
<td>🔽 0.85</td>
<td>🔽 0.96</td>
<td>🔼 1.93</td>
<td>4.01%</td>
<td>04/01 11:49</td>
<td>4.10%</td>
<td>3.13%</td>
<td>80%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2330**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2330/)</td>
<td>台積電</td>
<td>12.00</td>
<td>🔼 23.95</td>
<td>🔼 24.33</td>
<td>🔼 26.41</td>
<td>0.65%</td>
<td>04/01 11:50</td>
<td>0.78%</td>
<td>0.59%</td>
<td>18%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2332**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2332/)</td>
<td>友訊</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>04/01 12:35</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**2345**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2345/)</td>
<td>智邦</td>
<td>15.00</td>
<td>🔼 24.47</td>
<td>🔼 25.25</td>
<td>-</td>
<td>0.90%</td>
<td>04/01 12:48</td>
<td>1.38%</td>
<td>0.86%</td>
<td>32%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2347**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2347/)</td>
<td>聯強</td>
<td>4.20</td>
<td>🔽 3.20</td>
<td>🔽 3.14</td>
<td>-</td>
<td>5.42%</td>
<td>04/01 11:50</td>
<td>7.28%</td>
<td>5.18%</td>
<td>83%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2353**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2353/)</td>
<td>宏碁</td>
<td>1.30</td>
<td>🔽 1.17</td>
<td>🔽 1.12</td>
<td>-</td>
<td>4.76%</td>
<td>04/01 12:19</td>
<td>5.19%</td>
<td>4.41%</td>
<td>103%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2354**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2354/)</td>
<td>鴻準</td>
<td>1.50</td>
<td>🔽 1.21</td>
<td>🔽 1.28</td>
<td>-</td>
<td>2.86%</td>
<td>04/01 11:51</td>
<td>2.99%</td>
<td>2.42%</td>
<td>65%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2356**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2356/)</td>
<td>英業達</td>
<td>2.00</td>
<td>🔼 2.05</td>
<td>🔼 2.03</td>
<td>🔼 2.01</td>
<td>4.87%</td>
<td>04/01 11:51</td>
<td>5.19%</td>
<td>3.64%</td>
<td>83%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2357**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2357/)</td>
<td>華碩</td>
<td>42.00</td>
<td>🔽 40.94</td>
<td>🔼 45.06</td>
<td>🔽 40.33</td>
<td>7.41%</td>
<td>04/01 11:52</td>
<td>8.57%</td>
<td>6.95%</td>
<td>70%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2359**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2359/)</td>
<td>所羅門</td>
<td>1.00</td>
<td>🔽 0.70</td>
<td>🔽 0.96</td>
<td>-</td>
<td>0.90%</td>
<td>04/01 12:37</td>
<td>0.93%</td>
<td>0.67%</td>
<td>81%</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**2360**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2360/)</td>
<td>致茂</td>
<td>19.50</td>
<td>🔽 18.40</td>
<td>🔽 19.28</td>
<td>-</td>
<td>1.21%</td>
<td>04/01 12:54</td>
<td>2.51%</td>
<td>1.12%</td>
<td>70%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2376**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2376/)</td>
<td>技嘉</td>
<td>10.00</td>
<td>🔼 12.15</td>
<td>🔼 12.41</td>
<td>🔼 13.84</td>
<td>4.01%</td>
<td>04/01 11:52</td>
<td>5.56%</td>
<td>3.15%</td>
<td>66%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2377**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2377/)</td>
<td>微星</td>
<td>4.20</td>
<td>🔽 4.12</td>
<td>🔽 3.98</td>
<td>-</td>
<td>4.77%</td>
<td>04/01 11:53</td>
<td>4.94%</td>
<td>4.08%</td>
<td>62%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2379**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2379/)</td>
<td>瑞昱</td>
<td>25.00</td>
<td>🔽 22.03</td>
<td>🔽 24.54</td>
<td>-</td>
<td>5.16%</td>
<td>04/01 11:53</td>
<td>5.71%</td>
<td>4.22%</td>
<td>87%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2382**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2382/)</td>
<td>廣達</td>
<td>15.60</td>
<td>🔽 15.42</td>
<td>🔼 15.83</td>
<td>🔽 15.42</td>
<td>5.37%</td>
<td>04/01 11:54</td>
<td>5.81%</td>
<td>5.17%</td>
<td>80%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2383**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2383/)</td>
<td>台光電</td>
<td>25.00</td>
<td>🔽 23.95</td>
<td>🔽 24.77</td>
<td>-</td>
<td>0.87%</td>
<td>04/01 12:42</td>
<td>1.63%</td>
<td>0.82%</td>
<td>60%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2395**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2395/)</td>
<td>研華</td>
<td>11.20</td>
<td>🔽 9.46</td>
<td>🔽 9.69</td>
<td>🔽 9.13</td>
<td>3.38%</td>
<td>04/01 11:55</td>
<td>4.08%</td>
<td>2.97%</td>
<td>91%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2405**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2405/)</td>
<td>輔信</td>
<td>0.10</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.65%</td>
<td>04/01 11:56</td>
<td>0.70%</td>
<td>0.55%</td>
<td>-</td>
<td>🔴 0.0</td>
</tr>
<tr>
<td>[**2408**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2408/)</td>
<td>南亞科</td>
<td>1.50</td>
<td>🔽 1.22</td>
<td>🔽 1.17</td>
<td>-</td>
<td>0.71%</td>
<td>04/01 12:52</td>
<td>0.79%</td>
<td>0.46%</td>
<td>71%</td>
<td>🔴 2.5</td>
</tr>
<tr>
<td>[**2412**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2412/)</td>
<td>中華電</td>
<td>5.20</td>
<td>🔽 4.99</td>
<td>🔽 5.08</td>
<td>-</td>
<td>3.88%</td>
<td>04/01 11:56</td>
<td>3.97%</td>
<td>3.77%</td>
<td>104%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2449**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2449/)</td>
<td>京元電子</td>
<td>1.00</td>
<td>🔼 3.88</td>
<td>🔼 4.71</td>
<td>-</td>
<td>0.36%</td>
<td>04/01 12:48</td>
<td>0.40%</td>
<td>0.30%</td>
<td>17%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2450**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2450/)</td>
<td>神腦</td>
<td>1.55</td>
<td>🔽 1.46</td>
<td>🔽 1.46</td>
<td>-</td>
<td>5.31%</td>
<td>04/01 12:17</td>
<td>5.44%</td>
<td>5.08%</td>
<td>90%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2451**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2451/)</td>
<td>創見</td>
<td>11.80</td>
<td>🔼 13.96</td>
<td>🔼 13.27</td>
<td>-</td>
<td>5.13%</td>
<td>04/01 11:57</td>
<td>6.16%</td>
<td>3.52%</td>
<td>91%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2454**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2454/)</td>
<td>聯發科</td>
<td>53.50</td>
<td>🔼 60.80</td>
<td>🔼 63.54</td>
<td>🔼 57.86</td>
<td>3.65%</td>
<td>04/01 11:57</td>
<td>3.78%</td>
<td>2.71%</td>
<td>81%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2458**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2458/)</td>
<td>義隆</td>
<td>4.42</td>
<td>🔼 6.12</td>
<td>🔼 6.14</td>
<td>🔼 5.56</td>
<td>3.47%</td>
<td>04/01 11:58</td>
<td>3.83%</td>
<td>3.08%</td>
<td>52%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**2474**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2474/)</td>
<td>可成</td>
<td>11.49</td>
<td>🔽 6.45</td>
<td>🔽 8.67</td>
<td>-</td>
<td>5.52%</td>
<td>04/01 11:59</td>
<td>6.53%</td>
<td>5.03%</td>
<td>59%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**2480**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2480/)</td>
<td>敦陽科</td>
<td>7.80</td>
<td>🔽 7.24</td>
<td>🔽 7.53</td>
<td>-</td>
<td>5.61%</td>
<td>04/01 11:59</td>
<td>5.76%</td>
<td>5.08%</td>
<td>98%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2603**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2603/)</td>
<td>長榮</td>
<td>16.00</td>
<td>🔽 15.41</td>
<td>🔼 17.96</td>
<td>🔼 18.10</td>
<td>7.82%</td>
<td>04/01 12:39</td>
<td>8.74%</td>
<td>7.19%</td>
<td>51%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**2646**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2646/)</td>
<td>星宇航空</td>
<td>0.00</td>
<td>🟡 0.00</td>
<td>⚪ 0.00</td>
<td>-</td>
<td>0.00%</td>
<td>04/01 12:14</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🔴 0.5</td>
</tr>
<tr>
<td>[**2881**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2881/)</td>
<td>富邦金</td>
<td>4.25</td>
<td>🔽 2.42</td>
<td>🔽 3.30</td>
<td>-</td>
<td>4.42%</td>
<td>04/01 12:50</td>
<td>5.89%</td>
<td>4.30%</td>
<td>42%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**2882**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2882/)</td>
<td>國泰金</td>
<td>3.50</td>
<td>🔽 2.52</td>
<td>🔽 3.17</td>
<td>🔽 2.92</td>
<td>4.62%</td>
<td>04/01 12:50</td>
<td>7.07%</td>
<td>4.53%</td>
<td>48%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**2884**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2884/)</td>
<td>玉山金</td>
<td>1.40</td>
<td>🔽 1.11</td>
<td>🔽 1.16</td>
<td>-</td>
<td>4.33%</td>
<td>04/01 12:51</td>
<td>4.54%</td>
<td>3.94%</td>
<td>66%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**2891**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-2891/)</td>
<td>中信金</td>
<td>2.30</td>
<td>🔽 2.12</td>
<td>🔼 2.35</td>
<td>-</td>
<td>4.58%</td>
<td>04/01 12:50</td>
<td>6.84%</td>
<td>4.52%</td>
<td>63%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**3014**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3014/)</td>
<td>聯陽</td>
<td>8.50</td>
<td>🔽 7.40</td>
<td>🔽 7.98</td>
<td>-</td>
<td>7.33%</td>
<td>04/01 12:23</td>
<td>7.69%</td>
<td>6.75%</td>
<td>89%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**3022**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3022/)</td>
<td>威強電</td>
<td>3.50</td>
<td>🔽 1.49</td>
<td>🔽 2.54</td>
<td>-</td>
<td>5.70%</td>
<td>04/01 12:00</td>
<td>6.32%</td>
<td>4.82%</td>
<td>76%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**3026**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3026/)</td>
<td>禾伸堂</td>
<td>5.80</td>
<td>🔽 5.26</td>
<td>🔽 5.46</td>
<td>-</td>
<td>4.08%</td>
<td>04/01 12:00</td>
<td>5.80%</td>
<td>3.68%</td>
<td>88%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**3029**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3029/)</td>
<td>零壹</td>
<td>5.50</td>
<td>🔼 5.65</td>
<td>🔼 5.76</td>
<td>-</td>
<td>5.74%</td>
<td>04/01 12:30</td>
<td>5.93%</td>
<td>4.44%</td>
<td>84%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3034**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3034/)</td>
<td>聯詠</td>
<td>23.00</td>
<td>🔽 21.72</td>
<td>🔽 22.24</td>
<td>🔼 24.68</td>
<td>5.87%</td>
<td>04/01 12:01</td>
<td>6.53%</td>
<td>5.66%</td>
<td>86%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3035**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3035/)</td>
<td>智原</td>
<td>1.80</td>
<td>🔽 1.54</td>
<td>🔼 1.84</td>
<td>🔽 1.76</td>
<td>1.25%</td>
<td>04/01 12:08</td>
<td>1.29%</td>
<td>0.99%</td>
<td>64%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**3045**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3045/)</td>
<td>台灣大</td>
<td>4.80</td>
<td>🔼 4.84</td>
<td>🔼 4.94</td>
<td>-</td>
<td>4.38%</td>
<td>04/01 12:01</td>
<td>4.59%</td>
<td>4.36%</td>
<td>101%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**3048**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3048/)</td>
<td>益登</td>
<td>1.00</td>
<td>🔼 1.13</td>
<td>🔼 1.23</td>
<td>-</td>
<td>2.88%</td>
<td>04/01 12:02</td>
<td>2.92%</td>
<td>2.01%</td>
<td>50%</td>
<td>🔴 4.5</td>
</tr>
<tr>
<td>[**3150**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3150/)</td>
<td>鈺寶-創</td>
<td>0.50</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>2.89%</td>
<td>04/01 12:14</td>
<td>3.25%</td>
<td>2.27%</td>
<td>-</td>
<td>🔴 3.0</td>
</tr>
<tr>
<td>[**3158**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3158/)</td>
<td>嘉實</td>
<td>6.50</td>
<td>🔽 6.36</td>
<td>🔽 5.61</td>
<td>-</td>
<td>7.16%</td>
<td>04/01 12:20</td>
<td>7.49%</td>
<td>6.53%</td>
<td>88%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**3231**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3231/)</td>
<td>緯創</td>
<td>5.50</td>
<td>🔽 5.39</td>
<td>🔼 5.63</td>
<td>🔽 5.39</td>
<td>4.33%</td>
<td>04/01 12:02</td>
<td>4.49%</td>
<td>3.42%</td>
<td>60%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**3260**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3260/)</td>
<td>威剛</td>
<td>17.00</td>
<td>🔽 14.74</td>
<td>🔽 14.18</td>
<td>-</td>
<td>4.61%</td>
<td>04/01 12:43</td>
<td>6.72%</td>
<td>3.24%</td>
<td>73%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3293**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3293/)</td>
<td>鈊象</td>
<td>36.00</td>
<td>🔽 31.06</td>
<td>🔽 30.37</td>
<td>-</td>
<td>4.69%</td>
<td>04/01 12:38</td>
<td>5.37%</td>
<td>4.47%</td>
<td>93%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**3356**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3356/)</td>
<td>奇偶</td>
<td>4.00</td>
<td>🔼 6.29</td>
<td>🔼 4.75</td>
<td>-</td>
<td>8.51%</td>
<td>04/01 12:03</td>
<td>10.11%</td>
<td>5.94%</td>
<td>57%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**3467**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3467/)</td>
<td>台灣精材</td>
<td>0.50</td>
<td>🔼 0.60</td>
<td>🔽 0.47</td>
<td>-</td>
<td>1.16%</td>
<td>04/01 12:44</td>
<td>1.35%</td>
<td>1.05%</td>
<td>83%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**3558**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3558/)</td>
<td>神準</td>
<td>3.00</td>
<td>🔽 1.74</td>
<td>🔽 2.07</td>
<td>-</td>
<td>2.70%</td>
<td>04/01 12:16</td>
<td>2.79%</td>
<td>2.00%</td>
<td>58%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**3653**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3653/)</td>
<td>健策</td>
<td>22.00</td>
<td>🔽 20.34</td>
<td>🔽 21.99</td>
<td>-</td>
<td>0.56%</td>
<td>04/01 12:55</td>
<td>0.96%</td>
<td>0.52%</td>
<td>60%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**3661**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3661/)</td>
<td>世芯-KY</td>
<td>34.41</td>
<td>🔽 33.21</td>
<td>🔽 34.26</td>
<td>-</td>
<td>1.26%</td>
<td>04/01 12:49</td>
<td>1.39%</td>
<td>0.90%</td>
<td>50%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**3665**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3665/)</td>
<td>貿聯-KY</td>
<td>15.00</td>
<td>🔼 21.62</td>
<td>🔼 21.96</td>
<td>-</td>
<td>0.79%</td>
<td>04/01 12:55</td>
<td>1.20%</td>
<td>0.78%</td>
<td>32%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**3711**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-3711/)</td>
<td>日月光投控</td>
<td>6.60</td>
<td>🔼 8.32</td>
<td>🔽 5.99</td>
<td>🔼 8.62</td>
<td>1.83%</td>
<td>04/01 12:51</td>
<td>2.64%</td>
<td>1.68%</td>
<td>70%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**4114**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4114/)</td>
<td>健喬</td>
<td>0.60</td>
<td>🔽 0.49</td>
<td>🔽 0.51</td>
<td>-</td>
<td>1.85%</td>
<td>04/01 12:44</td>
<td>2.07%</td>
<td>1.51%</td>
<td>92%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**4749**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4749/)</td>
<td>新應材</td>
<td>8.00</td>
<td>🔼 8.04</td>
<td>🔼 8.02</td>
<td>-</td>
<td>0.97%</td>
<td>04/01 12:28</td>
<td>1.00%</td>
<td>0.78%</td>
<td>71%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**4938**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4938/)</td>
<td>和碩</td>
<td>4.00</td>
<td>🔽 3.45</td>
<td>🔽 3.76</td>
<td>🔼 6.17</td>
<td>5.12%</td>
<td>04/01 12:03</td>
<td>5.89%</td>
<td>4.79%</td>
<td>74%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**4953**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-4953/)</td>
<td>緯軟</td>
<td>5.00</td>
<td>🔼 5.33</td>
<td>🔼 5.19</td>
<td>-</td>
<td>4.55%</td>
<td>04/01 12:15</td>
<td>4.65%</td>
<td>3.52%</td>
<td>59%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**5203**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5203/)</td>
<td>訊連</td>
<td>3.60</td>
<td>🔽 2.24</td>
<td>🔽 3.59</td>
<td>-</td>
<td>5.70%</td>
<td>04/01 12:03</td>
<td>5.99%</td>
<td>4.00%</td>
<td>99%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**5269**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5269/)</td>
<td>祥碩</td>
<td>30.00</td>
<td>🔼 38.71</td>
<td>🔼 40.53</td>
<td>-</td>
<td>2.48%</td>
<td>04/01 12:10</td>
<td>2.65%</td>
<td>1.32%</td>
<td>58%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**5274**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5274/)</td>
<td>信驊</td>
<td>80.00</td>
<td>🔽 78.94</td>
<td>🔼 82.95</td>
<td>🔽 75.50</td>
<td>0.71%</td>
<td>04/01 12:38</td>
<td>1.13%</td>
<td>0.64%</td>
<td>78%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**5434**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5434/)</td>
<td>崇越</td>
<td>13.50</td>
<td>🔼 13.63</td>
<td>🔼 13.90</td>
<td>-</td>
<td>4.19%</td>
<td>04/01 12:07</td>
<td>4.64%</td>
<td>3.81%</td>
<td>62%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**5536**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5536/)</td>
<td>聖暉</td>
<td>20.00</td>
<td>🔽 19.74</td>
<td>🔽 19.54</td>
<td>-</td>
<td>2.79%</td>
<td>04/01 12:36</td>
<td>3.36%</td>
<td>2.37%</td>
<td>70%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**5904**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-5904/)</td>
<td>寶雅</td>
<td>25.50</td>
<td>🔽 25.00</td>
<td>🔼 25.74</td>
<td>-</td>
<td>5.05%</td>
<td>04/01 12:21</td>
<td>6.50%</td>
<td>4.87%</td>
<td>86%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6035**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6035/)</td>
<td>悠遊卡</td>
<td>2.28</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>4.15%</td>
<td>04/01 12:20</td>
<td>4.48%</td>
<td>3.83%</td>
<td>-</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6123**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6123/)</td>
<td>上奇</td>
<td>2.60</td>
<td>🔼 2.80</td>
<td>🔼 2.64</td>
<td>-</td>
<td>6.06%</td>
<td>04/01 12:28</td>
<td>6.24%</td>
<td>5.37%</td>
<td>96%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**6125**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6125/)</td>
<td>廣運</td>
<td>0.50</td>
<td>🔽 0.04</td>
<td>🔽 0.07</td>
<td>-</td>
<td>0.92%</td>
<td>04/01 12:37</td>
<td>0.94%</td>
<td>0.64%</td>
<td>500%</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**6182**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6182/)</td>
<td>合晶</td>
<td>0.00</td>
<td>🔼 0.03</td>
<td>🔼 0.04</td>
<td>-</td>
<td>0.00%</td>
<td>04/01 12:21</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🔴 3.5</td>
</tr>
<tr>
<td>[**6214**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6214/)</td>
<td>精誠</td>
<td>5.20</td>
<td>🔼 7.16</td>
<td>🔼 7.01</td>
<td>-</td>
<td>4.41%</td>
<td>04/01 12:04</td>
<td>5.28%</td>
<td>3.44%</td>
<td>67%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6231**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6231/)</td>
<td>系微</td>
<td>5.70</td>
<td>🔽 5.17</td>
<td>🔽 5.23</td>
<td>-</td>
<td>2.13%</td>
<td>04/01 12:15</td>
<td>3.19%</td>
<td>1.95%</td>
<td>86%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6285**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6285/)</td>
<td>啟碁</td>
<td>4.30</td>
<td>🔽 4.03</td>
<td>🔽 4.19</td>
<td>-</td>
<td>2.42%</td>
<td>04/01 12:04</td>
<td>4.34%</td>
<td>2.07%</td>
<td>67%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**6425**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6425/)</td>
<td>易發</td>
<td>0.50</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.79%</td>
<td>04/01 12:29</td>
<td>0.83%</td>
<td>0.56%</td>
<td>-</td>
<td>🔴 4.5</td>
</tr>
<tr>
<td>[**6442**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6442/)</td>
<td>光聖</td>
<td>11.80</td>
<td>🔼 14.16</td>
<td>🔼 14.77</td>
<td>-</td>
<td>0.58%</td>
<td>04/01 12:34</td>
<td>0.98%</td>
<td>0.46%</td>
<td>50%</td>
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
<td>04/01 12:05</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 2.0</td>
</tr>
<tr>
<td>[**6506**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6506/)</td>
<td>雙邦</td>
<td>1.00</td>
<td>🔽 0.62</td>
<td>🔽 0.84</td>
<td>-</td>
<td>6.02%</td>
<td>04/01 12:38</td>
<td>6.51%</td>
<td>5.92%</td>
<td>95%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6510**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6510/)</td>
<td>精測</td>
<td>15.30</td>
<td>🔽 15.21</td>
<td>🔽 15.27</td>
<td>-</td>
<td>0.46%</td>
<td>04/01 12:49</td>
<td>0.73%</td>
<td>0.36%</td>
<td>50%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**6526**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6526/)</td>
<td>達發</td>
<td>13.50</td>
<td>🔽 10.06</td>
<td>🔽 10.69</td>
<td>-</td>
<td>2.79%</td>
<td>04/01 12:07</td>
<td>3.20%</td>
<td>2.32%</td>
<td>78%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6561**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6561/)</td>
<td>是方</td>
<td>7.60</td>
<td>🔼 13.86</td>
<td>🔼 13.93</td>
<td>🔼 8.68</td>
<td>2.15%</td>
<td>04/01 12:11</td>
<td>2.44%</td>
<td>1.95%</td>
<td>48%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6597**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6597/)</td>
<td>立誠</td>
<td>1.00</td>
<td>🔽 0.58</td>
<td>🔼 1.20</td>
<td>-</td>
<td>1.66%</td>
<td>04/01 12:45</td>
<td>1.96%</td>
<td>1.48%</td>
<td>39%</td>
<td>🔴 3.5</td>
</tr>
<tr>
<td>[**6613**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6613/)</td>
<td>朋億</td>
<td>10.00</td>
<td>🔽 9.56</td>
<td>🔽 9.21</td>
<td>-</td>
<td>4.81%</td>
<td>04/01 12:18</td>
<td>5.60%</td>
<td>4.50%</td>
<td>75%</td>
<td>🟡 7.5</td>
</tr>
<tr>
<td>[**6669**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6669/)</td>
<td>緯穎</td>
<td>145.00</td>
<td>🔼 151.65</td>
<td>🔼 156.38</td>
<td>🔽 144.32</td>
<td>4.24%</td>
<td>04/01 12:10</td>
<td>4.41%</td>
<td>2.99%</td>
<td>60%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6690**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6690/)</td>
<td>安碁資訊</td>
<td>9.00</td>
<td>🔽 6.88</td>
<td>🔽 6.64</td>
<td>-</td>
<td>5.50%</td>
<td>04/01 12:31</td>
<td>5.71%</td>
<td>5.16%</td>
<td>88%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**6695**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6695/)</td>
<td>芯鼎</td>
<td>0.00</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.00%</td>
<td>04/01 12:11</td>
<td>0.00%</td>
<td>0.00%</td>
<td>-</td>
<td>🔴 0.5</td>
</tr>
<tr>
<td>[**6720**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6720/)</td>
<td>久昌</td>
<td>3.50</td>
<td>🔽 1.58</td>
<td>🔽 2.16</td>
<td>-</td>
<td>2.03%</td>
<td>04/01 12:23</td>
<td>3.02%</td>
<td>1.92%</td>
<td>84%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6751**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6751/)</td>
<td>智聯服務</td>
<td>3.00</td>
<td>🔼 4.21</td>
<td>🔼 4.19</td>
<td>-</td>
<td>5.95%</td>
<td>04/01 12:33</td>
<td>5.99%</td>
<td>4.22%</td>
<td>58%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**6757**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6757/)</td>
<td>台灣虎航</td>
<td>2.42</td>
<td>🔽 2.02</td>
<td>🔼 2.56</td>
<td>-</td>
<td>4.78%</td>
<td>04/01 12:24</td>
<td>5.13%</td>
<td>3.32%</td>
<td>45%</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**6763**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6763/)</td>
<td>綠界科技</td>
<td>3.00</td>
<td>🔽 2.81</td>
<td>🔽 2.35</td>
<td>-</td>
<td>6.36%</td>
<td>04/01 12:32</td>
<td>6.50%</td>
<td>5.12%</td>
<td>71%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6811**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6811/)</td>
<td>宏碁資訊</td>
<td>10.50</td>
<td>🔽 9.53</td>
<td>🔽 10.12</td>
<td>-</td>
<td>5.65%</td>
<td>04/01 12:30</td>
<td>5.83%</td>
<td>4.57%</td>
<td>73%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6850**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6850/)</td>
<td>光鼎生技</td>
<td>0.30</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0.75%</td>
<td>04/01 12:46</td>
<td>0.79%</td>
<td>0.57%</td>
<td>-</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**6902**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6902/)</td>
<td>GOGOLOOK</td>
<td>0.00</td>
<td>🟠 0.00</td>
<td>⚪ 0.00</td>
<td>-</td>
<td>0.00%</td>
<td>04/01 12:46</td>
<td>0.00%</td>
<td>0.00%</td>
<td>0%</td>
<td>🔴 0.5</td>
</tr>
<tr>
<td>[**6918**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6918/)</td>
<td>愛派司</td>
<td>5.00</td>
<td>🔽 3.52</td>
<td>🔽 3.89</td>
<td>-</td>
<td>6.38%</td>
<td>04/01 12:46</td>
<td>6.45%</td>
<td>5.69%</td>
<td>95%</td>
<td>🔴 4.0</td>
</tr>
<tr>
<td>[**6925**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6925/)</td>
<td>意藍</td>
<td>2.00</td>
<td>🔼 2.19</td>
<td>🔽 1.94</td>
<td>-</td>
<td>2.69%</td>
<td>04/01 12:47</td>
<td>2.93%</td>
<td>2.07%</td>
<td>64%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**6962**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6962/)</td>
<td>奕力-KY</td>
<td>1.00</td>
<td>🔼 1.61</td>
<td>🔼 1.61</td>
<td>-</td>
<td>3.00%</td>
<td>04/01 12:22</td>
<td>3.42%</td>
<td>2.42%</td>
<td>34%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6996**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6996/)</td>
<td>力領科技</td>
<td>10.00</td>
<td>🔼 12.14</td>
<td>🔼 10.13</td>
<td>-</td>
<td>6.01%</td>
<td>04/01 12:25</td>
<td>7.12%</td>
<td>5.51%</td>
<td>82%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**6997**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-6997/)</td>
<td>博弘</td>
<td>4.60</td>
<td>🔽 4.42</td>
<td>🔽 4.40</td>
<td>-</td>
<td>5.69%</td>
<td>04/01 12:27</td>
<td>5.69%</td>
<td>5.05%</td>
<td>90%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7547**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7547/)</td>
<td>碩網</td>
<td>1.80</td>
<td>🔼 1.92</td>
<td>🔼 1.85</td>
<td>-</td>
<td>2.10%</td>
<td>04/01 12:39</td>
<td>3.61%</td>
<td>1.97%</td>
<td>67%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**7703**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7703/)</td>
<td>銳澤</td>
<td>7.00</td>
<td>🔼 7.26</td>
<td>🔽 6.49</td>
<td>-</td>
<td>3.26%</td>
<td>04/01 12:19</td>
<td>3.78%</td>
<td>2.71%</td>
<td>80%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**7704**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7704/)</td>
<td>明遠精密</td>
<td>1.80</td>
<td>🔼 2.17</td>
<td>🔽 1.66</td>
<td>-</td>
<td>3.98%</td>
<td>04/01 12:27</td>
<td>4.19%</td>
<td>3.66%</td>
<td>87%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**7705**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7705/)</td>
<td>三商餐飲</td>
<td>1.60</td>
<td>🔼 2.02</td>
<td>🔼 1.79</td>
<td>-</td>
<td>4.62%</td>
<td>04/01 12:22</td>
<td>4.68%</td>
<td>3.96%</td>
<td>83%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**7708**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7708/)</td>
<td>全家餐飲</td>
<td>5.50</td>
<td>🔽 4.79</td>
<td>🔽 4.87</td>
<td>-</td>
<td>5.97%</td>
<td>04/01 12:18</td>
<td>6.04%</td>
<td>5.67%</td>
<td>85%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**7709**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7709/)</td>
<td>榮田</td>
<td>1.50</td>
<td>🔽 1.07</td>
<td>🔽 1.32</td>
<td>-</td>
<td>2.07%</td>
<td>04/01 12:42</td>
<td>3.99%</td>
<td>1.81%</td>
<td>60%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7712**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7712/)</td>
<td>博盛半導體</td>
<td>4.00</td>
<td>🔽 1.28</td>
<td>🔽 1.07</td>
<td>-</td>
<td>4.69%</td>
<td>04/01 12:29</td>
<td>4.88%</td>
<td>1.41%</td>
<td>48%</td>
<td>🔴 4.5</td>
</tr>
<tr>
<td>[**7713**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7713/)</td>
<td>威力德生醫</td>
<td>4.10</td>
<td>🔽 4.03</td>
<td>🔽 3.59</td>
<td>-</td>
<td>6.09%</td>
<td>04/01 12:43</td>
<td>6.13%</td>
<td>5.51%</td>
<td>88%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7722**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7722/)</td>
<td>LINEPAY</td>
<td>1.50</td>
<td>🔽 0.90</td>
<td>🔽 0.89</td>
<td>-</td>
<td>0.49%</td>
<td>04/01 12:20</td>
<td>0.50%</td>
<td>0.26%</td>
<td>27%</td>
<td>🔴 1.5</td>
</tr>
<tr>
<td>[**7728**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7728/)</td>
<td>光焱科技</td>
<td>5.00</td>
<td>🔽 4.73</td>
<td>🔽 4.29</td>
<td>-</td>
<td>0.71%</td>
<td>04/01 12:41</td>
<td>0.88%</td>
<td>0.51%</td>
<td>103%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7732**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7732/)</td>
<td>金興精密</td>
<td>1.50</td>
<td>🔽 1.15</td>
<td>🔽 1.31</td>
<td>-</td>
<td>4.29%</td>
<td>04/01 12:41</td>
<td>4.57%</td>
<td>3.53%</td>
<td>87%</td>
<td>🔴 5.5</td>
</tr>
<tr>
<td>[**7734**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7734/)</td>
<td>印能科技</td>
<td>19.85</td>
<td>🔽 19.06</td>
<td>🔽 17.84</td>
<td>-</td>
<td>0.85%</td>
<td>04/01 12:40</td>
<td>2.09%</td>
<td>0.84%</td>
<td>55%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7736**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7736/)</td>
<td>虎山</td>
<td>3.80</td>
<td>🔽 2.94</td>
<td>🔽 2.92</td>
<td>-</td>
<td>4.64%</td>
<td>04/01 12:40</td>
<td>4.85%</td>
<td>3.94%</td>
<td>74%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**7747**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7747/)</td>
<td>昕奇雲端</td>
<td>3.00</td>
<td>🔽 2.95</td>
<td>🔽 2.89</td>
<td>-</td>
<td>2.61%</td>
<td>04/01 12:28</td>
<td>2.67%</td>
<td>2.43%</td>
<td>97%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7765**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7765/)</td>
<td>中華資安</td>
<td>9.67</td>
<td>🔽 9.12</td>
<td>🔽 8.81</td>
<td>-</td>
<td>4.27%</td>
<td>04/01 12:11</td>
<td>4.45%</td>
<td>3.34%</td>
<td>83%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**7794**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7794/)</td>
<td>宏碁智新</td>
<td>1.60</td>
<td>🔼 2.01</td>
<td>🔼 2.05</td>
<td>-</td>
<td>3.17%</td>
<td>04/01 12:24</td>
<td>3.70%</td>
<td>2.93%</td>
<td>120%</td>
<td>🔴 3.5</td>
</tr>
<tr>
<td>[**7805**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-7805/)</td>
<td>威聯通</td>
<td>38.00</td>
<td>🔽 36.82</td>
<td>🔼 39.33</td>
<td>-</td>
<td>5.51%</td>
<td>04/01 12:36</td>
<td>7.13%</td>
<td>4.94%</td>
<td>89%</td>
<td>🔴 5.0</td>
</tr>
<tr>
<td>[**8016**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8016/)</td>
<td>矽創</td>
<td>11.50</td>
<td>🔼 11.71</td>
<td>🔽 10.86</td>
<td>-</td>
<td>5.91%</td>
<td>04/01 12:26</td>
<td>6.57%</td>
<td>5.62%</td>
<td>79%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**8045**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8045/)</td>
<td>達運光電</td>
<td>1.00</td>
<td>🔽 0.67</td>
<td>🔽 0.50</td>
<td>-</td>
<td>1.35%</td>
<td>04/01 12:26</td>
<td>1.41%</td>
<td>1.06%</td>
<td>154%</td>
<td>🔴 2.5</td>
</tr>
<tr>
<td>[**8272**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8272/)</td>
<td>全景軟體</td>
<td>2.80</td>
<td>🔼 3.56</td>
<td>🔽 2.78</td>
<td>-</td>
<td>3.84%</td>
<td>04/01 12:06</td>
<td>3.97%</td>
<td>3.40%</td>
<td>60%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**8299**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8299/)</td>
<td>群聯</td>
<td>17.00</td>
<td>🔼 22.65</td>
<td>🔼 21.56</td>
<td>🔽 15.60</td>
<td>1.03%</td>
<td>04/01 12:07</td>
<td>1.19%</td>
<td>0.69%</td>
<td>40%</td>
<td>🟡 6.5</td>
</tr>
<tr>
<td>[**8454**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-8454/)</td>
<td>富邦媒</td>
<td>10.00</td>
<td>🔽 9.84</td>
<td>🔽 9.93</td>
<td>-</td>
<td>5.56%</td>
<td>04/01 12:35</td>
<td>5.80%</td>
<td>4.71%</td>
<td>86%</td>
<td>🟢 8.0</td>
</tr>
<tr>
<td>[**9914**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-9914/)</td>
<td>美利達</td>
<td>2.80</td>
<td>🔼 3.93</td>
<td>🔼 2.90</td>
<td>🔼 4.12</td>
<td>4.27%</td>
<td>04/01 12:05</td>
<td>4.34%</td>
<td>2.84%</td>
<td>70%</td>
<td>🟡 6.0</td>
</tr>
<tr>
<td>[**9917**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-9917/)</td>
<td>中保科</td>
<td>5.70</td>
<td>🔼 5.79</td>
<td>🔼 5.78</td>
<td>-</td>
<td>4.94%</td>
<td>04/01 12:16</td>
<td>5.51%</td>
<td>4.91%</td>
<td>91%</td>
<td>🟡 7.0</td>
</tr>
<tr>
<td>[**9921**](../stage2-cleaning-dividends-report/stage2-cleaning-dividends-report-9921/)</td>
<td>巨大</td>
<td>1.80</td>
<td>🔽 0.75</td>
<td>🔽 1.24</td>
<td>🔼 2.43</td>
<td>2.51%</td>
<td>04/01 12:06</td>
<td>2.60%</td>
<td>1.79%</td>
<td>98%</td>
<td>🟡 7.5</td>
</tr>
</tbody>
</table>

---

## :information_source: 資料來源與涵蓋範圍

!!! note "資料統計"
    - **分析股票數**: 123 檔
    - **略過股票數**: 3 檔 (資料不足: < 3 年)
    - **平均資料品質**: 9.5/10

!!! info "報告元資訊"
    - **報告產生時間**: 2026-04-25 13:08:07
    - **資料來源**: Stage 2 資料清理股利報告系統
    - **主要資料**: `cleaned_dividends.csv` (Type 1: DividendDetail)
    - **EPS資料**: `cleaned_performance1.csv` (Type 7: Quarterly Performance)

---

<div class="result" markdown>

:material-information-outline: **本報告僅供參考，投資決策請審慎評估**

</div>
