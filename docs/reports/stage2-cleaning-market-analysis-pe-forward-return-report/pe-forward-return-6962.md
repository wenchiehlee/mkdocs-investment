---
title: "6962 奕力-KY - 本益比與未來報酬率分析 (互動式)"
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
description: "6962 奕力-KY (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6962 奕力-KY - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6962
    - **公司名稱**: 奕力-KY
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月, 1年
    - **報告生成時間**: 2026-01-24 21:31:38 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6962 奕力-KY - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-11-15",
        "pe_ratio": 9.8,
        "forward_return": -10.66,
        "start_price": 55.0,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-12-16",
        "pe_ratio": 9.77,
        "forward_return": -12.68,
        "start_price": 54.8,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 9.61,
        "forward_return": 32.04,
        "start_price": 52.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 11.39,
        "forward_return": -17.6,
        "start_price": 60.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 10.37,
        "forward_return": -22.38,
        "start_price": 53.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 9.72,
        "forward_return": 5.1,
        "start_price": 48.1,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 11.99,
        "forward_return": -58.91,
        "start_price": 57.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 11.59,
        "forward_return": -52.3,
        "start_price": 53.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 10.5,
        "forward_return": -5.41,
        "start_price": 46.7,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 10.23,
        "forward_return": -28.81,
        "start_price": 43.8,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 10.3,
        "forward_return": -27.76,
        "start_price": 42.4,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-11-15",
        "pe_ratio": 9.8,
        "forward_return": 8.62,
        "start_price": 55.0,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-12-16",
        "pe_ratio": 9.77,
        "forward_return": -18.4,
        "start_price": 54.8,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 9.61,
        "forward_return": -13.4,
        "start_price": 52.3,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 11.39,
        "forward_return": -42.03,
        "start_price": 60.1,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 10.37,
        "forward_return": -15.41,
        "start_price": 53.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 9.72,
        "forward_return": -0.21,
        "start_price": 48.1,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 11.99,
        "forward_return": -43.29,
        "start_price": 57.3,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 11.59,
        "forward_return": -40.92,
        "start_price": 53.5,
        "start_year": 2025
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2024-11-15",
        "pe_ratio": 9.8,
        "forward_return": -23.74,
        "start_price": 55.0,
        "start_year": 2024
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2024-12-16",
        "pe_ratio": 9.77,
        "forward_return": -25.01,
        "start_price": 54.8,
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
          "1y"
        ],
        "labels": [
          "全部期間",
          "3個月",
          "6個月",
          "1年"
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

!!! note "本益比河流帶水位: 9.7倍、9.9倍、10.4倍、11.2倍、11.6倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6962 奕力-KY - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2024-11-15",
        "price": 55.0,
        "pe": 9.8,
        "pe_10": 54.64,
        "pe_25": 55.6,
        "pe_50": 58.56,
        "pe_75": 63.1,
        "pe_90": 65.28
      },
      {
        "date": "2024-12-16",
        "price": 54.8,
        "pe": 9.77,
        "pe_10": 54.6,
        "pe_25": 55.57,
        "pe_50": 58.53,
        "pe_75": 63.06,
        "pe_90": 65.24
      },
      {
        "date": "2025-01-16",
        "price": 52.3,
        "pe": 9.61,
        "pe_10": 52.98,
        "pe_25": 53.92,
        "pe_50": 56.79,
        "pe_75": 61.18,
        "pe_90": 63.3
      },
      {
        "date": "2025-02-14",
        "price": 60.1,
        "pe": 11.39,
        "pe_10": 51.37,
        "pe_25": 52.28,
        "pe_50": 55.06,
        "pe_75": 59.32,
        "pe_90": 61.38
      },
      {
        "date": "2025-03-16",
        "price": 53.0,
        "pe": 10.37,
        "pe_10": 49.75,
        "pe_25": 50.64,
        "pe_50": 53.33,
        "pe_75": 57.46,
        "pe_90": 59.45
      },
      {
        "date": "2025-04-15",
        "price": 48.1,
        "pe": 9.72,
        "pe_10": 48.17,
        "pe_25": 49.03,
        "pe_50": 51.64,
        "pe_75": 55.63,
        "pe_90": 57.56
      },
      {
        "date": "2025-05-16",
        "price": 57.3,
        "pe": 11.99,
        "pe_10": 46.52,
        "pe_25": 47.35,
        "pe_50": 49.87,
        "pe_75": 53.73,
        "pe_90": 55.59
      },
      {
        "date": "2025-06-15",
        "price": 53.5,
        "pe": 11.59,
        "pe_10": 44.94,
        "pe_25": 45.73,
        "pe_50": 48.17,
        "pe_75": 51.9,
        "pe_90": 53.69
      },
      {
        "date": "2025-07-16",
        "price": 46.7,
        "pe": 10.5,
        "pe_10": 43.3,
        "pe_25": 44.06,
        "pe_50": 46.41,
        "pe_75": 50.0,
        "pe_90": 51.73
      },
      {
        "date": "2025-08-16",
        "price": 43.8,
        "pe": 10.23,
        "pe_10": 41.68,
        "pe_25": 42.42,
        "pe_50": 44.68,
        "pe_75": 48.14,
        "pe_90": 49.8
      },
      {
        "date": "2025-09-15",
        "price": 42.4,
        "pe": 10.3,
        "pe_10": 40.07,
        "pe_25": 40.78,
        "pe_50": 42.96,
        "pe_75": 46.28,
        "pe_90": 47.88
      },
      {
        "date": "2025-10-16",
        "price": 46.05,
        "pe": 11.65,
        "pe_10": 38.48,
        "pe_25": 39.16,
        "pe_50": 41.25,
        "pe_75": 44.44,
        "pe_90": 45.98
      },
      {
        "date": "2025-11-15",
        "price": 39.95,
        "pe": 10.55,
        "pe_10": 36.86,
        "pe_25": 37.52,
        "pe_50": 39.51,
        "pe_75": 42.57,
        "pe_90": 44.05
      },
      {
        "date": "2025-12-16",
        "price": 39.1,
        "pe": 10.8,
        "pe_10": 35.24,
        "pe_25": 35.87,
        "pe_50": 37.78,
        "pe_75": 40.7,
        "pe_90": 42.11
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
            "title": "PE 10% (9.7倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (10.4倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (11.6倍)",
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
  "title": "6962 奕力-KY - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2024-09-15",
        "revenue_yoy": -22.4
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": -11.2
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": -7.78
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": -8.02
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": -15.9
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": -7.42
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": -4.39
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -23.0
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -27.5
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": -23.7
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -29.4
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -6.23
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 0.64
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -21.0
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -10.3
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -1.44
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
| 3個月 | 10.5 | -18.1% | 0.628 | 2025-01 (+32.0%) | 2025-05 (-58.9%) |
| 6個月 | 10.5 | -20.6% | 0.793 | 2024-11 (+8.6%) | 2025-05 (-43.3%) |
| 1年 | 9.8 | -24.4% | 1.000 | 2024-11 (-23.7%) | 2024-12 (-25.0%) |


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
