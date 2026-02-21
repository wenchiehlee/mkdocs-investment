---
title: "7734 印能科技 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-02-21"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 半導體業
description: "7734 印能科技 (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7734 印能科技 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7734
    - **公司名稱**: 印能科技
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-02-21 12:39:10 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7734 印能科技 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 42.61,
        "forward_return": -67.26,
        "start_price": 1580.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 30.61,
        "forward_return": -23.75,
        "start_price": 1135.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 27.64,
        "forward_return": 4.67,
        "start_price": 1025.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 32.36,
        "forward_return": -40.76,
        "start_price": 1200.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 30.34,
        "forward_return": -11.24,
        "start_price": 1125.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 27.37,
        "forward_return": 1.97,
        "start_price": 1015.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 27.78,
        "forward_return": -19.75,
        "start_price": 1030.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 28.86,
        "forward_return": -36.11,
        "start_price": 1070.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-10-16",
        "pe_ratio": 27.51,
        "forward_return": 32.54,
        "start_price": 1020.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 42.61,
        "forward_return": -55.82,
        "start_price": 1580.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 30.61,
        "forward_return": -13.62,
        "start_price": 1135.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 27.64,
        "forward_return": 3.28,
        "start_price": 1025.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 32.36,
        "forward_return": -29.38,
        "start_price": 1200.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 30.34,
        "forward_return": -24.27,
        "start_price": 1125.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 27.37,
        "forward_return": 16.25,
        "start_price": 1015.0,
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

!!! note "本益比河流帶水位: 26.0倍、27.5倍、28.3倍、30.4倍、32.2倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7734 印能科技 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-02-14",
        "price": 1580.0,
        "pe": 42.61,
        "pe_10": 962.83,
        "pe_25": 1018.79,
        "pe_50": 1050.12,
        "pe_75": 1127.53,
        "pe_90": 1193.44
      },
      {
        "date": "2025-03-16",
        "price": 1135.0,
        "pe": 30.61,
        "pe_10": 962.8,
        "pe_25": 1018.76,
        "pe_50": 1050.09,
        "pe_75": 1127.49,
        "pe_90": 1193.4
      },
      {
        "date": "2025-04-15",
        "price": 1025.0,
        "pe": 27.64,
        "pe_10": 962.92,
        "pe_25": 1018.88,
        "pe_50": 1050.22,
        "pe_75": 1127.63,
        "pe_90": 1193.55
      },
      {
        "date": "2025-05-16",
        "price": 1200.0,
        "pe": 32.36,
        "pe_10": 962.89,
        "pe_25": 1018.85,
        "pe_50": 1050.19,
        "pe_75": 1127.6,
        "pe_90": 1193.51
      },
      {
        "date": "2025-06-15",
        "price": 1125.0,
        "pe": 30.34,
        "pe_10": 962.81,
        "pe_25": 1018.77,
        "pe_50": 1050.1,
        "pe_75": 1127.5,
        "pe_90": 1193.41
      },
      {
        "date": "2025-07-16",
        "price": 1015.0,
        "pe": 27.37,
        "pe_10": 962.93,
        "pe_25": 1018.89,
        "pe_50": 1050.23,
        "pe_75": 1127.64,
        "pe_90": 1193.56
      },
      {
        "date": "2025-08-16",
        "price": 1030.0,
        "pe": 27.78,
        "pe_10": 962.74,
        "pe_25": 1018.69,
        "pe_50": 1050.02,
        "pe_75": 1127.42,
        "pe_90": 1193.32
      },
      {
        "date": "2025-09-15",
        "price": 1070.0,
        "pe": 28.86,
        "pe_10": 962.7,
        "pe_25": 1018.65,
        "pe_50": 1049.98,
        "pe_75": 1127.37,
        "pe_90": 1193.28
      },
      {
        "date": "2025-10-16",
        "price": 1020.0,
        "pe": 27.51,
        "pe_10": 962.75,
        "pe_25": 1018.7,
        "pe_50": 1050.03,
        "pe_75": 1127.43,
        "pe_90": 1193.34
      },
      {
        "date": "2025-11-15",
        "price": 879.0,
        "pe": 23.71,
        "pe_10": 962.64,
        "pe_25": 1018.58,
        "pe_50": 1049.91,
        "pe_75": 1127.3,
        "pe_90": 1193.19
      },
      {
        "date": "2025-12-16",
        "price": 957.0,
        "pe": 25.81,
        "pe_10": 962.78,
        "pe_25": 1018.74,
        "pe_50": 1050.07,
        "pe_75": 1127.47,
        "pe_90": 1193.38
      },
      {
        "date": "2026-01-16",
        "price": 1095.0,
        "pe": 29.53,
        "pe_10": 962.84,
        "pe_25": 1018.8,
        "pe_50": 1050.13,
        "pe_75": 1127.54,
        "pe_90": 1193.45
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
            "title": "PE 10% (26.0倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (28.3倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (32.2倍)",
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
  "title": "7734 印能科技 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-12-16",
        "revenue_yoy": 26.1
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 43.0
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 265.7
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 91.6
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 6.97
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": -24.5
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 264.5
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 43.2
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 50.2
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 284.4
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 158.5
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 11.6
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 3.83
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": -4.77
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 109.8
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": -4.66
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 67.8
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -1.97
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 23.9
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 76.0
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 75.3
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 95.8
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -34.1
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 6.3
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 9.09
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 142.0
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
| 3個月 | 30.6 | -17.7% | 0.613 | 2025-10 (+32.5%) | 2025-02 (-67.3%) |
| 6個月 | 31.8 | -17.3% | 0.831 | 2025-07 (+16.2%) | 2025-02 (-55.8%) |


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
*數據更新時間: 2026-02-21 12:39:10 CST*
