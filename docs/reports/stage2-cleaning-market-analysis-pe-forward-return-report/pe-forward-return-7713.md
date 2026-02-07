---
title: "7713 威力德生醫 - 本益比與未來報酬率分析 (互動式)"
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
  - 生技醫療業
description: "7713 威力德生醫 (生技醫療業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7713 威力德生醫 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7713
    - **公司名稱**: 威力德生醫
    - **產業別**: 生技醫療業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-02-07 12:44:40 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7713 威力德生醫 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 15.27,
        "forward_return": -16.86,
        "start_price": 65.2,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 14.24,
        "forward_return": 41.46,
        "start_price": 60.8,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 13.16,
        "forward_return": 118.32,
        "start_price": 56.2,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 14.59,
        "forward_return": 90.37,
        "start_price": 62.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 14.29,
        "forward_return": 194.43,
        "start_price": 61.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 15.2,
        "forward_return": 72.92,
        "start_price": 64.9,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 16.37,
        "forward_return": 15.75,
        "start_price": 69.9,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 17.96,
        "forward_return": -16.18,
        "start_price": 76.7,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 17.45,
        "forward_return": -19.22,
        "start_price": 74.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 15.27,
        "forward_return": 26.38,
        "start_price": 65.2,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 14.24,
        "forward_return": 52.55,
        "start_price": 60.8,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 13.16,
        "forward_return": 91.72,
        "start_price": 56.2,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 14.59,
        "forward_return": 42.82,
        "start_price": 62.3,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 14.29,
        "forward_return": 58.23,
        "start_price": 61.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 15.2,
        "forward_return": 18.19,
        "start_price": 64.9,
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

!!! note "本益比河流帶水位: 14.2倍、14.5倍、15.8倍、17.2倍、17.4倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7713 威力德生醫 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-02-14",
        "price": 65.2,
        "pe": 15.27,
        "pe_10": 60.82,
        "pe_25": 61.98,
        "pe_50": 67.55,
        "pe_75": 73.49,
        "pe_90": 74.44
      },
      {
        "date": "2025-03-16",
        "price": 60.8,
        "pe": 14.24,
        "pe_10": 60.82,
        "pe_25": 61.97,
        "pe_50": 67.55,
        "pe_75": 73.49,
        "pe_90": 74.43
      },
      {
        "date": "2025-04-15",
        "price": 56.2,
        "pe": 13.16,
        "pe_10": 60.83,
        "pe_25": 61.99,
        "pe_50": 67.56,
        "pe_75": 73.51,
        "pe_90": 74.45
      },
      {
        "date": "2025-05-16",
        "price": 62.3,
        "pe": 14.59,
        "pe_10": 60.83,
        "pe_25": 61.98,
        "pe_50": 67.55,
        "pe_75": 73.5,
        "pe_90": 74.44
      },
      {
        "date": "2025-06-15",
        "price": 61.0,
        "pe": 14.29,
        "pe_10": 60.81,
        "pe_25": 61.96,
        "pe_50": 67.53,
        "pe_75": 73.48,
        "pe_90": 74.42
      },
      {
        "date": "2025-07-16",
        "price": 64.9,
        "pe": 15.2,
        "pe_10": 60.82,
        "pe_25": 61.98,
        "pe_50": 67.55,
        "pe_75": 73.49,
        "pe_90": 74.43
      },
      {
        "date": "2025-08-16",
        "price": 69.9,
        "pe": 16.37,
        "pe_10": 60.83,
        "pe_25": 61.98,
        "pe_50": 67.55,
        "pe_75": 73.5,
        "pe_90": 74.44
      },
      {
        "date": "2025-09-15",
        "price": 76.7,
        "pe": 17.96,
        "pe_10": 60.83,
        "pe_25": 61.99,
        "pe_50": 67.56,
        "pe_75": 73.51,
        "pe_90": 74.45
      },
      {
        "date": "2025-10-16",
        "price": 74.5,
        "pe": 17.45,
        "pe_10": 60.82,
        "pe_25": 61.97,
        "pe_50": 67.54,
        "pe_75": 73.49,
        "pe_90": 74.43
      },
      {
        "date": "2025-11-15",
        "price": 73.8,
        "pe": 17.28,
        "pe_10": 60.84,
        "pe_25": 61.99,
        "pe_50": 67.56,
        "pe_75": 73.51,
        "pe_90": 74.45
      },
      {
        "date": "2025-12-16",
        "price": 73.4,
        "pe": 17.19,
        "pe_10": 60.83,
        "pe_25": 61.98,
        "pe_50": 67.55,
        "pe_75": 73.5,
        "pe_90": 74.44
      },
      {
        "date": "2026-01-16",
        "price": 70.6,
        "pe": 16.53,
        "pe_10": 60.84,
        "pe_25": 61.99,
        "pe_50": 67.57,
        "pe_75": 73.51,
        "pe_90": 74.46
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
            "title": "PE 10% (14.2倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (15.8倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (17.4倍)",
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
  "title": "7713 威力德生醫 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-10-16",
        "revenue_yoy": -6.89
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": -3.73
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -3.22
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 13.0
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -1.12
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": -0.24
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 1.06
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 3.38
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 16.0
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 3.09
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 8.92
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": -2.88
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 5.86
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 15.2
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 1.49
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": -2.94
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 10.6
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 6.31
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 11.3
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 14.9
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 0.08
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 12.5
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 10.2
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 25.8
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 22.0
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 14.7
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 21.0
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
| 3個月 | 15.4 | +53.4% | 0.538 | 2025-06 (+194.4%) | 2025-10 (-19.2%) |
| 6個月 | 14.5 | +48.3% | 0.975 | 2025-04 (+91.7%) | 2025-07 (+18.2%) |


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
*數據更新時間: 2026-02-07 12:44:40 CST*
