---
title: "7704 明遠精密 - 本益比與未來報酬率分析 (互動式)"
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
description: "7704 明遠精密 (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7704 明遠精密 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7704
    - **公司名稱**: 明遠精密
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-24 21:31:39 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7704 明遠精密 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-12-16",
        "pe_ratio": 27.08,
        "forward_return": -62.21,
        "start_price": 78.8,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 26.81,
        "forward_return": -53.09,
        "start_price": 75.4,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 27.62,
        "forward_return": -62.75,
        "start_price": 75.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 23.69,
        "forward_return": -40.06,
        "start_price": 62.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 24.21,
        "forward_return": -46.26,
        "start_price": 61.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 24.27,
        "forward_return": -61.1,
        "start_price": 58.8,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 25.98,
        "forward_return": -53.13,
        "start_price": 60.4,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 22.45,
        "forward_return": -34.18,
        "start_price": 50.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 20.7,
        "forward_return": 31.31,
        "start_price": 44.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 23.44,
        "forward_return": 5.59,
        "start_price": 47.65,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-12-16",
        "pe_ratio": 27.08,
        "forward_return": -50.72,
        "start_price": 78.8,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 26.81,
        "forward_return": -52.28,
        "start_price": 75.4,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 27.62,
        "forward_return": -61.92,
        "start_price": 75.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 23.69,
        "forward_return": -37.09,
        "start_price": 62.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 24.21,
        "forward_return": -39.92,
        "start_price": 61.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 24.27,
        "forward_return": -22.73,
        "start_price": 58.8,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 25.98,
        "forward_return": -29.89,
        "start_price": 60.4,
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

!!! note "本益比河流帶水位: 22.6倍、23.4倍、24.2倍、26.8倍、27.5倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7704 明遠精密 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2024-12-16",
        "price": 78.8,
        "pe": 27.08,
        "pe_10": 65.8,
        "pe_25": 68.21,
        "pe_50": 70.45,
        "pe_75": 78.01,
        "pe_90": 80.06
      },
      {
        "date": "2025-01-16",
        "price": 75.4,
        "pe": 26.81,
        "pe_10": 63.59,
        "pe_25": 65.92,
        "pe_50": 68.09,
        "pe_75": 75.4,
        "pe_90": 77.37
      },
      {
        "date": "2025-02-14",
        "price": 75.0,
        "pe": 27.62,
        "pe_10": 61.4,
        "pe_25": 63.65,
        "pe_50": 65.74,
        "pe_75": 72.8,
        "pe_90": 74.71
      },
      {
        "date": "2025-03-16",
        "price": 62.0,
        "pe": 23.69,
        "pe_10": 59.18,
        "pe_25": 61.35,
        "pe_50": 63.36,
        "pe_75": 70.17,
        "pe_90": 72.0
      },
      {
        "date": "2025-04-15",
        "price": 61.0,
        "pe": 24.21,
        "pe_10": 56.97,
        "pe_25": 59.06,
        "pe_50": 61.0,
        "pe_75": 67.55,
        "pe_90": 69.32
      },
      {
        "date": "2025-05-16",
        "price": 58.8,
        "pe": 24.27,
        "pe_10": 54.78,
        "pe_25": 56.79,
        "pe_50": 58.65,
        "pe_75": 64.95,
        "pe_90": 66.65
      },
      {
        "date": "2025-06-15",
        "price": 60.4,
        "pe": 25.98,
        "pe_10": 52.57,
        "pe_25": 54.49,
        "pe_50": 56.28,
        "pe_75": 62.33,
        "pe_90": 63.96
      },
      {
        "date": "2025-07-16",
        "price": 50.0,
        "pe": 22.45,
        "pe_10": 50.36,
        "pe_25": 52.2,
        "pe_50": 53.92,
        "pe_75": 59.71,
        "pe_90": 61.27
      },
      {
        "date": "2025-08-16",
        "price": 44.1,
        "pe": 20.7,
        "pe_10": 48.17,
        "pe_25": 49.94,
        "pe_50": 51.58,
        "pe_75": 57.12,
        "pe_90": 58.61
      },
      {
        "date": "2025-09-15",
        "price": 47.65,
        "pe": 23.44,
        "pe_10": 45.97,
        "pe_25": 47.65,
        "pe_50": 49.22,
        "pe_75": 54.5,
        "pe_90": 55.93
      },
      {
        "date": "2025-10-16",
        "price": 45.0,
        "pe": 23.26,
        "pe_10": 43.75,
        "pe_25": 45.35,
        "pe_50": 46.84,
        "pe_75": 51.87,
        "pe_90": 53.23
      },
      {
        "date": "2025-11-15",
        "price": 44.2,
        "pe": 24.05,
        "pe_10": 41.56,
        "pe_25": 43.08,
        "pe_50": 44.49,
        "pe_75": 49.27,
        "pe_90": 50.56
      },
      {
        "date": "2025-12-16",
        "price": 48.3,
        "pe": 27.76,
        "pe_10": 39.34,
        "pe_25": 40.78,
        "pe_50": 42.12,
        "pe_75": 46.65,
        "pe_90": 47.87
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
            "title": "PE 10% (22.6倍)",
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
            "title": "PE 90% (27.5倍)",
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
  "title": "7704 明遠精密 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-09-15",
        "revenue_yoy": -22.1
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -18.0
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": -3.06
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -22.1
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 29.0
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 49.9
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": -6.28
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 8.95
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": -9.22
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": -19.8
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": -7.17
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 6.86
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 3.09
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 46.3
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 25.3
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": -30.5
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 10.7
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": -40.2
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 4.04
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -17.8
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 3.04
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -16.9
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -11.2
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -15.1
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -16.9
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -27.9
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -14.2
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 30.3
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
| 3個月 | 24.6 | -37.6% | 0.642 | 2025-08 (+31.3%) | 2025-02 (-62.8%) |
| 6個月 | 25.7 | -42.1% | 0.571 | 2025-05 (-22.7%) | 2025-02 (-61.9%) |


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
*數據更新時間: 2026-01-24 21:31:39 CST*
