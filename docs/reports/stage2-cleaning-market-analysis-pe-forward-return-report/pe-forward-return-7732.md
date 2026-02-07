---
title: "7732 金興精密 - 本益比與未來報酬率分析 (互動式)"
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
  - 汽車工業
description: "7732 金興精密 (汽車工業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7732 金興精密 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7732
    - **公司名稱**: 金興精密
    - **產業別**: 汽車工業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-02-07 12:44:41 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7732 金興精密 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 22.66,
        "forward_return": -7.17,
        "start_price": 43.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 22.76,
        "forward_return": -11.11,
        "start_price": 43.7,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 20.18,
        "forward_return": 9.97,
        "start_price": 38.75,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 21.8,
        "forward_return": -16.6,
        "start_price": 41.85,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 22.11,
        "forward_return": -32.14,
        "start_price": 42.45,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 21.28,
        "forward_return": -17.23,
        "start_price": 40.85,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 19.79,
        "forward_return": -21.52,
        "start_price": 38.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 19.01,
        "forward_return": 33.52,
        "start_price": 36.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 19.24,
        "forward_return": 40.27,
        "start_price": 36.95,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 18.62,
        "forward_return": 9.78,
        "start_price": 35.75,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 22.66,
        "forward_return": -15.57,
        "start_price": 43.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 22.76,
        "forward_return": -22.45,
        "start_price": 43.7,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 20.18,
        "forward_return": -4.36,
        "start_price": 38.75,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 21.8,
        "forward_return": -18.6,
        "start_price": 41.85,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 22.11,
        "forward_return": -1.0,
        "start_price": 42.45,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 21.28,
        "forward_return": 6.7,
        "start_price": 40.85,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 19.79,
        "forward_return": -7.18,
        "start_price": 38.0,
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

!!! note "本益比河流帶水位: 19.0倍、19.2倍、20.5倍、21.8倍、22.6倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7732 金興精密 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-01-16",
        "price": 43.5,
        "pe": 22.66,
        "pe_10": 36.51,
        "pe_25": 36.93,
        "pe_50": 39.33,
        "pe_75": 41.85,
        "pe_90": 43.29
      },
      {
        "date": "2025-02-14",
        "price": 43.7,
        "pe": 22.76,
        "pe_10": 36.52,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.86,
        "pe_90": 43.3
      },
      {
        "date": "2025-03-16",
        "price": 38.75,
        "pe": 20.18,
        "pe_10": 36.52,
        "pe_25": 36.94,
        "pe_50": 39.35,
        "pe_75": 41.86,
        "pe_90": 43.3
      },
      {
        "date": "2025-04-15",
        "price": 41.85,
        "pe": 21.8,
        "pe_10": 36.51,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.85,
        "pe_90": 43.29
      },
      {
        "date": "2025-05-16",
        "price": 42.45,
        "pe": 22.11,
        "pe_10": 36.52,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.85,
        "pe_90": 43.29
      },
      {
        "date": "2025-06-15",
        "price": 40.85,
        "pe": 21.28,
        "pe_10": 36.51,
        "pe_25": 36.93,
        "pe_50": 39.33,
        "pe_75": 41.85,
        "pe_90": 43.29
      },
      {
        "date": "2025-07-16",
        "price": 38.0,
        "pe": 19.79,
        "pe_10": 36.52,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.86,
        "pe_90": 43.3
      },
      {
        "date": "2025-08-16",
        "price": 36.5,
        "pe": 19.01,
        "pe_10": 36.52,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.86,
        "pe_90": 43.3
      },
      {
        "date": "2025-09-15",
        "price": 36.95,
        "pe": 19.24,
        "pe_10": 36.53,
        "pe_25": 36.95,
        "pe_50": 39.35,
        "pe_75": 41.87,
        "pe_90": 43.31
      },
      {
        "date": "2025-10-16",
        "price": 35.75,
        "pe": 18.62,
        "pe_10": 36.52,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.86,
        "pe_90": 43.3
      },
      {
        "date": "2025-11-15",
        "price": 39.35,
        "pe": 20.49,
        "pe_10": 36.53,
        "pe_25": 36.95,
        "pe_50": 39.35,
        "pe_75": 41.87,
        "pe_90": 43.31
      },
      {
        "date": "2025-12-16",
        "price": 40.2,
        "pe": 20.94,
        "pe_10": 36.51,
        "pe_25": 36.94,
        "pe_50": 39.34,
        "pe_75": 41.85,
        "pe_90": 43.29
      },
      {
        "date": "2026-01-16",
        "price": 36.6,
        "pe": 19.06,
        "pe_10": 36.52,
        "pe_25": 36.95,
        "pe_50": 39.35,
        "pe_75": 41.86,
        "pe_90": 43.3
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
            "title": "PE 10% (19.0倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (20.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (22.6倍)",
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
  "title": "7732 金興精密 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-12-16",
        "revenue_yoy": 59.0
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 11.8
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 8.56
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 17.3
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 44.2
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": -8.22
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": -1.17
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": -39.8
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 4.09
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 15.8
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": -1.86
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 25.2
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 5.17
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 36.4
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 14.6
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 0.66
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -5.65
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -11.5
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -1.48
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 15.6
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -0.61
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 18.4
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 2.43
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -6.91
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -26.8
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
| 3個月 | 20.8 | -1.2% | 0.470 | 2025-09 (+40.3%) | 2025-05 (-32.1%) |
| 6個月 | 21.5 | -8.9% | 0.235 | 2025-06 (+6.7%) | 2025-02 (-22.4%) |


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
*數據更新時間: 2026-02-07 12:44:41 CST*
