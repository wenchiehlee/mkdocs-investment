---
title: "6720 久昌 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-01-24"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 半導體業
description: "6720 久昌 (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6720 久昌 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6720
    - **公司名稱**: 久昌
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-24 21:31:35 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6720 久昌 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-12-16",
        "pe_ratio": 23.56,
        "forward_return": 3.97,
        "start_price": 155.5,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 25.39,
        "forward_return": -10.79,
        "start_price": 163.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 27.88,
        "forward_return": -34.11,
        "start_price": 174.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 25.9,
        "forward_return": -44.08,
        "start_price": 157.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 27.45,
        "forward_return": -59.04,
        "start_price": 161.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 27.52,
        "forward_return": -42.12,
        "start_price": 157.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 26.79,
        "forward_return": -22.5,
        "start_price": 148.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 23.48,
        "forward_return": 13.27,
        "start_price": 125.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 25.74,
        "forward_return": -19.9,
        "start_price": 133.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 27.07,
        "forward_return": -30.05,
        "start_price": 135.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-12-16",
        "pe_ratio": 23.56,
        "forward_return": -27.23,
        "start_price": 155.5,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 25.39,
        "forward_return": -37.34,
        "start_price": 163.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 27.88,
        "forward_return": -38.29,
        "start_price": 174.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 25.9,
        "forward_return": -24.37,
        "start_price": 157.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 27.45,
        "forward_return": -31.82,
        "start_price": 161.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 27.52,
        "forward_return": -30.09,
        "start_price": 157.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 26.79,
        "forward_return": -25.97,
        "start_price": 148.0,
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

!!! note "本益比河流帶水位: 23.9倍、25.7倍、26.9倍、27.4倍、27.7倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6720 久昌 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2024-12-16",
        "price": 155.5,
        "pe": 23.56,
        "pe_10": 157.92,
        "pe_25": 169.89,
        "pe_50": 177.74,
        "pe_75": 181.17,
        "pe_90": 182.85
      },
      {
        "date": "2025-01-16",
        "price": 163.0,
        "pe": 25.39,
        "pe_10": 153.6,
        "pe_25": 165.25,
        "pe_50": 172.89,
        "pe_75": 176.22,
        "pe_90": 177.86
      },
      {
        "date": "2025-02-14",
        "price": 174.0,
        "pe": 27.88,
        "pe_10": 149.32,
        "pe_25": 160.64,
        "pe_50": 168.07,
        "pe_75": 171.32,
        "pe_90": 172.9
      },
      {
        "date": "2025-03-16",
        "price": 157.0,
        "pe": 25.9,
        "pe_10": 145.03,
        "pe_25": 156.03,
        "pe_50": 163.24,
        "pe_75": 166.4,
        "pe_90": 167.94
      },
      {
        "date": "2025-04-15",
        "price": 161.5,
        "pe": 27.45,
        "pe_10": 140.77,
        "pe_25": 151.44,
        "pe_50": 158.44,
        "pe_75": 161.5,
        "pe_90": 162.99
      },
      {
        "date": "2025-05-16",
        "price": 157.0,
        "pe": 27.52,
        "pe_10": 136.5,
        "pe_25": 146.85,
        "pe_50": 153.63,
        "pe_75": 156.6,
        "pe_90": 158.05
      },
      {
        "date": "2025-06-15",
        "price": 148.0,
        "pe": 26.79,
        "pe_10": 132.18,
        "pe_25": 142.2,
        "pe_50": 148.77,
        "pe_75": 151.65,
        "pe_90": 153.05
      },
      {
        "date": "2025-07-16",
        "price": 125.5,
        "pe": 23.48,
        "pe_10": 127.88,
        "pe_25": 137.58,
        "pe_50": 143.94,
        "pe_75": 146.72,
        "pe_90": 148.08
      },
      {
        "date": "2025-08-16",
        "price": 133.0,
        "pe": 25.74,
        "pe_10": 123.63,
        "pe_25": 133.0,
        "pe_50": 139.15,
        "pe_75": 141.84,
        "pe_90": 143.15
      },
      {
        "date": "2025-09-15",
        "price": 135.0,
        "pe": 27.07,
        "pe_10": 119.32,
        "pe_25": 128.37,
        "pe_50": 134.3,
        "pe_75": 136.9,
        "pe_90": 138.16
      },
      {
        "date": "2025-10-16",
        "price": 129.5,
        "pe": 26.93,
        "pe_10": 115.05,
        "pe_25": 123.78,
        "pe_50": 129.5,
        "pe_75": 132.0,
        "pe_90": 133.22
      },
      {
        "date": "2025-11-15",
        "price": 125.0,
        "pe": 27.0,
        "pe_10": 110.77,
        "pe_25": 119.17,
        "pe_50": 124.68,
        "pe_75": 127.08,
        "pe_90": 128.26
      },
      {
        "date": "2025-12-16",
        "price": 123.5,
        "pe": 27.75,
        "pe_10": 106.48,
        "pe_25": 114.55,
        "pe_50": 119.85,
        "pe_75": 122.16,
        "pe_90": 123.3
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
            "title": "PE 10% (23.9倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (26.9倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (27.7倍)",
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
  "title": "6720 久昌 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2018-11-15",
        "revenue_yoy": 13.0
      },
      {
        "date": "2018-12-16",
        "revenue_yoy": -4.85
      },
      {
        "date": "2019-01-16",
        "revenue_yoy": 19.6
      },
      {
        "date": "2019-02-14",
        "revenue_yoy": -8.87
      },
      {
        "date": "2019-03-16",
        "revenue_yoy": -13.7
      },
      {
        "date": "2019-04-15",
        "revenue_yoy": 7.36
      },
      {
        "date": "2019-05-16",
        "revenue_yoy": -23.0
      },
      {
        "date": "2019-06-15",
        "revenue_yoy": -2.64
      },
      {
        "date": "2019-07-16",
        "revenue_yoy": -2.8
      },
      {
        "date": "2019-08-16",
        "revenue_yoy": 10.4
      },
      {
        "date": "2019-09-15",
        "revenue_yoy": 16.0
      },
      {
        "date": "2019-10-16",
        "revenue_yoy": 35.4
      },
      {
        "date": "2019-11-15",
        "revenue_yoy": 75.0
      },
      {
        "date": "2019-12-16",
        "revenue_yoy": 130.6
      },
      {
        "date": "2020-01-16",
        "revenue_yoy": 33.3
      },
      {
        "date": "2020-02-15",
        "revenue_yoy": 45.0
      },
      {
        "date": "2020-03-16",
        "revenue_yoy": -4.02
      },
      {
        "date": "2020-04-15",
        "revenue_yoy": 31.8
      },
      {
        "date": "2020-05-16",
        "revenue_yoy": 122.4
      },
      {
        "date": "2020-06-15",
        "revenue_yoy": 104.0
      },
      {
        "date": "2020-07-16",
        "revenue_yoy": 113.5
      },
      {
        "date": "2020-08-16",
        "revenue_yoy": 115.0
      },
      {
        "date": "2020-09-15",
        "revenue_yoy": 87.5
      },
      {
        "date": "2020-10-16",
        "revenue_yoy": 84.0
      },
      {
        "date": "2020-11-15",
        "revenue_yoy": 48.5
      },
      {
        "date": "2020-12-16",
        "revenue_yoy": 64.2
      },
      {
        "date": "2021-01-16",
        "revenue_yoy": 73.8
      },
      {
        "date": "2021-02-14",
        "revenue_yoy": 83.6
      },
      {
        "date": "2021-03-16",
        "revenue_yoy": 193.2
      },
      {
        "date": "2021-04-15",
        "revenue_yoy": 93.6
      },
      {
        "date": "2021-05-16",
        "revenue_yoy": 20.8
      },
      {
        "date": "2021-06-15",
        "revenue_yoy": 13.7
      },
      {
        "date": "2021-07-16",
        "revenue_yoy": 14.8
      },
      {
        "date": "2021-08-16",
        "revenue_yoy": 1.6
      },
      {
        "date": "2021-09-15",
        "revenue_yoy": 8.87
      },
      {
        "date": "2021-10-16",
        "revenue_yoy": 0.1
      },
      {
        "date": "2021-11-15",
        "revenue_yoy": -13.7
      },
      {
        "date": "2021-12-16",
        "revenue_yoy": -16.7
      },
      {
        "date": "2022-01-16",
        "revenue_yoy": -34.2
      },
      {
        "date": "2022-02-14",
        "revenue_yoy": 1.13
      },
      {
        "date": "2022-03-16",
        "revenue_yoy": -38.0
      },
      {
        "date": "2022-04-15",
        "revenue_yoy": -41.8
      },
      {
        "date": "2022-05-16",
        "revenue_yoy": -48.8
      },
      {
        "date": "2022-06-15",
        "revenue_yoy": -41.3
      },
      {
        "date": "2022-07-16",
        "revenue_yoy": -35.0
      },
      {
        "date": "2022-08-16",
        "revenue_yoy": -23.7
      },
      {
        "date": "2022-09-15",
        "revenue_yoy": -31.5
      },
      {
        "date": "2022-10-16",
        "revenue_yoy": -30.7
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": -21.3
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": -31.4
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": -15.2
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": -8.18
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": 17.9
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": 41.6
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": 62.7
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": 44.8
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": 60.6
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 63.1
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 74.6
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": 76.8
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 78.1
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": 126.4
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 113.6
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 67.6
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 52.0
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 70.7
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 53.0
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 54.5
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 40.7
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 9.68
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 24.2
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 25.4
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 34.7
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 4.81
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 4.2
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 28.4
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 16.6
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -8.86
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -17.5
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -21.1
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -26.7
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -33.1
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -27.9
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -29.0
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -25.7
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -24.6
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
| 3個月 | 26.1 | -24.5% | 0.738 | 2025-07 (+13.3%) | 2025-04 (-59.0%) |
| 6個月 | 26.4 | -30.7% | 0.105 | 2025-03 (-24.4%) | 2025-02 (-38.3%) |


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
*數據更新時間: 2026-01-24 21:31:35 CST*
