---
title: "7709 榮田 - 本益比與未來報酬率分析 (互動式)"
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
  - 電機機械
description: "7709 榮田 (電機機械) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7709 榮田 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7709
    - **公司名稱**: 榮田
    - **產業別**: 電機機械
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-03-21 12:43:32 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7709 榮田 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 11.64,
        "forward_return": -67.59,
        "start_price": 56.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 10.23,
        "forward_return": -39.86,
        "start_price": 49.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 9.72,
        "forward_return": 3.95,
        "start_price": 41.2,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 11.63,
        "forward_return": -10.75,
        "start_price": 42.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 13.24,
        "forward_return": -6.66,
        "start_price": 40.65,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 13.97,
        "forward_return": -3.49,
        "start_price": 39.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 15.25,
        "forward_return": -8.93,
        "start_price": 39.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 16.37,
        "forward_return": 1.61,
        "start_price": 37.65,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 16.5,
        "forward_return": 578.93,
        "start_price": 38.95,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 11.64,
        "forward_return": -45.92,
        "start_price": 56.1,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 10.23,
        "forward_return": -26.23,
        "start_price": 49.3,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 9.72,
        "forward_return": 0.24,
        "start_price": 41.2,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 11.63,
        "forward_return": -9.44,
        "start_price": 42.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 13.24,
        "forward_return": -2.68,
        "start_price": 40.65,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 13.97,
        "forward_return": 155.98,
        "start_price": 39.3,
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

!!! note "本益比河流帶水位: 10.5倍、11.6倍、15.2倍、16.4倍、23.3倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7709 榮田 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-02-14",
        "price": 56.1,
        "pe": 11.64,
        "pe_10": 50.65,
        "pe_25": 56.1,
        "pe_50": 73.45,
        "pe_75": 78.9,
        "pe_90": 112.14
      },
      {
        "date": "2025-03-16",
        "price": 49.3,
        "pe": 10.23,
        "pe_10": 50.65,
        "pe_25": 56.1,
        "pe_50": 73.44,
        "pe_75": 78.89,
        "pe_90": 112.13
      },
      {
        "date": "2025-04-15",
        "price": 41.2,
        "pe": 9.72,
        "pe_10": 44.55,
        "pe_25": 49.34,
        "pe_50": 64.6,
        "pe_75": 69.39,
        "pe_90": 98.63
      },
      {
        "date": "2025-05-16",
        "price": 42.5,
        "pe": 11.63,
        "pe_10": 38.41,
        "pe_25": 42.54,
        "pe_50": 55.69,
        "pe_75": 59.82,
        "pe_90": 85.03
      },
      {
        "date": "2025-06-15",
        "price": 40.65,
        "pe": 13.24,
        "pe_10": 32.27,
        "pe_25": 35.74,
        "pe_50": 46.79,
        "pe_75": 50.26,
        "pe_90": 71.44
      },
      {
        "date": "2025-07-16",
        "price": 39.3,
        "pe": 13.97,
        "pe_10": 29.57,
        "pe_25": 32.75,
        "pe_50": 42.87,
        "pe_75": 46.05,
        "pe_90": 65.46
      },
      {
        "date": "2025-08-16",
        "price": 39.0,
        "pe": 15.25,
        "pe_10": 26.88,
        "pe_25": 29.77,
        "pe_50": 38.97,
        "pe_75": 41.86,
        "pe_90": 59.51
      },
      {
        "date": "2025-09-15",
        "price": 37.65,
        "pe": 16.37,
        "pe_10": 24.17,
        "pe_25": 26.77,
        "pe_50": 35.05,
        "pe_75": 37.65,
        "pe_90": 53.51
      },
      {
        "date": "2025-10-16",
        "price": 38.95,
        "pe": 16.5,
        "pe_10": 24.81,
        "pe_25": 27.48,
        "pe_50": 35.98,
        "pe_75": 38.64,
        "pe_90": 54.93
      },
      {
        "date": "2025-11-15",
        "price": 37.5,
        "pe": 15.5,
        "pe_10": 25.43,
        "pe_25": 28.16,
        "pe_50": 36.87,
        "pe_75": 39.6,
        "pe_90": 56.29
      },
      {
        "date": "2025-12-16",
        "price": 37.8,
        "pe": 15.24,
        "pe_10": 26.07,
        "pe_25": 28.87,
        "pe_50": 37.8,
        "pe_75": 40.6,
        "pe_90": 57.71
      },
      {
        "date": "2026-01-16",
        "price": 63.1,
        "pe": 25.44,
        "pe_10": 26.07,
        "pe_25": 28.87,
        "pe_50": 37.8,
        "pe_75": 40.6,
        "pe_90": 57.71
      },
      {
        "date": "2026-02-14",
        "price": 61.9,
        "pe": 24.96,
        "pe_10": 26.06,
        "pe_25": 28.87,
        "pe_50": 37.79,
        "pe_75": 40.6,
        "pe_90": 57.7
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
            "title": "PE 10% (10.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (15.2倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (23.3倍)",
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
  "title": "7709 榮田 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-09-15",
        "revenue_yoy": -6.36
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -64.3
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 164.1
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -40.6
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 305.3
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -32.2
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 37.9
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 244.8
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": -47.0
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": -49.8
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 47.0
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": -57.1
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 149.4
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 178.8
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": -40.9
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 48.8
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": -48.4
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 41.8
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": -30.0
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -26.6
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -51.4
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -7.03
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -22.6
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -13.7
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -69.8
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -43.6
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -23.7
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 11.9
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 20.3
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": -6.14
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
| 3個月 | 13.2 | +49.7% | 0.277 | 2025-10 (+578.9%) | 2025-02 (-67.6%) |
| 6個月 | 11.7 | +12.0% | 0.421 | 2025-07 (+156.0%) | 2025-02 (-45.9%) |


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
*數據更新時間: 2026-03-21 12:43:32 CST*
