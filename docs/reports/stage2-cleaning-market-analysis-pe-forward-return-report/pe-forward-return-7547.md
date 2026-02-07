---
title: "7547 碩網 - 本益比與未來報酬率分析 (互動式)"
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
  - 數位雲端
description: "7547 碩網 (數位雲端) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7547 碩網 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7547
    - **公司名稱**: 碩網
    - **產業別**: 數位雲端
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月
    - **報告生成時間**: 2026-02-07 12:44:37 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7547 碩網 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 40.84,
        "forward_return": -78.84,
        "start_price": 111.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 41.21,
        "forward_return": -86.8,
        "start_price": 112.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 33.0,
        "forward_return": -83.86,
        "start_price": 90.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 27.62,
        "forward_return": -70.8,
        "start_price": 75.4,
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

!!! note "本益比河流帶水位: 20.7倍、23.5倍、27.6倍、36.9倍、41.0倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7547 碩網 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-07-16",
        "price": 111.5,
        "pe": 40.84,
        "pe_10": 56.44,
        "pe_25": 64.15,
        "pe_50": 75.41,
        "pe_75": 100.8,
        "pe_90": 111.9
      },
      {
        "date": "2025-08-16",
        "price": 112.5,
        "pe": 41.21,
        "pe_10": 56.44,
        "pe_25": 64.14,
        "pe_50": 75.4,
        "pe_75": 100.79,
        "pe_90": 111.89
      },
      {
        "date": "2025-09-15",
        "price": 90.1,
        "pe": 33.0,
        "pe_10": 56.45,
        "pe_25": 64.15,
        "pe_50": 75.41,
        "pe_75": 100.8,
        "pe_90": 111.91
      },
      {
        "date": "2025-10-16",
        "price": 75.4,
        "pe": 27.62,
        "pe_10": 56.44,
        "pe_25": 64.14,
        "pe_50": 75.4,
        "pe_75": 100.79,
        "pe_90": 111.89
      },
      {
        "date": "2025-11-15",
        "price": 71.1,
        "pe": 26.04,
        "pe_10": 56.45,
        "pe_25": 64.15,
        "pe_50": 75.41,
        "pe_75": 100.81,
        "pe_90": 111.91
      },
      {
        "date": "2025-12-16",
        "price": 57.2,
        "pe": 20.95,
        "pe_10": 56.45,
        "pe_25": 64.15,
        "pe_50": 75.41,
        "pe_75": 100.8,
        "pe_90": 111.91
      },
      {
        "date": "2026-01-16",
        "price": 55.3,
        "pe": 20.26,
        "pe_10": 56.43,
        "pe_25": 64.13,
        "pe_50": 75.39,
        "pe_75": 100.77,
        "pe_90": 111.88
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
            "title": "PE 10% (20.7倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (27.6倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (41.0倍)",
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
  "title": "7547 碩網 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2020-06-15",
        "revenue_yoy": 57.1
      },
      {
        "date": "2020-07-16",
        "revenue_yoy": -52.6
      },
      {
        "date": "2020-08-16",
        "revenue_yoy": 16.4
      },
      {
        "date": "2020-09-15",
        "revenue_yoy": -8.75
      },
      {
        "date": "2020-10-16",
        "revenue_yoy": -10.4
      },
      {
        "date": "2020-11-15",
        "revenue_yoy": -47.0
      },
      {
        "date": "2020-12-16",
        "revenue_yoy": 37.4
      },
      {
        "date": "2021-01-16",
        "revenue_yoy": -66.4
      },
      {
        "date": "2021-02-14",
        "revenue_yoy": -13.3
      },
      {
        "date": "2021-03-16",
        "revenue_yoy": 84.9
      },
      {
        "date": "2021-04-15",
        "revenue_yoy": -1.26
      },
      {
        "date": "2021-05-16",
        "revenue_yoy": -3.41
      },
      {
        "date": "2021-06-15",
        "revenue_yoy": -21.8
      },
      {
        "date": "2021-07-16",
        "revenue_yoy": 68.0
      },
      {
        "date": "2021-08-16",
        "revenue_yoy": 102.4
      },
      {
        "date": "2021-09-15",
        "revenue_yoy": -7.04
      },
      {
        "date": "2021-10-16",
        "revenue_yoy": 19.7
      },
      {
        "date": "2021-11-15",
        "revenue_yoy": 59.4
      },
      {
        "date": "2021-12-16",
        "revenue_yoy": 7.12
      },
      {
        "date": "2022-01-16",
        "revenue_yoy": 112.9
      },
      {
        "date": "2022-02-14",
        "revenue_yoy": 52.0
      },
      {
        "date": "2022-03-16",
        "revenue_yoy": -39.3
      },
      {
        "date": "2022-04-15",
        "revenue_yoy": 9.48
      },
      {
        "date": "2022-05-16",
        "revenue_yoy": 13.6
      },
      {
        "date": "2022-06-15",
        "revenue_yoy": -4.37
      },
      {
        "date": "2022-07-16",
        "revenue_yoy": -20.4
      },
      {
        "date": "2022-08-16",
        "revenue_yoy": -30.5
      },
      {
        "date": "2022-09-15",
        "revenue_yoy": 29.4
      },
      {
        "date": "2022-10-16",
        "revenue_yoy": 9.15
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": -16.4
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": 13.9
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": 30.6
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": -31.5
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": 78.6
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": -13.7
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": 7.6
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": 0.51
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": 60.3
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": -33.9
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": -16.8
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": 30.9
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 27.1
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -18.5
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 15.6
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 49.1
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": -7.62
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 69.7
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 84.4
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 74.1
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 61.1
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 176.7
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 171.6
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 50.7
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 46.5
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 120.8
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 10.0
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 21.3
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 45.0
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 22.8
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 16.4
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 9.64
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 3.33
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -9.48
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 11.4
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 14.1
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -15.9
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -33.8
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
| 3個月 | 35.7 | -80.1% | 0.479 | 2025-10 (-70.8%) | 2025-08 (-86.8%) |


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
*數據更新時間: 2026-02-07 12:44:37 CST*
