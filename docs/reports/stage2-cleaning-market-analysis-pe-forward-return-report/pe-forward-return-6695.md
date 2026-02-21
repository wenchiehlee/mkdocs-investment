---
title: "6695 芯鼎 - 本益比與未來報酬率分析 (互動式)"
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
description: "6695 芯鼎 (半導體業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 6695 芯鼎 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 6695
    - **公司名稱**: 芯鼎
    - **產業別**: 半導體業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月, 1年, 2年, 3年
    - **報告生成時間**: 2026-02-21 12:38:55 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6695 芯鼎 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2022-11-15",
        "pe_ratio": 58.38,
        "forward_return": -19.15,
        "start_price": 46.7,
        "start_year": 2022
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2022-12-16",
        "pe_ratio": 50.0,
        "forward_return": 41.21,
        "start_price": 40.0,
        "start_year": 2022
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-01-16",
        "pe_ratio": 63.4,
        "forward_return": 20.01,
        "start_price": 42.9,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-02-14",
        "pe_ratio": 79.79,
        "forward_return": 13.51,
        "start_price": 44.15,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-03-16",
        "pe_ratio": 101.3,
        "forward_return": -7.05,
        "start_price": 43.55,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-04-15",
        "pe_ratio": 138.9,
        "forward_return": -0.94,
        "start_price": 42.6,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-05-16",
        "pe_ratio": 248.4,
        "forward_return": -40.3,
        "start_price": 45.55,
        "start_year": 2023
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2023-06-15",
        "pe_ratio": 772.5,
        "forward_return": -46.73,
        "start_price": 46.35,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2022-11-15",
        "pe_ratio": 58.38,
        "forward_return": -4.91,
        "start_price": 46.7,
        "start_year": 2022
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2022-12-16",
        "pe_ratio": 50.0,
        "forward_return": 11.01,
        "start_price": 40.0,
        "start_year": 2022
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-01-16",
        "pe_ratio": 63.4,
        "forward_return": -1.87,
        "start_price": 42.9,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-02-14",
        "pe_ratio": 79.79,
        "forward_return": -17.97,
        "start_price": 44.15,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-03-16",
        "pe_ratio": 101.3,
        "forward_return": 0.98,
        "start_price": 43.55,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-04-15",
        "pe_ratio": 138.9,
        "forward_return": 5.7,
        "start_price": 42.6,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-05-16",
        "pe_ratio": 248.4,
        "forward_return": 122.1,
        "start_price": 45.55,
        "start_year": 2023
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2023-06-15",
        "pe_ratio": 772.5,
        "forward_return": 145.57,
        "start_price": 46.35,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2022-11-15",
        "pe_ratio": 58.38,
        "forward_return": 34.5,
        "start_price": 46.7,
        "start_year": 2022
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2022-12-16",
        "pe_ratio": 50.0,
        "forward_return": 81.82,
        "start_price": 40.0,
        "start_year": 2022
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-01-16",
        "pe_ratio": 63.4,
        "forward_return": 104.76,
        "start_price": 42.9,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-02-14",
        "pe_ratio": 79.79,
        "forward_return": 89.21,
        "start_price": 44.15,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-03-16",
        "pe_ratio": 101.3,
        "forward_return": 46.15,
        "start_price": 43.55,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-04-15",
        "pe_ratio": 138.9,
        "forward_return": 27.87,
        "start_price": 42.6,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-05-16",
        "pe_ratio": 248.4,
        "forward_return": 60.11,
        "start_price": 45.55,
        "start_year": 2023
      },
      {
        "horizon": "1y",
        "horizon_label": "1年",
        "start_date": "2023-06-15",
        "pe_ratio": 772.5,
        "forward_return": 62.51,
        "start_price": 46.35,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2022-11-15",
        "pe_ratio": 58.38,
        "forward_return": 6.93,
        "start_price": 46.7,
        "start_year": 2022
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2022-12-16",
        "pe_ratio": 50.0,
        "forward_return": 28.53,
        "start_price": 40.0,
        "start_year": 2022
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-01-16",
        "pe_ratio": 63.4,
        "forward_return": 17.56,
        "start_price": 42.9,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-02-14",
        "pe_ratio": 79.79,
        "forward_return": 17.53,
        "start_price": 44.15,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-03-16",
        "pe_ratio": 101.3,
        "forward_return": 3.16,
        "start_price": 43.55,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-04-15",
        "pe_ratio": 138.9,
        "forward_return": 1.11,
        "start_price": 42.6,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-05-16",
        "pe_ratio": 248.4,
        "forward_return": -4.2,
        "start_price": 45.55,
        "start_year": 2023
      },
      {
        "horizon": "2y",
        "horizon_label": "2年",
        "start_date": "2023-06-15",
        "pe_ratio": 772.5,
        "forward_return": -3.96,
        "start_price": 46.35,
        "start_year": 2023
      },
      {
        "horizon": "3y",
        "horizon_label": "3年",
        "start_date": "2022-11-15",
        "pe_ratio": 58.38,
        "forward_return": -1.71,
        "start_price": 46.7,
        "start_year": 2022
      },
      {
        "horizon": "3y",
        "horizon_label": "3年",
        "start_date": "2022-12-16",
        "pe_ratio": 50.0,
        "forward_return": 4.31,
        "start_price": 40.0,
        "start_year": 2022
      },
      {
        "horizon": "3y",
        "horizon_label": "3年",
        "start_date": "2023-01-16",
        "pe_ratio": 63.4,
        "forward_return": -0.12,
        "start_price": 42.9,
        "start_year": 2023
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
          "1y",
          "2y",
          "3y"
        ],
        "labels": [
          "全部期間",
          "3個月",
          "6個月",
          "1年",
          "2年",
          "3年"
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

!!! note "本益比河流帶水位: 55.9倍、62.1倍、90.5倍、166.3倍、405.6倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "6695 芯鼎 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2022-11-15",
        "price": 46.7,
        "pe": 58.38,
        "pe_10": 44.69,
        "pe_25": 49.71,
        "pe_50": 72.43,
        "pe_75": 133.01,
        "pe_90": 324.48
      },
      {
        "date": "2022-12-16",
        "price": 40.0,
        "pe": 50.0,
        "pe_10": 44.69,
        "pe_25": 49.72,
        "pe_50": 72.44,
        "pe_75": 133.02,
        "pe_90": 324.5
      },
      {
        "date": "2023-01-16",
        "price": 42.9,
        "pe": 63.4,
        "pe_10": 37.8,
        "pe_25": 42.05,
        "pe_50": 61.27,
        "pe_75": 112.51,
        "pe_90": 274.47
      },
      {
        "date": "2023-02-14",
        "price": 44.15,
        "pe": 79.79,
        "pe_10": 30.91,
        "pe_25": 34.39,
        "pe_50": 50.1,
        "pe_75": 92.0,
        "pe_90": 224.45
      },
      {
        "date": "2023-03-16",
        "price": 43.55,
        "pe": 101.3,
        "pe_10": 24.02,
        "pe_25": 26.72,
        "pe_50": 38.93,
        "pe_75": 71.48,
        "pe_90": 174.38
      },
      {
        "date": "2023-04-15",
        "price": 42.6,
        "pe": 138.9,
        "pe_10": 17.13,
        "pe_25": 19.06,
        "pe_50": 27.77,
        "pe_75": 51.0,
        "pe_90": 124.4
      },
      {
        "date": "2023-05-16",
        "price": 45.55,
        "pe": 248.4,
        "pe_10": 10.24,
        "pe_25": 11.4,
        "pe_50": 16.6,
        "pe_75": 30.49,
        "pe_90": 74.38
      },
      {
        "date": "2023-06-15",
        "price": 46.35,
        "pe": 772.5,
        "pe_10": 3.35,
        "pe_25": 3.73,
        "pe_50": 5.43,
        "pe_75": 9.98,
        "pe_90": 24.34
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
            "title": "PE 10% (55.9倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (90.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (405.6倍)",
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
  "title": "6695 芯鼎 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2018-07-16",
        "revenue_yoy": 14.4
      },
      {
        "date": "2018-08-16",
        "revenue_yoy": -5.07
      },
      {
        "date": "2018-09-15",
        "revenue_yoy": -29.1
      },
      {
        "date": "2018-10-16",
        "revenue_yoy": -28.8
      },
      {
        "date": "2018-11-15",
        "revenue_yoy": -44.5
      },
      {
        "date": "2018-12-16",
        "revenue_yoy": -49.2
      },
      {
        "date": "2019-01-16",
        "revenue_yoy": -35.6
      },
      {
        "date": "2019-02-14",
        "revenue_yoy": -27.5
      },
      {
        "date": "2019-03-16",
        "revenue_yoy": -16.2
      },
      {
        "date": "2019-04-15",
        "revenue_yoy": -1.07
      },
      {
        "date": "2019-05-16",
        "revenue_yoy": 8.67
      },
      {
        "date": "2019-06-15",
        "revenue_yoy": 20.8
      },
      {
        "date": "2019-07-16",
        "revenue_yoy": 25.9
      },
      {
        "date": "2019-08-16",
        "revenue_yoy": 32.6
      },
      {
        "date": "2019-09-15",
        "revenue_yoy": 13.3
      },
      {
        "date": "2019-10-16",
        "revenue_yoy": 17.5
      },
      {
        "date": "2019-11-15",
        "revenue_yoy": 59.3
      },
      {
        "date": "2019-12-16",
        "revenue_yoy": 19.6
      },
      {
        "date": "2020-01-16",
        "revenue_yoy": -8.63
      },
      {
        "date": "2020-02-15",
        "revenue_yoy": 10.3
      },
      {
        "date": "2020-03-16",
        "revenue_yoy": 4.39
      },
      {
        "date": "2020-04-15",
        "revenue_yoy": -34.0
      },
      {
        "date": "2020-05-16",
        "revenue_yoy": -48.0
      },
      {
        "date": "2020-06-15",
        "revenue_yoy": -45.1
      },
      {
        "date": "2020-07-16",
        "revenue_yoy": -25.2
      },
      {
        "date": "2020-08-16",
        "revenue_yoy": -20.4
      },
      {
        "date": "2020-09-15",
        "revenue_yoy": 12.9
      },
      {
        "date": "2020-10-16",
        "revenue_yoy": 8.86
      },
      {
        "date": "2020-11-15",
        "revenue_yoy": -8.24
      },
      {
        "date": "2020-12-16",
        "revenue_yoy": 24.6
      },
      {
        "date": "2021-01-16",
        "revenue_yoy": 58.6
      },
      {
        "date": "2021-02-14",
        "revenue_yoy": 59.5
      },
      {
        "date": "2021-03-16",
        "revenue_yoy": 24.5
      },
      {
        "date": "2021-04-15",
        "revenue_yoy": 98.2
      },
      {
        "date": "2021-05-16",
        "revenue_yoy": 161.8
      },
      {
        "date": "2021-06-15",
        "revenue_yoy": 126.1
      },
      {
        "date": "2021-07-16",
        "revenue_yoy": 53.4
      },
      {
        "date": "2021-08-16",
        "revenue_yoy": 52.1
      },
      {
        "date": "2021-09-15",
        "revenue_yoy": 21.9
      },
      {
        "date": "2021-10-16",
        "revenue_yoy": 28.1
      },
      {
        "date": "2021-11-15",
        "revenue_yoy": 47.8
      },
      {
        "date": "2021-12-16",
        "revenue_yoy": 65.7
      },
      {
        "date": "2022-01-16",
        "revenue_yoy": 10.9
      },
      {
        "date": "2022-02-14",
        "revenue_yoy": 22.0
      },
      {
        "date": "2022-03-16",
        "revenue_yoy": 25.0
      },
      {
        "date": "2022-04-15",
        "revenue_yoy": 10.7
      },
      {
        "date": "2022-05-16",
        "revenue_yoy": 11.1
      },
      {
        "date": "2022-06-15",
        "revenue_yoy": 2.04
      },
      {
        "date": "2022-07-16",
        "revenue_yoy": -13.5
      },
      {
        "date": "2022-08-16",
        "revenue_yoy": -34.5
      },
      {
        "date": "2022-09-15",
        "revenue_yoy": -23.4
      },
      {
        "date": "2022-10-16",
        "revenue_yoy": -20.9
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": -38.6
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": -37.3
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": -16.3
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": -5.0
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": -2.48
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": -1.11
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": -23.6
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": -31.7
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": -7.14
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 25.5
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 29.4
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": 7.76
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 45.0
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": 34.8
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 25.0
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": -20.4
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": -28.6
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": -34.2
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": -24.4
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": -9.74
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": -2.61
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": -8.26
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": -15.2
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 3.58
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 5.77
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 40.1
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": -14.4
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 32.2
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 26.3
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 40.4
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 42.5
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 69.5
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 0.83
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -1.69
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -2.56
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -14.2
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 12.9
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -22.1
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 28.8
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
| 3個月 | 189.1 | +85.1% | 0.497 | 2023-10 (+1481.4%) | 2025-02 (-78.4%) |
| 6個月 | 189.1 | +20.6% | 0.737 | 2023-07 (+322.2%) | 2024-02 (-49.3%) |
| 1年 | 189.1 | +12.4% | 0.008 | 2023-01 (+104.8%) | 2024-06 (-43.3%) |
| 2年 | 189.1 | +3.5% | 0.349 | 2022-12 (+28.5%) | 2024-01 (-30.2%) |
| 3年 | 57.3 | +0.8% | 0.646 | 2022-12 (+4.3%) | 2022-11 (-1.7%) |


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
*數據更新時間: 2026-02-21 12:38:55 CST*
