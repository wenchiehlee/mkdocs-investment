---
title: "6902 GOGOLOOK - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-03-21"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 數位雲端
description: "6902 GOGOLOOK (數位雲端) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6902 GOGOLOOK - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6902
    - **公司名稱**: GOGOLOOK
    - **產業別**: 數位雲端
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月, 1年, 2年
    - **報告生成時間**: 2026-03-21 12:43:25 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6902 GOGOLOOK - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-07-16",
        "pe_ratio": 594.6,
        "forward_return": -81.92,
        "start_price": 220.0,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-08-16",
        "pe_ratio": 456.8,
        "forward_return": 1.78,
        "start_price": 169.0,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-09-15",
        "pe_ratio": 433.8,
        "forward_return": 25.96,
        "start_price": 160.5,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-10-16",
        "pe_ratio": 476.7,
        "forward_return": 91.83,
        "start_price": 143.0,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-11-15",
        "pe_ratio": 821.7,
        "forward_return": -49.72,
        "start_price": 189.0,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-12-16",
        "pe_ratio": 1062.0,
        "forward_return": -38.68,
        "start_price": 170.0,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-01-16",
        "pe_ratio": 648.1,
        "forward_return": -36.45,
        "start_price": 168.5,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-02-15",
        "pe_ratio": 433.3,
        "forward_return": -25.43,
        "start_price": 156.0,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-03-16",
        "pe_ratio": 327.2,
        "forward_return": -5.85,
        "start_price": 150.5,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-04-15",
        "pe_ratio": 687.0,
        "forward_return": -24.12,
        "start_price": 158.0,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 662.5,
        "forward_return": -12.04,
        "start_price": 79.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 124.1,
        "forward_return": 24.05,
        "start_price": 75.3,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-07-16",
        "pe_ratio": 594.6,
        "forward_return": -41.1,
        "start_price": 220.0,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-08-16",
        "pe_ratio": 456.8,
        "forward_return": -18.03,
        "start_price": 169.0,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-09-15",
        "pe_ratio": 433.8,
        "forward_return": -12.11,
        "start_price": 160.5,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-10-16",
        "pe_ratio": 476.7,
        "forward_return": 2.41,
        "start_price": 143.0,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-11-15",
        "pe_ratio": 821.7,
        "forward_return": -41.25,
        "start_price": 189.0,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-12-16",
        "pe_ratio": 1062.0,
        "forward_return": -21.61,
        "start_price": 170.0,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-01-16",
        "pe_ratio": 648.1,
        "forward_return": -23.44,
        "start_price": 168.5,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-02-15",
        "pe_ratio": 433.3,
        "forward_return": -14.17,
        "start_price": 156.0,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-03-16",
        "pe_ratio": 327.2,
        "forward_return": -0.57,
        "start_price": 150.5,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-04-15",
        "pe_ratio": 687.0,
        "forward_return": -9.85,
        "start_price": 158.0,
        "start_year": 2024
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-07-16",
        "pe_ratio": 594.6,
        "forward_return": -32.9,
        "start_price": 220.0,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-08-16",
        "pe_ratio": 456.8,
        "forward_return": -14.47,
        "start_price": 169.0,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-09-15",
        "pe_ratio": 433.8,
        "forward_return": -4.97,
        "start_price": 160.5,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-10-16",
        "pe_ratio": 476.7,
        "forward_return": 4.88,
        "start_price": 143.0,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-11-15",
        "pe_ratio": 821.7,
        "forward_return": -22.18,
        "start_price": 189.0,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-12-16",
        "pe_ratio": 1062.0,
        "forward_return": -30.24,
        "start_price": 170.0,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2024-01-16",
        "pe_ratio": 648.1,
        "forward_return": -30.51,
        "start_price": 168.5,
        "start_year": 2024
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2024-02-15",
        "pe_ratio": 433.3,
        "forward_return": -20.33,
        "start_price": 156.0,
        "start_year": 2024
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2024-03-16",
        "pe_ratio": 327.2,
        "forward_return": -18.95,
        "start_price": 150.5,
        "start_year": 2024
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2024-04-15",
        "pe_ratio": 687.0,
        "forward_return": -38.44,
        "start_price": 158.0,
        "start_year": 2024
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-07-16",
        "pe_ratio": 594.6,
        "forward_return": -42.65,
        "start_price": 220.0,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-08-16",
        "pe_ratio": 456.8,
        "forward_return": -29.69,
        "start_price": 169.0,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-09-15",
        "pe_ratio": 433.8,
        "forward_return": -29.6,
        "start_price": 160.5,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-10-16",
        "pe_ratio": 476.7,
        "forward_return": -27.42,
        "start_price": 143.0,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-11-15",
        "pe_ratio": 821.7,
        "forward_return": -34.52,
        "start_price": 189.0,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-12-16",
        "pe_ratio": 1062.0,
        "forward_return": -32.68,
        "start_price": 170.0,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2024-01-16",
        "pe_ratio": 648.1,
        "forward_return": -31.29,
        "start_price": 168.5,
        "start_year": 2024
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
          "0.5y",
          "1y",
          "2y"
        ],
        "labels": [
          "全部期間",
          "3個月",
          "6個月",
          "1年",
          "2年"
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

!!! note "本益比河流帶水位: 49.5倍、111.6倍、445.3倍、651.7倍、754.4倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6902 GOGOLOOK - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2023-07-16",
        "price": 220.0,
        "pe": 594.6,
        "pe_10": 18.32,
        "pe_25": 41.29,
        "pe_50": 164.76,
        "pe_75": 241.13,
        "pe_90": 279.11
      },
      {
        "date": "2023-08-16",
        "price": 169.0,
        "pe": 456.8,
        "pe_10": 18.32,
        "pe_25": 41.29,
        "pe_50": 164.75,
        "pe_75": 241.11,
        "pe_90": 279.08
      },
      {
        "date": "2023-09-15",
        "price": 160.5,
        "pe": 433.8,
        "pe_10": 18.32,
        "pe_25": 41.29,
        "pe_50": 164.75,
        "pe_75": 241.12,
        "pe_90": 279.1
      },
      {
        "date": "2023-10-16",
        "price": 143.0,
        "pe": 476.7,
        "pe_10": 14.86,
        "pe_25": 33.48,
        "pe_50": 133.58,
        "pe_75": 195.5,
        "pe_90": 226.29
      },
      {
        "date": "2023-11-15",
        "price": 189.0,
        "pe": 821.7,
        "pe_10": 11.39,
        "pe_25": 25.67,
        "pe_50": 102.42,
        "pe_75": 149.9,
        "pe_90": 173.51
      },
      {
        "date": "2023-12-16",
        "price": 170.0,
        "pe": 1062.0,
        "pe_10": 7.93,
        "pe_25": 17.86,
        "pe_50": 71.28,
        "pe_75": 104.32,
        "pe_90": 120.75
      },
      {
        "date": "2024-01-16",
        "price": 168.5,
        "pe": 648.1,
        "pe_10": 12.88,
        "pe_25": 29.01,
        "pe_50": 115.77,
        "pe_75": 169.44,
        "pe_90": 196.12
      },
      {
        "date": "2024-02-15",
        "price": 156.0,
        "pe": 433.3,
        "pe_10": 17.83,
        "pe_25": 40.18,
        "pe_50": 160.32,
        "pe_75": 234.63,
        "pe_90": 271.59
      },
      {
        "date": "2024-03-16",
        "price": 150.5,
        "pe": 327.2,
        "pe_10": 22.78,
        "pe_25": 51.33,
        "pe_50": 204.82,
        "pe_75": 299.76,
        "pe_90": 346.97
      },
      {
        "date": "2024-04-15",
        "price": 158.0,
        "pe": 687.0,
        "pe_10": 11.39,
        "pe_25": 25.67,
        "pe_50": 102.41,
        "pe_75": 149.88,
        "pe_90": 173.49
      },
      {
        "date": "2025-09-15",
        "price": 79.5,
        "pe": 662.5,
        "pe_10": 5.94,
        "pe_25": 13.39,
        "pe_50": 53.44,
        "pe_75": 78.2,
        "pe_90": 90.52
      },
      {
        "date": "2025-10-16",
        "price": 75.3,
        "pe": 124.1,
        "pe_10": 30.05,
        "pe_25": 67.71,
        "pe_50": 270.19,
        "pe_75": 395.43,
        "pe_90": 457.72
      },
      {
        "date": "2025-11-15",
        "price": 81.0,
        "pe": 74.09,
        "pe_10": 54.14,
        "pe_25": 122.01,
        "pe_50": 486.83,
        "pe_75": 712.48,
        "pe_90": 824.7
      },
      {
        "date": "2025-12-16",
        "price": 77.0,
        "pe": 48.73,
        "pe_10": 78.26,
        "pe_25": 176.34,
        "pe_50": 703.63,
        "pe_75": 1029.77,
        "pe_90": 1191.98
      },
      {
        "date": "2026-01-16",
        "price": 79.5,
        "pe": 50.32,
        "pe_10": 78.24,
        "pe_25": 176.31,
        "pe_50": 703.52,
        "pe_75": 1029.61,
        "pe_90": 1191.79
      },
      {
        "date": "2026-02-14",
        "price": 75.5,
        "pe": 47.78,
        "pe_10": 78.26,
        "pe_25": 176.34,
        "pe_50": 703.64,
        "pe_75": 1029.79,
        "pe_90": 1191.99
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
            "title": "PE 10% (49.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (445.3倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (754.4倍)",
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
  "title": "6902 GOGOLOOK - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-04-15",
        "revenue_yoy": 120.0
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": 87.8
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": 74.4
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": 82.8
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 81.5
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 92.9
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": 77.0
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 43.4
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": 60.0
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 43.5
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -1.53
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 5.09
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": -14.0
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 6.58
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 20.1
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 7.98
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 13.7
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 23.7
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 6.22
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 34.1
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 10.5
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 0.44
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 17.7
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 31.0
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 41.2
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 16.4
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 13.8
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 37.2
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 22.7
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 14.9
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 36.8
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 12.2
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 18.5
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 37.4
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": 16.6
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
| 3個月 | 560.6 | -23.4% | 0.253 | 2023-10 (+91.8%) | 2023-07 (-81.9%) |
| 6個月 | 594.1 | -30.4% | 0.268 | 2025-07 (+20.7%) | 2025-02 (-63.2%) |
| 1年 | 594.1 | -32.2% | 0.276 | 2023-10 (+4.9%) | 2024-07 (-51.0%) |
| 2年 | 642.0 | -32.5% | 0.077 | 2023-10 (-27.4%) | 2023-07 (-42.6%) |


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
*數據更新時間: 2026-03-21 12:43:25 CST*
