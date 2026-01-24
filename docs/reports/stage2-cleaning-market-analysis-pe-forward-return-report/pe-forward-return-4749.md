---
title: "4749 新應材 - 本益比與未來報酬率分析 (互動式)"
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
description: "4749 新應材 (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 4749 新應材 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 4749
    - **公司名稱**: 新應材
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-24 21:31:01 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "4749 新應材 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-01-16",
        "pe_ratio": 70.78,
        "forward_return": -35.04,
        "start_price": 734.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": 65.57,
        "forward_return": -23.29,
        "start_price": 680.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": 46.77,
        "forward_return": 158.42,
        "start_price": 485.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": 42.09,
        "forward_return": 445.07,
        "start_price": 436.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": 61.43,
        "forward_return": 154.51,
        "start_price": 637.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": 61.72,
        "forward_return": 280.3,
        "start_price": 640.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": 63.65,
        "forward_return": 229.18,
        "start_price": 660.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": 77.15,
        "forward_return": 31.67,
        "start_price": 800.0,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": 85.82,
        "forward_return": -5.73,
        "start_price": 890.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-01-16",
        "pe_ratio": 70.78,
        "forward_return": -17.82,
        "start_price": 734.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": 65.57,
        "forward_return": 40.65,
        "start_price": 680.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": 46.77,
        "forward_return": 185.62,
        "start_price": 485.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": 42.09,
        "forward_return": 321.04,
        "start_price": 436.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": 61.43,
        "forward_return": 74.6,
        "start_price": 637.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": 61.72,
        "forward_return": 90.1,
        "start_price": 640.0,
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

!!! note "本益比河流帶水位: 48.2倍、61.6倍、68.2倍、80.3倍、85.7倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "4749 新應材 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-01-16",
        "price": 734.0,
        "pe": 70.78,
        "pe_10": 500.22,
        "pe_25": 639.29,
        "pe_50": 706.99,
        "pe_75": 832.75,
        "pe_90": 888.67
      },
      {
        "date": "2025-02-14",
        "price": 680.0,
        "pe": 65.57,
        "pe_10": 500.24,
        "pe_25": 639.32,
        "pe_50": 707.02,
        "pe_75": 832.78,
        "pe_90": 888.71
      },
      {
        "date": "2025-03-16",
        "price": 485.0,
        "pe": 46.77,
        "pe_10": 500.2,
        "pe_25": 639.28,
        "pe_50": 706.97,
        "pe_75": 832.73,
        "pe_90": 888.65
      },
      {
        "date": "2025-04-15",
        "price": 436.5,
        "pe": 42.09,
        "pe_10": 500.24,
        "pe_25": 639.32,
        "pe_50": 707.02,
        "pe_75": 832.79,
        "pe_90": 888.71
      },
      {
        "date": "2025-05-16",
        "price": 637.0,
        "pe": 61.43,
        "pe_10": 500.18,
        "pe_25": 639.26,
        "pe_50": 706.94,
        "pe_75": 832.7,
        "pe_90": 888.62
      },
      {
        "date": "2025-06-15",
        "price": 640.0,
        "pe": 61.72,
        "pe_10": 500.18,
        "pe_25": 639.25,
        "pe_50": 706.93,
        "pe_75": 832.69,
        "pe_90": 888.61
      },
      {
        "date": "2025-07-16",
        "price": 660.0,
        "pe": 63.65,
        "pe_10": 500.17,
        "pe_25": 639.24,
        "pe_50": 706.92,
        "pe_75": 832.67,
        "pe_90": 888.59
      },
      {
        "date": "2025-08-16",
        "price": 800.0,
        "pe": 77.15,
        "pe_10": 500.18,
        "pe_25": 639.25,
        "pe_50": 706.93,
        "pe_75": 832.69,
        "pe_90": 888.61
      },
      {
        "date": "2025-09-15",
        "price": 890.0,
        "pe": 85.82,
        "pe_10": 500.23,
        "pe_25": 639.32,
        "pe_50": 707.01,
        "pe_75": 832.78,
        "pe_90": 888.7
      },
      {
        "date": "2025-10-16",
        "price": 891.0,
        "pe": 85.92,
        "pe_10": 500.21,
        "pe_25": 639.29,
        "pe_50": 706.98,
        "pe_75": 832.75,
        "pe_90": 888.67
      },
      {
        "date": "2025-11-15",
        "price": 818.0,
        "pe": 78.88,
        "pe_10": 500.22,
        "pe_25": 639.3,
        "pe_50": 706.99,
        "pe_75": 832.75,
        "pe_90": 888.67
      },
      {
        "date": "2025-12-16",
        "price": 877.0,
        "pe": 84.57,
        "pe_10": 500.21,
        "pe_25": 639.29,
        "pe_50": 706.98,
        "pe_75": 832.75,
        "pe_90": 888.67
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
            "title": "PE 10% (48.2倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (68.2倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (85.7倍)",
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
  "title": "4749 新應材 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2013-01-16",
        "revenue_yoy": 9.9
      },
      {
        "date": "2013-02-14",
        "revenue_yoy": 27.3
      },
      {
        "date": "2013-03-16",
        "revenue_yoy": 23.6
      },
      {
        "date": "2013-04-15",
        "revenue_yoy": 18.1
      },
      {
        "date": "2013-05-16",
        "revenue_yoy": 22.6
      },
      {
        "date": "2013-06-15",
        "revenue_yoy": 65.0
      },
      {
        "date": "2013-07-16",
        "revenue_yoy": 67.2
      },
      {
        "date": "2013-08-16",
        "revenue_yoy": 47.1
      },
      {
        "date": "2013-09-15",
        "revenue_yoy": 28.6
      },
      {
        "date": "2013-10-16",
        "revenue_yoy": 27.6
      },
      {
        "date": "2013-11-15",
        "revenue_yoy": 27.7
      },
      {
        "date": "2013-12-16",
        "revenue_yoy": 33.2
      },
      {
        "date": "2014-01-16",
        "revenue_yoy": 32.2
      },
      {
        "date": "2014-02-14",
        "revenue_yoy": 2.04
      },
      {
        "date": "2014-03-16",
        "revenue_yoy": 14.1
      },
      {
        "date": "2014-04-15",
        "revenue_yoy": 10.4
      },
      {
        "date": "2014-05-16",
        "revenue_yoy": -1.6
      },
      {
        "date": "2014-06-15",
        "revenue_yoy": -16.7
      },
      {
        "date": "2014-07-16",
        "revenue_yoy": 10.7
      },
      {
        "date": "2014-08-16",
        "revenue_yoy": -16.8
      },
      {
        "date": "2014-09-15",
        "revenue_yoy": 24.5
      },
      {
        "date": "2014-10-16",
        "revenue_yoy": 4.6
      },
      {
        "date": "2015-01-16",
        "revenue_yoy": -14.4
      },
      {
        "date": "2015-02-14",
        "revenue_yoy": -11.6
      },
      {
        "date": "2015-03-16",
        "revenue_yoy": -18.9
      },
      {
        "date": "2015-04-15",
        "revenue_yoy": -26.9
      },
      {
        "date": "2015-05-16",
        "revenue_yoy": -25.3
      },
      {
        "date": "2015-06-15",
        "revenue_yoy": 11.7
      },
      {
        "date": "2015-07-16",
        "revenue_yoy": -7.17
      },
      {
        "date": "2015-08-16",
        "revenue_yoy": -6.35
      },
      {
        "date": "2015-09-15",
        "revenue_yoy": -17.6
      },
      {
        "date": "2015-10-16",
        "revenue_yoy": -9.36
      },
      {
        "date": "2015-11-15",
        "revenue_yoy": 13.1
      },
      {
        "date": "2015-12-16",
        "revenue_yoy": -5.34
      },
      {
        "date": "2016-01-16",
        "revenue_yoy": -5.62
      },
      {
        "date": "2016-02-15",
        "revenue_yoy": -26.8
      },
      {
        "date": "2016-03-16",
        "revenue_yoy": -5.14
      },
      {
        "date": "2016-04-15",
        "revenue_yoy": 8.62
      },
      {
        "date": "2016-05-16",
        "revenue_yoy": 8.25
      },
      {
        "date": "2016-06-15",
        "revenue_yoy": 6.33
      },
      {
        "date": "2016-07-16",
        "revenue_yoy": -14.2
      },
      {
        "date": "2021-08-16",
        "revenue_yoy": 52.5
      },
      {
        "date": "2021-09-15",
        "revenue_yoy": 45.2
      },
      {
        "date": "2021-10-16",
        "revenue_yoy": 70.5
      },
      {
        "date": "2021-11-15",
        "revenue_yoy": 22.1
      },
      {
        "date": "2021-12-16",
        "revenue_yoy": 7.87
      },
      {
        "date": "2022-01-16",
        "revenue_yoy": 55.7
      },
      {
        "date": "2022-02-14",
        "revenue_yoy": 27.0
      },
      {
        "date": "2022-03-16",
        "revenue_yoy": 14.0
      },
      {
        "date": "2022-04-15",
        "revenue_yoy": 16.6
      },
      {
        "date": "2022-05-16",
        "revenue_yoy": 40.3
      },
      {
        "date": "2022-06-15",
        "revenue_yoy": 31.4
      },
      {
        "date": "2022-07-16",
        "revenue_yoy": 38.5
      },
      {
        "date": "2022-08-16",
        "revenue_yoy": 39.6
      },
      {
        "date": "2022-09-15",
        "revenue_yoy": 47.0
      },
      {
        "date": "2022-10-16",
        "revenue_yoy": 62.4
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": 63.3
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": 43.8
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": 36.2
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": 55.0
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": 23.3
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": 39.4
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": -3.33
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": 12.3
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": -8.78
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": -8.16
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": -6.88
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -25.5
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": -19.0
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": 9.38
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 28.6
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -6.63
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 22.0
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 47.4
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 40.6
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 41.2
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 47.1
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 48.6
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 55.9
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 67.2
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 62.2
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 41.1
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 21.3
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 58.8
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 41.0
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 37.5
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 49.6
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 18.6
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 18.1
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 22.5
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 32.3
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 30.8
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 15.5
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": 11.0
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
| 3個月 | 63.9 | +137.2% | 0.575 | 2025-04 (+445.1%) | 2025-01 (-35.0%) |
| 6個月 | 58.1 | +115.7% | 0.945 | 2025-04 (+321.0%) | 2025-01 (-17.8%) |


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
*數據更新時間: 2026-01-24 21:31:01 CST*
