---
title: "6925 意藍 - 本益比與未來報酬率分析 (互動式)"
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
  - 數位雲端
description: "6925 意藍 (數位雲端) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6925 意藍 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6925
    - **公司名稱**: 意藍
    - **產業別**: 數位雲端
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-24 21:31:38 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6925 意藍 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 36.06,
        "forward_return": 265.94,
        "start_price": 103.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 58.19,
        "forward_return": -56.39,
        "start_price": 167.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 54.01,
        "forward_return": -74.37,
        "start_price": 155.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 49.3,
        "forward_return": -75.63,
        "start_price": 141.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 46.52,
        "forward_return": -80.97,
        "start_price": 133.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 36.06,
        "forward_return": -20.77,
        "start_price": 103.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 58.19,
        "forward_return": -70.69,
        "start_price": 167.0,
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

!!! note "本益比河流帶水位: 33.8倍、35.8倍、42.4倍、50.5倍、55.3倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6925 意藍 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-05-16",
        "price": 103.5,
        "pe": 36.06,
        "pe_10": 96.86,
        "pe_25": 102.75,
        "pe_50": 121.77,
        "pe_75": 144.88,
        "pe_90": 158.62
      },
      {
        "date": "2025-06-15",
        "price": 167.0,
        "pe": 58.19,
        "pe_10": 96.85,
        "pe_25": 102.74,
        "pe_50": 121.76,
        "pe_75": 144.87,
        "pe_90": 158.6
      },
      {
        "date": "2025-07-16",
        "price": 155.0,
        "pe": 54.01,
        "pe_10": 96.84,
        "pe_25": 102.74,
        "pe_50": 121.75,
        "pe_75": 144.86,
        "pe_90": 158.6
      },
      {
        "date": "2025-08-16",
        "price": 141.5,
        "pe": 49.3,
        "pe_10": 96.85,
        "pe_25": 102.75,
        "pe_50": 121.77,
        "pe_75": 144.88,
        "pe_90": 158.62
      },
      {
        "date": "2025-09-15",
        "price": 133.5,
        "pe": 46.52,
        "pe_10": 96.84,
        "pe_25": 102.74,
        "pe_50": 121.75,
        "pe_75": 144.86,
        "pe_90": 158.59
      },
      {
        "date": "2025-10-16",
        "price": 110.0,
        "pe": 38.33,
        "pe_10": 96.84,
        "pe_25": 102.74,
        "pe_50": 121.75,
        "pe_75": 144.86,
        "pe_90": 158.6
      },
      {
        "date": "2025-11-15",
        "price": 100.5,
        "pe": 35.02,
        "pe_10": 96.84,
        "pe_25": 102.74,
        "pe_50": 121.75,
        "pe_75": 144.86,
        "pe_90": 158.6
      },
      {
        "date": "2025-12-16",
        "price": 88.3,
        "pe": 30.77,
        "pe_10": 96.84,
        "pe_25": 102.73,
        "pe_50": 121.75,
        "pe_75": 144.85,
        "pe_90": 158.59
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
            "title": "PE 10% (33.8倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (42.4倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (55.3倍)",
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
  "title": "6925 意藍 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2022-10-16",
        "revenue_yoy": 3.09
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": 26.5
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": 26.9
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": 6.0
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": 13.3
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": -11.6
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": -4.98
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": -0.45
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": 11.8
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": -5.89
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 22.2
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 4.63
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -13.1
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": -8.65
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -15.7
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 8.77
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 4.07
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 7.32
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 2.12
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 31.8
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 2.84
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 10.2
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": -0.56
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 45.8
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 17.7
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 12.2
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": -2.78
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 12.1
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 16.3
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 7.3
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 15.1
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -0.93
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 16.6
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 16.8
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 11.2
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 0.76
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 23.4
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 32.7
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 25.1
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
| 3個月 | 48.8 | -4.3% | 0.667 | 2025-05 (+265.9%) | 2025-09 (-81.0%) |
| 6個月 | 47.1 | -45.7% | 1.000 | 2025-05 (-20.8%) | 2025-06 (-70.7%) |


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
*數據更新時間: 2026-01-24 21:31:38 CST*
