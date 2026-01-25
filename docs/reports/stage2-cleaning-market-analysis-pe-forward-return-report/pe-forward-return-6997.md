---
title: "6997 博弘 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-01-25"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 數位雲端
description: "6997 博弘 (數位雲端) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6997 博弘 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6997
    - **公司名稱**: 博弘
    - **產業別**: 數位雲端
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-25 20:41:40 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6997 博弘 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2024-12-16",
        "pe_ratio": 21.19,
        "forward_return": -26.6,
        "start_price": 129.5,
        "start_year": 2024
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 21.06,
        "forward_return": -41.18,
        "start_price": 125.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 22.73,
        "forward_return": -59.26,
        "start_price": 131.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 21.47,
        "forward_return": -18.66,
        "start_price": 120.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 20.22,
        "forward_return": 9.48,
        "start_price": 109.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 20.03,
        "forward_return": -19.23,
        "start_price": 105.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 22.09,
        "forward_return": -15.02,
        "start_price": 112.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 21.85,
        "forward_return": -12.37,
        "start_price": 107.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 20.01,
        "forward_return": -10.98,
        "start_price": 94.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 22.53,
        "forward_return": -38.25,
        "start_price": 102.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2024-12-16",
        "pe_ratio": 21.19,
        "forward_return": -22.13,
        "start_price": 129.5,
        "start_year": 2024
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 21.06,
        "forward_return": -19.88,
        "start_price": 125.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 22.73,
        "forward_return": -42.42,
        "start_price": 131.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 21.47,
        "forward_return": -15.8,
        "start_price": 120.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 20.22,
        "forward_return": -1.81,
        "start_price": 109.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 20.03,
        "forward_return": -14.34,
        "start_price": 105.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 22.09,
        "forward_return": -26.64,
        "start_price": 112.0,
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

!!! note "本益比河流帶水位: 20.1倍、21.1倍、21.9倍、22.6倍、22.8倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6997 博弘 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2024-12-16",
        "price": 129.5,
        "pe": 21.19,
        "pe_10": 122.64,
        "pe_25": 128.71,
        "pe_50": 133.53,
        "pe_75": 137.87,
        "pe_90": 139.11
      },
      {
        "date": "2025-01-16",
        "price": 125.0,
        "pe": 21.06,
        "pe_10": 119.11,
        "pe_25": 125.0,
        "pe_50": 129.69,
        "pe_75": 133.9,
        "pe_90": 135.1
      },
      {
        "date": "2025-02-14",
        "price": 131.0,
        "pe": 22.73,
        "pe_10": 115.66,
        "pe_25": 121.38,
        "pe_50": 125.93,
        "pe_75": 130.02,
        "pe_90": 131.18
      },
      {
        "date": "2025-03-16",
        "price": 120.0,
        "pe": 21.47,
        "pe_10": 112.16,
        "pe_25": 117.71,
        "pe_50": 122.12,
        "pe_75": 126.09,
        "pe_90": 127.22
      },
      {
        "date": "2025-04-15",
        "price": 109.5,
        "pe": 20.22,
        "pe_10": 108.68,
        "pe_25": 114.05,
        "pe_50": 118.33,
        "pe_75": 122.17,
        "pe_90": 123.27
      },
      {
        "date": "2025-05-16",
        "price": 105.0,
        "pe": 20.03,
        "pe_10": 105.2,
        "pe_25": 110.4,
        "pe_50": 114.54,
        "pe_75": 118.26,
        "pe_90": 119.32
      },
      {
        "date": "2025-06-15",
        "price": 112.0,
        "pe": 22.09,
        "pe_10": 101.75,
        "pe_25": 106.78,
        "pe_50": 110.78,
        "pe_75": 114.38,
        "pe_90": 115.41
      },
      {
        "date": "2025-07-16",
        "price": 107.0,
        "pe": 21.85,
        "pe_10": 98.27,
        "pe_25": 103.13,
        "pe_50": 107.0,
        "pe_75": 110.48,
        "pe_90": 111.47
      },
      {
        "date": "2025-08-16",
        "price": 94.5,
        "pe": 20.01,
        "pe_10": 94.77,
        "pe_25": 99.46,
        "pe_50": 103.19,
        "pe_75": 106.54,
        "pe_90": 107.5
      },
      {
        "date": "2025-09-15",
        "price": 102.5,
        "pe": 22.53,
        "pe_10": 91.3,
        "pe_25": 95.81,
        "pe_50": 99.41,
        "pe_75": 102.64,
        "pe_90": 103.56
      },
      {
        "date": "2025-10-16",
        "price": 103.5,
        "pe": 23.65,
        "pe_10": 87.82,
        "pe_25": 92.17,
        "pe_50": 95.62,
        "pe_75": 98.73,
        "pe_90": 99.61
      },
      {
        "date": "2025-11-15",
        "price": 95.7,
        "pe": 22.77,
        "pe_10": 84.34,
        "pe_25": 88.51,
        "pe_50": 91.83,
        "pe_75": 94.82,
        "pe_90": 95.67
      },
      {
        "date": "2025-12-16",
        "price": 90.9,
        "pe": 22.56,
        "pe_10": 80.86,
        "pe_25": 84.86,
        "pe_50": 88.04,
        "pe_75": 90.9,
        "pe_90": 91.71
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
            "title": "PE 10% (20.1倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (21.9倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (22.8倍)",
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
  "title": "6997 博弘 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2023-08-16",
        "revenue_yoy": -5.43
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": -7.53
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -7.53
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": -5.11
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -0.33
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": -16.4
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -20.7
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": -20.8
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": -16.0
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": -10.1
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": -9.46
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": -12.1
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": -14.0
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": -16.8
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": -17.6
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": -17.8
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": -16.4
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 11.7
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 13.4
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 9.64
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 5.95
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -0.1
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 0.17
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 0.76
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 8.64
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 18.1
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 18.8
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 30.7
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 18.1
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
| 3個月 | 21.3 | -23.2% | 0.394 | 2025-04 (+9.5%) | 2025-02 (-59.3%) |
| 6個月 | 21.3 | -20.4% | 0.780 | 2025-04 (-1.8%) | 2025-02 (-42.4%) |


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
*數據更新時間: 2026-01-25 20:41:40 CST*
