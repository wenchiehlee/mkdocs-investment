---
title: "3158 嘉實 - 本益比與未來報酬率分析 (互動式)"
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
  - 資訊服務業
description: "3158 嘉實 (資訊服務業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 3158 嘉實 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 3158
    - **公司名稱**: 嘉實
    - **產業別**: 資訊服務業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月
    - **報告生成時間**: 2026-04-18 13:15:17 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "3158 嘉實 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-11-15",
        "pe_ratio": 13.66,
        "forward_return": -23.33,
        "start_price": 99.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-12-16",
        "pe_ratio": 12.75,
        "forward_return": -7.24,
        "start_price": 92.7,
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
          "0.25y"
        ],
        "labels": [
          "全部期間",
          "3個月"
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

!!! note "本益比河流帶水位: 12.4倍、12.4倍、12.5倍、12.7倍、13.2倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "3158 嘉實 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-11-15",
        "price": 99.3,
        "pe": 13.66,
        "pe_10": 89.89,
        "pe_25": 90.01,
        "pe_50": 90.54,
        "pe_75": 92.27,
        "pe_90": 95.99
      },
      {
        "date": "2025-12-16",
        "price": 92.7,
        "pe": 12.75,
        "pe_10": 89.9,
        "pe_25": 90.03,
        "pe_50": 90.56,
        "pe_75": 92.28,
        "pe_90": 96.01
      },
      {
        "date": "2026-01-16",
        "price": 89.8,
        "pe": 12.35,
        "pe_10": 89.91,
        "pe_25": 90.04,
        "pe_50": 90.56,
        "pe_75": 92.29,
        "pe_90": 96.02
      },
      {
        "date": "2026-02-14",
        "price": 90.1,
        "pe": 12.39,
        "pe_10": 89.92,
        "pe_25": 90.05,
        "pe_50": 90.57,
        "pe_75": 92.3,
        "pe_90": 96.03
      },
      {
        "date": "2026-03-16",
        "price": 91.0,
        "pe": 12.52,
        "pe_10": 89.87,
        "pe_25": 90.0,
        "pe_50": 90.53,
        "pe_75": 92.25,
        "pe_90": 95.98
      },
      {
        "date": "2026-04-15",
        "price": 90.0,
        "pe": 12.38,
        "pe_10": 89.89,
        "pe_25": 90.02,
        "pe_50": 90.55,
        "pe_75": 92.27,
        "pe_90": 96.0
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
            "title": "PE 10% (12.4倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (12.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (13.2倍)",
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
  "title": "3158 嘉實 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2022-12-16",
        "revenue_yoy": -0.8
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": -2.8
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": -7.84
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": 4.92
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": 12.0
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": 12.8
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": -13.1
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": 9.03
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 6.14
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 12.7
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -10.0
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 10.9
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -10.7
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 4.93
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 8.75
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 5.32
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 2.24
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 4.19
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 5.61
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 6.71
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 18.3
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 16.1
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 14.2
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 23.7
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 65.1
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 12.8
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 21.3
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 16.2
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 8.84
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 8.23
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 17.6
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 4.98
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 1.59
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 5.84
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 5.96
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 5.87
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -10.2
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 11.5
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": 5.3
      },
      {
        "date": "2026-03-16",
        "revenue_yoy": 21.6
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
| 3個月 | 13.2 | -15.3% | 1.000 | 2025-12 (-7.2%) | 2025-11 (-23.3%) |


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
*數據更新時間: 2026-04-18 13:15:17 CST*
