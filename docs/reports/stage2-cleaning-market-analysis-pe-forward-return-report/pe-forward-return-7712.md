---
title: "7712 博盛半導體 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-01-25"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 半導體業
description: "7712 博盛半導體 (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7712 博盛半導體 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7712
    - **公司名稱**: 博盛半導體
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-25 20:41:43 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7712 博盛半導體 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-12-16",
        "pe_ratio": 25.98,
        "forward_return": -84.82,
        "start_price": 218.0,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 29.48,
        "forward_return": -83.96,
        "start_price": 239.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 27.1,
        "forward_return": -85.82,
        "start_price": 212.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 18.17,
        "forward_return": -40.02,
        "start_price": 137.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 18.4,
        "forward_return": -44.08,
        "start_price": 133.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 18.79,
        "forward_return": 115.77,
        "start_price": 131.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 18.01,
        "forward_return": 89.23,
        "start_price": 120.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 17.4,
        "forward_return": 5.45,
        "start_price": 111.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 25.31,
        "forward_return": -83.33,
        "start_price": 155.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 23.54,
        "forward_return": -85.35,
        "start_price": 137.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-12-16",
        "pe_ratio": 25.98,
        "forward_return": -66.53,
        "start_price": 218.0,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 29.48,
        "forward_return": -76.95,
        "start_price": 239.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 27.1,
        "forward_return": -43.86,
        "start_price": 212.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 18.17,
        "forward_return": -23.61,
        "start_price": 137.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 18.4,
        "forward_return": -23.15,
        "start_price": 133.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 18.79,
        "forward_return": -48.1,
        "start_price": 131.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 18.01,
        "forward_return": -45.14,
        "start_price": 120.5,
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

!!! note "本益比河流帶水位: 17.1倍、18.0倍、18.8倍、25.3倍、26.9倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7712 博盛半導體 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2024-12-16",
        "price": 218.0,
        "pe": 25.98,
        "pe_10": 143.79,
        "pe_25": 151.12,
        "pe_50": 157.67,
        "pe_75": 212.38,
        "pe_90": 225.52
      },
      {
        "date": "2025-01-16",
        "price": 239.0,
        "pe": 29.48,
        "pe_10": 138.92,
        "pe_25": 146.01,
        "pe_50": 152.33,
        "pe_75": 205.19,
        "pe_90": 217.89
      },
      {
        "date": "2025-02-14",
        "price": 212.0,
        "pe": 27.1,
        "pe_10": 134.05,
        "pe_25": 140.89,
        "pe_50": 146.99,
        "pe_75": 198.0,
        "pe_90": 210.25
      },
      {
        "date": "2025-03-16",
        "price": 137.0,
        "pe": 18.17,
        "pe_10": 129.2,
        "pe_25": 135.79,
        "pe_50": 141.67,
        "pe_75": 190.83,
        "pe_90": 202.64
      },
      {
        "date": "2025-04-15",
        "price": 133.5,
        "pe": 18.4,
        "pe_10": 124.33,
        "pe_25": 130.67,
        "pe_50": 136.33,
        "pe_75": 183.64,
        "pe_90": 195.0
      },
      {
        "date": "2025-05-16",
        "price": 131.0,
        "pe": 18.79,
        "pe_10": 119.47,
        "pe_25": 125.56,
        "pe_50": 131.0,
        "pe_75": 176.46,
        "pe_90": 187.37
      },
      {
        "date": "2025-06-15",
        "price": 120.5,
        "pe": 18.01,
        "pe_10": 114.65,
        "pe_25": 120.5,
        "pe_50": 125.72,
        "pe_75": 169.34,
        "pe_90": 179.82
      },
      {
        "date": "2025-07-16",
        "price": 111.5,
        "pe": 17.4,
        "pe_10": 109.81,
        "pe_25": 115.41,
        "pe_50": 120.41,
        "pe_75": 162.19,
        "pe_90": 172.22
      },
      {
        "date": "2025-08-16",
        "price": 155.0,
        "pe": 25.31,
        "pe_10": 104.94,
        "pe_25": 110.29,
        "pe_50": 115.07,
        "pe_75": 155.0,
        "pe_90": 164.59
      },
      {
        "date": "2025-09-15",
        "price": 137.5,
        "pe": 23.54,
        "pe_10": 100.09,
        "pe_25": 105.2,
        "pe_50": 109.75,
        "pe_75": 147.84,
        "pe_90": 156.99
      },
      {
        "date": "2025-10-16",
        "price": 113.0,
        "pe": 20.34,
        "pe_10": 95.2,
        "pe_25": 100.06,
        "pe_50": 104.39,
        "pe_75": 140.61,
        "pe_90": 149.31
      },
      {
        "date": "2025-11-15",
        "price": 88.3,
        "pe": 16.74,
        "pe_10": 90.39,
        "pe_25": 95.0,
        "pe_50": 99.11,
        "pe_75": 133.5,
        "pe_90": 141.77
      },
      {
        "date": "2025-12-16",
        "price": 85.2,
        "pe": 17.07,
        "pe_10": 85.53,
        "pe_25": 89.89,
        "pe_50": 93.78,
        "pe_75": 126.33,
        "pe_90": 134.14
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
            "title": "PE 10% (17.1倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (18.8倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (26.9倍)",
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
  "title": "7712 博盛半導體 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-11-15",
        "revenue_yoy": -29.8
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -36.9
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 6.71
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -14.3
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": -2.67
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 28.5
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 19.2
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 24.6
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 5.68
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 3.19
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": -13.8
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 2.42
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 3.03
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 12.1
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": -14.8
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 0.35
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 3.14
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -2.12
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 6.28
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -16.2
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -19.0
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -1.59
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -10.5
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 6.56
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -13.6
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -8.2
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
| 3個月 | 22.2 | -29.7% | 0.496 | 2025-05 (+115.8%) | 2025-02 (-85.8%) |
| 6個月 | 22.3 | -46.8% | 0.595 | 2025-04 (-23.1%) | 2025-01 (-77.0%) |


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
*數據更新時間: 2026-01-25 20:41:43 CST*
