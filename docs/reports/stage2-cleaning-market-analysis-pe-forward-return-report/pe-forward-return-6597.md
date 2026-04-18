---
title: "6597 立誠 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-04-18"
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
    - **報告生成時間**: 2026-04-18 13:18:03 CST

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
        "pe_ratio": 27.67,
        "forward_return": -37.4,
        "start_price": 76.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 28.95,
        "forward_return": -71.29,
        "start_price": 79.6,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 29.52,
        "forward_return": -74.61,
        "start_price": 79.8,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 24.47,
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
        "pe_ratio": 21.93,
        "forward_return": 22.8,
        "start_price": 56.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-11-15",
        "pe_ratio": 25.16,
        "forward_return": -26.67,
        "start_price": 64.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-12-16",
        "pe_ratio": 23.71,
        "forward_return": -11.1,
        "start_price": 59.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 27.67,
        "forward_return": -29.26,
        "start_price": 76.1,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 28.95,
        "forward_return": -39.01,
        "start_price": 79.6,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 29.52,
        "forward_return": -44.16,
        "start_price": 79.8,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-08-16",
        "pe_ratio": 24.47,
        "forward_return": -18.31,
        "start_price": 65.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-09-15",
        "pe_ratio": 21.26,
        "forward_return": 8.54,
        "start_price": 55.5,
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

!!! note "本益比河流帶水位: 22.0倍、23.5倍、24.2倍、26.2倍、28.8倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6597 立誠 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-05-16",
        "price": 76.1,
        "pe": 27.67,
        "pe_10": 60.62,
        "pe_25": 64.74,
        "pe_50": 66.57,
        "pe_75": 72.04,
        "pe_90": 79.27
      },
      {
        "date": "2025-06-15",
        "price": 79.6,
        "pe": 28.95,
        "pe_10": 60.6,
        "pe_25": 64.72,
        "pe_50": 66.55,
        "pe_75": 72.02,
        "pe_90": 79.25
      },
      {
        "date": "2025-07-16",
        "price": 79.8,
        "pe": 29.52,
        "pe_10": 59.58,
        "pe_25": 63.63,
        "pe_50": 65.43,
        "pe_75": 70.8,
        "pe_90": 77.91
      },
      {
        "date": "2025-08-16",
        "price": 65.0,
        "pe": 24.47,
        "pe_10": 58.55,
        "pe_25": 62.53,
        "pe_50": 64.3,
        "pe_75": 69.58,
        "pe_90": 76.56
      },
      {
        "date": "2025-09-15",
        "price": 55.5,
        "pe": 21.26,
        "pe_10": 57.54,
        "pe_25": 61.45,
        "pe_50": 63.19,
        "pe_75": 68.38,
        "pe_90": 75.24
      },
      {
        "date": "2025-10-16",
        "price": 56.5,
        "pe": 21.93,
        "pe_10": 56.78,
        "pe_25": 60.65,
        "pe_50": 62.36,
        "pe_75": 67.48,
        "pe_90": 74.26
      },
      {
        "date": "2025-11-15",
        "price": 64.0,
        "pe": 25.16,
        "pe_10": 56.06,
        "pe_25": 59.88,
        "pe_50": 61.57,
        "pe_75": 66.63,
        "pe_90": 73.32
      },
      {
        "date": "2025-12-16",
        "price": 59.5,
        "pe": 23.71,
        "pe_10": 55.31,
        "pe_25": 59.07,
        "pe_50": 60.74,
        "pe_75": 65.73,
        "pe_90": 72.33
      },
      {
        "date": "2026-01-16",
        "price": 59.5,
        "pe": 23.71,
        "pe_10": 55.31,
        "pe_25": 59.07,
        "pe_50": 60.74,
        "pe_75": 65.73,
        "pe_90": 72.33
      },
      {
        "date": "2026-02-14",
        "price": 64.5,
        "pe": 25.7,
        "pe_10": 55.31,
        "pe_25": 59.08,
        "pe_50": 60.75,
        "pe_75": 65.74,
        "pe_90": 72.34
      },
      {
        "date": "2026-03-16",
        "price": 57.8,
        "pe": 23.03,
        "pe_10": 55.32,
        "pe_25": 59.08,
        "pe_50": 60.75,
        "pe_75": 65.74,
        "pe_90": 72.34
      },
      {
        "date": "2026-04-15",
        "price": 60.1,
        "pe": 23.94,
        "pe_10": 55.33,
        "pe_25": 59.1,
        "pe_50": 60.77,
        "pe_75": 65.75,
        "pe_90": 72.36
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
            "title": "PE 10% (22.0倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (24.2倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (28.8倍)",
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
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": -21.2
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": -40.6
      },
      {
        "date": "2026-03-16",
        "revenue_yoy": -6.91
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
| 3個月 | 25.3 | -23.7% | 0.955 | 2025-09 (+32.2%) | 2025-07 (-74.6%) |
| 6個月 | 26.4 | -24.4% | 0.975 | 2025-09 (+8.5%) | 2025-07 (-44.2%) |


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
*數據更新時間: 2026-04-18 13:18:03 CST*
