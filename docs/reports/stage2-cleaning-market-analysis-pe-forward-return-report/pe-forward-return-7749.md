---
title: "7749 意騰-KY - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-04-04"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 半導體業
description: "7749 意騰-KY (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7749 意騰-KY - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7749
    - **公司名稱**: 意騰-KY
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-04-04 12:51:04 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7749 意騰-KY - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 77.1,
        "forward_return": -62.0,
        "start_price": 660.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 55.07,
        "forward_return": -29.55,
        "start_price": 527.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 59.45,
        "forward_return": -68.64,
        "start_price": 629.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 44.18,
        "forward_return": -51.74,
        "start_price": 512.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 41.42,
        "forward_return": -51.79,
        "start_price": 482.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-11-15",
        "pe_ratio": 38.0,
        "forward_return": -49.51,
        "start_price": 445.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-12-16",
        "pe_ratio": 36.28,
        "forward_return": -52.47,
        "start_price": 427.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 77.1,
        "forward_return": -57.03,
        "start_price": 660.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 55.07,
        "forward_return": -41.72,
        "start_price": 527.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-08-16",
        "pe_ratio": 59.45,
        "forward_return": -62.58,
        "start_price": 629.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-09-15",
        "pe_ratio": 44.18,
        "forward_return": -52.1,
        "start_price": 512.0,
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

!!! note "本益比河流帶水位: 33.7倍、36.7倍、40.1倍、52.4倍、61.2倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7749 意騰-KY - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-06-15",
        "price": 660.0,
        "pe": 77.1,
        "pe_10": 288.65,
        "pe_25": 314.25,
        "pe_50": 343.48,
        "pe_75": 448.11,
        "pe_90": 524.02
      },
      {
        "date": "2025-07-16",
        "price": 527.0,
        "pe": 55.07,
        "pe_10": 322.68,
        "pe_25": 351.3,
        "pe_50": 383.98,
        "pe_75": 500.95,
        "pe_90": 585.81
      },
      {
        "date": "2025-08-16",
        "price": 629.0,
        "pe": 59.45,
        "pe_10": 356.76,
        "pe_25": 388.4,
        "pe_50": 424.54,
        "pe_75": 553.85,
        "pe_90": 647.67
      },
      {
        "date": "2025-09-15",
        "price": 512.0,
        "pe": 44.18,
        "pe_10": 390.77,
        "pe_25": 425.43,
        "pe_50": 465.01,
        "pe_75": 606.65,
        "pe_90": 709.42
      },
      {
        "date": "2025-10-16",
        "price": 482.5,
        "pe": 41.42,
        "pe_10": 392.79,
        "pe_25": 427.63,
        "pe_50": 467.41,
        "pe_75": 609.79,
        "pe_90": 713.09
      },
      {
        "date": "2025-11-15",
        "price": 445.0,
        "pe": 38.0,
        "pe_10": 394.87,
        "pe_25": 429.89,
        "pe_50": 469.88,
        "pe_75": 613.02,
        "pe_90": 716.86
      },
      {
        "date": "2025-12-16",
        "price": 427.0,
        "pe": 36.28,
        "pe_10": 396.86,
        "pe_25": 432.06,
        "pe_50": 472.25,
        "pe_75": 616.11,
        "pe_90": 720.47
      },
      {
        "date": "2026-01-16",
        "price": 401.5,
        "pe": 34.11,
        "pe_10": 396.9,
        "pe_25": 432.1,
        "pe_50": 472.3,
        "pe_75": 616.17,
        "pe_90": 720.55
      },
      {
        "date": "2026-02-14",
        "price": 457.0,
        "pe": 38.83,
        "pe_10": 396.85,
        "pe_25": 432.05,
        "pe_50": 472.24,
        "pe_75": 616.09,
        "pe_90": 720.45
      },
      {
        "date": "2026-03-16",
        "price": 355.5,
        "pe": 30.2,
        "pe_10": 396.92,
        "pe_25": 432.13,
        "pe_50": 472.33,
        "pe_75": 616.21,
        "pe_90": 720.59
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
            "title": "PE 10% (33.7倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (40.1倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (61.2倍)",
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
  "title": "7749 意騰-KY - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2025-04-15",
        "revenue_yoy": 155.7
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 120.5
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 32.7
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 85.6
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 87.3
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 100.9
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 62.2
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 60.0
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 17.2
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 42.6
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": 74.8
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
| 3個月 | 50.2 | -52.2% | 0.102 | 2025-07 (-29.6%) | 2025-08 (-68.6%) |
| 6個月 | 59.0 | -53.4% | 0.137 | 2025-07 (-41.7%) | 2025-08 (-62.6%) |


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
*數據更新時間: 2026-04-04 12:51:04 CST*
