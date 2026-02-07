---
title: "6597 立誠 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-02-07"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 電子零組件業
description: "6597 立誠 (電子零組件業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6597 立誠 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6597
    - **公司名稱**: 立誠
    - **產業別**: 電子零組件業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-02-07 12:44:18 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6597 立誠 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 29.16,
        "forward_return": -37.4,
        "start_price": 76.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 30.5,
        "forward_return": -71.29,
        "start_price": 79.6,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 30.57,
        "forward_return": -74.61,
        "start_price": 79.8,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 24.9,
        "forward_return": -23.26,
        "start_price": 65.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 21.26,
        "forward_return": 32.22,
        "start_price": 55.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 21.65,
        "forward_return": 22.8,
        "start_price": 56.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 29.16,
        "forward_return": -29.26,
        "start_price": 76.1,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 30.5,
        "forward_return": -39.01,
        "start_price": 79.6,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 30.57,
        "forward_return": -44.16,
        "start_price": 79.8,
        "start_year": 2025
      }
    ]
  },
  "params": [
    {
      "name": "horizon_select",
      "value": "0.25y",
      "bind": {
        "input": "select",
        "options": [
          "All",
          "0.25y",
          "0.5y"
        ],
        "labels": [
          "全部期間",
          "3個月",
          "6個月"
        ],
        "name": "投資期間: "
      }
    }
  ],
  "transform": [
    {
      "filter": "horizon_select === 'All' || datum.horizon === horizon_select"
    },
    {
      "calculate": "horizon_select === 'All' ? datum.horizon_label : toString(datum.start_year)",
      "as": "color_field"
    }
  ],
  "vconcat": [
    {
      "title": "報酬率時間軸",
      "width": 600,
      "height": 200,
      "layer": [
        {
          "mark": {
            "type": "line",
            "opacity": 0.6,
            "strokeWidth": 1.5
          },
          "encoding": {
            "x": {
              "field": "start_date",
              "type": "temporal",
              "title": "買入日期"
            },
            "y": {
              "field": "forward_return",
              "type": "quantitative",
              "title": "年化報酬率 (%)"
            },
            "color": {
              "field": "color_field",
              "type": "nominal",
              "title": "分類",
              "scale": {
                "scheme": "turbo"
              }
            }
          }
        },
        {
          "mark": {
            "type": "circle",
            "size": 40
          },
          "encoding": {
            "x": {
              "field": "start_date",
              "type": "temporal"
            },
            "y": {
              "field": "forward_return",
              "type": "quantitative"
            },
            "color": {
              "field": "color_field",
              "type": "nominal",
              "title": "分類",
              "scale": {
                "scheme": "turbo"
              }
            },
            "tooltip": [
              {
                "field": "start_date",
                "type": "temporal",
                "title": "買入日期"
              },
              {
                "field": "horizon_label",
                "type": "nominal",
                "title": "投資期間"
              },
              {
                "field": "forward_return",
                "type": "quantitative",
                "title": "年化報酬率",
                "format": "+.1f"
              },
              {
                "field": "pe_ratio",
                "type": "quantitative",
                "title": "本益比",
                "format": ".1f"
              }
            ]
          }
        }
      ]
    },
    {
      "title": "本益比 vs 未來報酬率",
      "width": 600,
      "height": 350,
      "mark": {
        "type": "circle",
        "opacity": 0.7,
        "size": 60
      },
      "encoding": {
        "x": {
          "field": "pe_ratio",
          "type": "quantitative",
          "title": "本益比 (P/E)",
          "scale": {
            "zero": false
          }
        },
        "y": {
          "field": "forward_return",
          "type": "quantitative",
          "title": "年化報酬率 (%)"
        },
        "color": {
          "field": "color_field",
          "type": "nominal",
          "title": "分類",
          "scale": {
            "scheme": "turbo"
          }
        },
        "tooltip": [
          {
            "field": "start_date",
            "type": "temporal",
            "title": "買入日期"
          },
          {
            "field": "horizon_label",
            "type": "nominal",
            "title": "投資期間"
          },
          {
            "field": "pe_ratio",
            "type": "quantitative",
            "title": "本益比",
            "format": ".1f"
          },
          {
            "field": "forward_return",
            "type": "quantitative",
            "title": "年化報酬率",
            "format": "+.1f"
          },
          {
            "field": "start_price",
            "type": "quantitative",
            "title": "買入價格",
            "format": ".1f"
          }
        ]
      }
    }
  ]
}
```


## 🌊 本益比河流帶

股價與歷史本益比百分位（10%、25%、50%、75%、90%）對應的價位區間。綠色區域為低估值區，黃色為合理區，紅色為高估值區。

!!! note "本益比河流帶水位: 21.6倍、22.8倍、24.5倍、29.2倍、30.5倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6597 立誠 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-05-16",
        "price": 76.1,
        "pe": 29.16,
        "pe_10": 56.3,
        "pe_25": 59.5,
        "pe_50": 63.99,
        "pe_75": 76.1,
        "pe_90": 79.63
      },
      {
        "date": "2025-06-15",
        "price": 79.6,
        "pe": 30.5,
        "pe_10": 56.3,
        "pe_25": 59.5,
        "pe_50": 63.99,
        "pe_75": 76.1,
        "pe_90": 79.64
      },
      {
        "date": "2025-07-16",
        "price": 79.8,
        "pe": 30.57,
        "pe_10": 56.31,
        "pe_25": 59.52,
        "pe_50": 64.01,
        "pe_75": 76.12,
        "pe_90": 79.65
      },
      {
        "date": "2025-08-16",
        "price": 65.0,
        "pe": 24.9,
        "pe_10": 56.31,
        "pe_25": 59.52,
        "pe_50": 64.01,
        "pe_75": 76.12,
        "pe_90": 79.66
      },
      {
        "date": "2025-09-15",
        "price": 55.5,
        "pe": 21.26,
        "pe_10": 56.31,
        "pe_25": 59.52,
        "pe_50": 64.01,
        "pe_75": 76.12,
        "pe_90": 79.66
      },
      {
        "date": "2025-10-16",
        "price": 56.5,
        "pe": 21.65,
        "pe_10": 56.3,
        "pe_25": 59.5,
        "pe_50": 63.99,
        "pe_75": 76.1,
        "pe_90": 79.63
      },
      {
        "date": "2025-11-15",
        "price": 64.0,
        "pe": 24.52,
        "pe_10": 56.31,
        "pe_25": 59.51,
        "pe_50": 64.0,
        "pe_75": 76.11,
        "pe_90": 79.65
      },
      {
        "date": "2025-12-16",
        "price": 59.5,
        "pe": 22.8,
        "pe_10": 56.3,
        "pe_25": 59.5,
        "pe_50": 63.99,
        "pe_75": 76.1,
        "pe_90": 79.63
      },
      {
        "date": "2026-01-16",
        "price": 59.5,
        "pe": 22.8,
        "pe_10": 56.3,
        "pe_25": 59.5,
        "pe_50": 63.99,
        "pe_75": 76.1,
        "pe_90": 79.63
      }
    ]
  },
  "width": 700,
  "height": 350,
  "layer": [
    {
      "mark": {
        "type": "area",
        "opacity": 0.15
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal",
          "title": "日期"
        },
        "y": {
          "field": "pe_10",
          "type": "quantitative",
          "title": "股價 (元)"
        },
        "y2": {
          "field": "pe_25"
        },
        "color": {
          "value": "#4CAF50"
        }
      }
    },
    {
      "mark": {
        "type": "area",
        "opacity": 0.15
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "pe_25",
          "type": "quantitative"
        },
        "y2": {
          "field": "pe_50"
        },
        "color": {
          "value": "#8BC34A"
        }
      }
    },
    {
      "mark": {
        "type": "area",
        "opacity": 0.15
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "pe_50",
          "type": "quantitative"
        },
        "y2": {
          "field": "pe_75"
        },
        "color": {
          "value": "#FFC107"
        }
      }
    },
    {
      "mark": {
        "type": "area",
        "opacity": 0.15
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "pe_75",
          "type": "quantitative"
        },
        "y2": {
          "field": "pe_90"
        },
        "color": {
          "value": "#F44336"
        }
      }
    },
    {
      "mark": {
        "type": "line",
        "color": "#1976D2",
        "strokeWidth": 2
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "price",
          "type": "quantitative"
        },
        "tooltip": [
          {
            "field": "date",
            "type": "temporal",
            "title": "日期"
          },
          {
            "field": "price",
            "type": "quantitative",
            "title": "股價",
            "format": ".1f"
          },
          {
            "field": "pe",
            "type": "quantitative",
            "title": "本益比",
            "format": ".1f"
          },
          {
            "field": "pe_10",
            "type": "quantitative",
            "title": "PE 10% (21.6倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (24.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (30.5倍)",
            "format": ".1f"
          }
        ]
      }
    },
    {
      "mark": {
        "type": "line",
        "strokeDash": [
          4,
          4
        ],
        "opacity": 0.6,
        "strokeWidth": 1
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "pe_25",
          "type": "quantitative"
        },
        "color": {
          "value": "#4CAF50"
        }
      }
    },
    {
      "mark": {
        "type": "line",
        "strokeDash": [
          4,
          4
        ],
        "opacity": 0.6,
        "strokeWidth": 1
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "pe_50",
          "type": "quantitative"
        },
        "color": {
          "value": "#FFC107"
        }
      }
    },
    {
      "mark": {
        "type": "line",
        "strokeDash": [
          4,
          4
        ],
        "opacity": 0.6,
        "strokeWidth": 1
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal"
        },
        "y": {
          "field": "pe_75",
          "type": "quantitative"
        },
        "color": {
          "value": "#F44336"
        }
      }
    }
  ]
}
```


## 📊 月營收年增率

月營收與去年同期相比的成長率。紅色柱狀代表正成長，綠色代表衰退。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6597 立誠 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2016-09-15",
        "revenue_yoy": 60.0
      },
      {
        "date": "2016-10-16",
        "revenue_yoy": -6.46
      },
      {
        "date": "2016-11-15",
        "revenue_yoy": 18.0
      },
      {
        "date": "2016-12-16",
        "revenue_yoy": 55.5
      },
      {
        "date": "2017-01-16",
        "revenue_yoy": 26.2
      },
      {
        "date": "2017-02-14",
        "revenue_yoy": 49.0
      },
      {
        "date": "2017-03-16",
        "revenue_yoy": 56.2
      },
      {
        "date": "2017-04-15",
        "revenue_yoy": 49.7
      },
      {
        "date": "2017-05-16",
        "revenue_yoy": -9.6
      },
      {
        "date": "2017-06-15",
        "revenue_yoy": 36.7
      },
      {
        "date": "2017-07-16",
        "revenue_yoy": -9.5
      },
      {
        "date": "2017-08-16",
        "revenue_yoy": 37.3
      },
      {
        "date": "2017-09-15",
        "revenue_yoy": 42.3
      },
      {
        "date": "2017-10-16",
        "revenue_yoy": 65.6
      },
      {
        "date": "2017-11-15",
        "revenue_yoy": 39.6
      },
      {
        "date": "2017-12-16",
        "revenue_yoy": 8.1
      },
      {
        "date": "2018-01-16",
        "revenue_yoy": 28.5
      },
      {
        "date": "2018-02-14",
        "revenue_yoy": -25.2
      },
      {
        "date": "2018-03-16",
        "revenue_yoy": 13.6
      },
      {
        "date": "2018-04-15",
        "revenue_yoy": 28.3
      },
      {
        "date": "2018-05-16",
        "revenue_yoy": 63.0
      },
      {
        "date": "2018-06-15",
        "revenue_yoy": 5.99
      },
      {
        "date": "2018-07-16",
        "revenue_yoy": 37.8
      },
      {
        "date": "2018-08-16",
        "revenue_yoy": -20.9
      },
      {
        "date": "2018-09-15",
        "revenue_yoy": -25.6
      },
      {
        "date": "2018-10-16",
        "revenue_yoy": -6.9
      },
      {
        "date": "2018-11-15",
        "revenue_yoy": -8.14
      },
      {
        "date": "2018-12-16",
        "revenue_yoy": -7.22
      },
      {
        "date": "2019-01-16",
        "revenue_yoy": 1.58
      },
      {
        "date": "2019-02-14",
        "revenue_yoy": 18.2
      },
      {
        "date": "2019-03-16",
        "revenue_yoy": -7.12
      },
      {
        "date": "2019-04-15",
        "revenue_yoy": -2.55
      },
      {
        "date": "2019-05-16",
        "revenue_yoy": 17.2
      },
      {
        "date": "2019-06-15",
        "revenue_yoy": 0.48
      },
      {
        "date": "2019-07-16",
        "revenue_yoy": -1.54
      },
      {
        "date": "2019-08-16",
        "revenue_yoy": 8.92
      },
      {
        "date": "2019-09-15",
        "revenue_yoy": 4.96
      },
      {
        "date": "2019-10-16",
        "revenue_yoy": -25.0
      },
      {
        "date": "2019-11-15",
        "revenue_yoy": -8.91
      },
      {
        "date": "2019-12-16",
        "revenue_yoy": 0.8
      },
      {
        "date": "2020-01-16",
        "revenue_yoy": -16.0
      },
      {
        "date": "2020-02-15",
        "revenue_yoy": -37.4
      },
      {
        "date": "2020-03-16",
        "revenue_yoy": 4.19
      },
      {
        "date": "2020-04-15",
        "revenue_yoy": -8.05
      },
      {
        "date": "2020-05-16",
        "revenue_yoy": -17.8
      },
      {
        "date": "2020-06-15",
        "revenue_yoy": 13.8
      },
      {
        "date": "2020-07-16",
        "revenue_yoy": 9.58
      },
      {
        "date": "2020-08-16",
        "revenue_yoy": -5.0
      },
      {
        "date": "2020-09-15",
        "revenue_yoy": 14.4
      },
      {
        "date": "2020-10-16",
        "revenue_yoy": 35.0
      },
      {
        "date": "2020-11-15",
        "revenue_yoy": 56.6
      },
      {
        "date": "2020-12-16",
        "revenue_yoy": 70.7
      },
      {
        "date": "2021-01-16",
        "revenue_yoy": 26.5
      },
      {
        "date": "2021-02-14",
        "revenue_yoy": 85.5
      },
      {
        "date": "2021-03-16",
        "revenue_yoy": 26.4
      },
      {
        "date": "2021-04-15",
        "revenue_yoy": 14.8
      },
      {
        "date": "2021-05-16",
        "revenue_yoy": 54.9
      },
      {
        "date": "2021-06-15",
        "revenue_yoy": 42.9
      },
      {
        "date": "2021-07-16",
        "revenue_yoy": 42.4
      },
      {
        "date": "2021-08-16",
        "revenue_yoy": 69.5
      },
      {
        "date": "2021-09-15",
        "revenue_yoy": 21.3
      },
      {
        "date": "2021-10-16",
        "revenue_yoy": -6.68
      },
      {
        "date": "2021-11-15",
        "revenue_yoy": -47.5
      },
      {
        "date": "2021-12-16",
        "revenue_yoy": -39.7
      },
      {
        "date": "2022-01-16",
        "revenue_yoy": -36.2
      },
      {
        "date": "2022-02-14",
        "revenue_yoy": -18.9
      },
      {
        "date": "2022-03-16",
        "revenue_yoy": -33.0
      },
      {
        "date": "2022-04-15",
        "revenue_yoy": 15.5
      },
      {
        "date": "2022-05-16",
        "revenue_yoy": -12.1
      },
      {
        "date": "2022-06-15",
        "revenue_yoy": -22.5
      },
      {
        "date": "2022-07-16",
        "revenue_yoy": -23.3
      },
      {
        "date": "2022-08-16",
        "revenue_yoy": -38.7
      },
      {
        "date": "2022-09-15",
        "revenue_yoy": -11.9
      },
      {
        "date": "2022-10-16",
        "revenue_yoy": 35.8
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": 105.1
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": 38.8
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": 45.8
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": 44.5
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": -16.1
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": -25.4
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": -5.83
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": 20.9
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": 14.5
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 54.9
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 47.0
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": 49.7
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 45.2
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": 83.0
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 69.6
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 43.9
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 142.7
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 78.3
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 78.6
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 37.2
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 46.2
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 63.5
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 44.6
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 17.9
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 6.41
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": -3.94
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 5.12
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 18.2
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 9.06
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -23.1
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -32.2
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -18.7
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -19.2
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -26.4
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -14.5
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -3.4
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -17.4
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -3.02
      }
    ]
  },
  "width": 700,
  "height": 250,
  "layer": [
    {
      "mark": {
        "type": "rule",
        "color": "#9E9E9E",
        "strokeDash": [
          2,
          2
        ]
      },
      "encoding": {
        "y": {
          "datum": 0
        }
      }
    },
    {
      "mark": {
        "type": "bar",
        "opacity": 0.8
      },
      "encoding": {
        "x": {
          "field": "date",
          "type": "temporal",
          "title": "日期"
        },
        "y": {
          "field": "revenue_yoy",
          "type": "quantitative",
          "title": "營收年增率 (%)"
        },
        "color": {
          "condition": {
            "test": "datum.revenue_yoy >= 0",
            "value": "#E53935"
          },
          "value": "#43A047"
        },
        "tooltip": [
          {
            "field": "date",
            "type": "temporal",
            "title": "日期"
          },
          {
            "field": "revenue_yoy",
            "type": "quantitative",
            "title": "營收年增率",
            "format": "+.1f"
          }
        ]
      }
    }
  ]
}
```

## 📊 各期間統計摘要

| 期間 | 平均PE | 平均報酬 | R² | 最佳買點 | 最差買點 |
|:---:|:---:|:---:|:---:|:---|:---|
| 3個月 | 26.3 | -25.2% | 0.950 | 2025-09 (+32.2%) | 2025-07 (-74.6%) |
| 6個月 | 30.1 | -37.5% | 0.911 | 2025-05 (-29.3%) | 2025-07 (-44.2%) |


## 🎯 使用說明

!!! tip "如何使用互動式圖表"
    1. **選擇投資期間**: 使用圖表上方的下拉選單選擇想要分析的投資期間（3個月至10年）
    2. **查看細節**: 將滑鼠移至圖表上的點，可查看該時點的詳細資訊（日期、本益比、報酬率）
    3. **解讀趨勢**: 觀察本益比與報酬率的關係，負相關表示低PE有較高報酬機會
    4. **對比期間**: 切換不同期間觀察短期與長期投資的差異

!!! warning "風險提示"
    - 過去表現不代表未來結果
    - 本分析基於歷史數據統計，實際報酬率會受到公司基本面變化、產業趨勢、總體經濟等多重因素影響
    - 應結合財報分析、產業研究、風險評估等多維度綜合判斷

---

*本報告由 Stock Analysis System v1.9.0 自動生成*
*數據更新時間: 2026-02-07 12:44:18 CST*
