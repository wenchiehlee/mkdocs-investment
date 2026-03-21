---
title: "7734 印能科技 - 本益比與未來報酬率分析 (互動式)"
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
    - **報告生成時間**: 2026-03-21 12:43:35 CST

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
        "pe_ratio": 39.02,
        "forward_return": -67.26,
        "start_price": 1580.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 28.03,
        "forward_return": -23.75,
        "start_price": 1135.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 28.09,
        "forward_return": 4.67,
        "start_price": 1025.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 36.93,
        "forward_return": -40.76,
        "start_price": 1200.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 39.47,
        "forward_return": -11.24,
        "start_price": 1125.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 32.37,
        "forward_return": 1.97,
        "start_price": 1015.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 30.1,
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
        "pe_ratio": 28.42,
        "forward_return": 32.54,
        "start_price": 1020.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 39.02,
        "forward_return": -55.82,
        "start_price": 1580.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 28.03,
        "forward_return": -13.62,
        "start_price": 1135.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 28.09,
        "forward_return": 3.28,
        "start_price": 1025.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 36.93,
        "forward_return": -29.38,
        "start_price": 1200.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 39.47,
        "forward_return": -24.27,
        "start_price": 1125.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-07-16",
        "pe_ratio": 32.37,
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

!!! note "本益比河流帶水位: 28.0倍、28.4倍、30.1倍、36.9倍、39.4倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7734 印能科技 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-02-14",
        "price": 1580.0,
        "pe": 39.02,
        "pe_10": 1135.48,
        "pe_25": 1150.78,
        "pe_50": 1218.81,
        "pe_75": 1495.37,
        "pe_90": 1594.58
      },
      {
        "date": "2025-03-16",
        "price": 1135.0,
        "pe": 28.03,
        "pe_10": 1135.49,
        "pe_25": 1150.79,
        "pe_50": 1218.82,
        "pe_75": 1495.38,
        "pe_90": 1594.59
      },
      {
        "date": "2025-04-15",
        "price": 1025.0,
        "pe": 28.09,
        "pe_10": 1023.25,
        "pe_25": 1037.04,
        "pe_50": 1098.34,
        "pe_75": 1347.57,
        "pe_90": 1436.97
      },
      {
        "date": "2025-05-16",
        "price": 1200.0,
        "pe": 36.93,
        "pe_10": 911.19,
        "pe_25": 923.48,
        "pe_50": 978.07,
        "pe_75": 1200.0,
        "pe_90": 1279.61
      },
      {
        "date": "2025-06-15",
        "price": 1125.0,
        "pe": 39.47,
        "pe_10": 799.27,
        "pe_25": 810.05,
        "pe_50": 857.93,
        "pe_75": 1052.6,
        "pe_90": 1122.43
      },
      {
        "date": "2025-07-16",
        "price": 1015.0,
        "pe": 32.37,
        "pe_10": 879.29,
        "pe_25": 891.14,
        "pe_50": 943.82,
        "pe_75": 1157.98,
        "pe_90": 1234.81
      },
      {
        "date": "2025-08-16",
        "price": 1030.0,
        "pe": 30.1,
        "pe_10": 959.58,
        "pe_25": 972.51,
        "pe_50": 1030.0,
        "pe_75": 1263.72,
        "pe_90": 1347.55
      },
      {
        "date": "2025-09-15",
        "price": 1070.0,
        "pe": 28.86,
        "pe_10": 1039.67,
        "pe_25": 1053.69,
        "pe_50": 1115.97,
        "pe_75": 1369.2,
        "pe_90": 1460.03
      },
      {
        "date": "2025-10-16",
        "price": 1020.0,
        "pe": 28.42,
        "pe_10": 1006.43,
        "pe_25": 1020.0,
        "pe_50": 1080.3,
        "pe_75": 1325.43,
        "pe_90": 1413.36
      },
      {
        "date": "2025-11-15",
        "price": 879.0,
        "pe": 25.34,
        "pe_10": 972.73,
        "pe_25": 985.84,
        "pe_50": 1044.12,
        "pe_75": 1281.04,
        "pe_90": 1366.02
      },
      {
        "date": "2025-12-16",
        "price": 957.0,
        "pe": 28.57,
        "pe_10": 939.31,
        "pe_25": 951.98,
        "pe_50": 1008.25,
        "pe_75": 1237.03,
        "pe_90": 1319.1
      },
      {
        "date": "2026-01-16",
        "price": 1095.0,
        "pe": 32.69,
        "pe_10": 939.31,
        "pe_25": 951.97,
        "pe_50": 1008.24,
        "pe_75": 1237.03,
        "pe_90": 1319.09
      },
      {
        "date": "2026-02-14",
        "price": 1825.0,
        "pe": 54.48,
        "pe_10": 939.37,
        "pe_25": 952.03,
        "pe_50": 1008.31,
        "pe_75": 1237.1,
        "pe_90": 1319.17
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
            "title": "PE 10% (28.0倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (30.1倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (39.4倍)",
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
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": 55.6
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
| 3個月 | 32.4 | -17.7% | 0.273 | 2025-10 (+32.5%) | 2025-02 (-67.3%) |
| 6個月 | 34.0 | -17.3% | 0.488 | 2025-07 (+16.2%) | 2025-02 (-55.8%) |


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
*數據更新時間: 2026-03-21 12:43:35 CST*
