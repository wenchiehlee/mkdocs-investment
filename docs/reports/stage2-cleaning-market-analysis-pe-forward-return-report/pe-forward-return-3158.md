---
title: "3158 嘉實 - 本益比與未來報酬率分析 (互動式)"
authors:
  - Stock Analysis System
date: "2026-05-16"
categories:
  - 市場分析
  - 估值分析
tags:
  - 台股
  - 本益比
  - 未來報酬
  - 互動式圖表
  - 資訊服務業
description: "3158 嘉實 (資訊服務業) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 3158 嘉實 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 3158
    - **公司名稱**: 嘉實
    - **產業別**: 資訊服務業
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月
    - **報告生成時間**: 2026-05-16 13:53:46 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "3158 嘉實 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-11-15",
        "pe_ratio": 13.66,
        "forward_return": -23.33,
        "start_price": 99.3,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-12-16",
        "pe_ratio": 12.75,
        "forward_return": -7.24,
        "start_price": 92.7,
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

!!! note "本益比河流帶水位: 12.4倍、12.4倍、12.5倍、12.7倍、13.2倍"

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "3158 嘉實 - 本益比河流帶",
  "data": {
    "values": [
      {
        "date": "2025-11-15",
        "price": 99.3,
        "pe": 13.66,
        "pe_10": 89.92,
        "pe_25": 90.07,
        "pe_50": 90.54,
        "pe_75": 92.27,
        "pe_90": 95.99
      },
      {
        "date": "2025-12-16",
        "price": 92.7,
        "pe": 12.75,
        "pe_10": 89.94,
        "pe_25": 90.08,
        "pe_50": 90.56,
        "pe_75": 92.28,
        "pe_90": 96.01
      },
      {
        "date": "2026-01-16",
        "price": 89.8,
        "pe": 12.35,
        "pe_10": 89.95,
        "pe_25": 90.09,
        "pe_50": 90.56,
        "pe_75": 92.29,
        "pe_90": 96.02
      },
      {
        "date": "2026-02-14",
        "price": 90.1,
        "pe": 12.39,
        "pe_10": 89.95,
        "pe_25": 90.1,
        "pe_50": 90.57,
        "pe_75": 92.3,
        "pe_90": 96.03
      },
      {
        "date": "2026-03-16",
        "price": 91.0,
        "pe": 12.52,
        "pe_10": 89.91,
        "pe_25": 90.06,
        "pe_50": 90.53,
        "pe_75": 92.25,
        "pe_90": 95.98
      },
      {
        "date": "2026-04-15",
        "price": 90.1,
        "pe": 12.39,
        "pe_10": 89.95,
        "pe_25": 90.1,
        "pe_50": 90.57,
        "pe_75": 92.3,
        "pe_90": 96.03
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
            "title": "PE 10% (12.4倍)",
            "format": ".1f"
          },
          {
            "field": "pe_50",
            "type": "quantitative",
            "title": "PE 50% (12.5倍)",
            "format": ".1f"
          },
          {
            "field": "pe_90",
            "type": "quantitative",
            "title": "PE 90% (13.2倍)",
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
  "title": "3158 嘉實 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2013-01-16",
        "revenue_yoy": -15.9
      },
      {
        "date": "2013-02-14",
        "revenue_yoy": 6.0
      },
      {
        "date": "2013-03-16",
        "revenue_yoy": -1.47
      },
      {
        "date": "2013-04-15",
        "revenue_yoy": -13.0
      },
      {
        "date": "2013-05-16",
        "revenue_yoy": -1.92
      },
      {
        "date": "2013-06-15",
        "revenue_yoy": 8.5
      },
      {
        "date": "2013-07-16",
        "revenue_yoy": -16.0
      },
      {
        "date": "2013-08-16",
        "revenue_yoy": 23.4
      },
      {
        "date": "2013-09-15",
        "revenue_yoy": 0.1
      },
      {
        "date": "2013-10-16",
        "revenue_yoy": 31.0
      },
      {
        "date": "2013-11-15",
        "revenue_yoy": -10.1
      },
      {
        "date": "2013-12-16",
        "revenue_yoy": -4.92
      },
      {
        "date": "2014-01-16",
        "revenue_yoy": 11.5
      },
      {
        "date": "2014-02-14",
        "revenue_yoy": -13.9
      },
      {
        "date": "2014-03-16",
        "revenue_yoy": 7.87
      },
      {
        "date": "2014-04-15",
        "revenue_yoy": 6.05
      },
      {
        "date": "2014-05-16",
        "revenue_yoy": 6.37
      },
      {
        "date": "2014-06-15",
        "revenue_yoy": 14.8
      },
      {
        "date": "2014-07-16",
        "revenue_yoy": 9.59
      },
      {
        "date": "2014-08-16",
        "revenue_yoy": -22.4
      },
      {
        "date": "2014-09-15",
        "revenue_yoy": 16.3
      },
      {
        "date": "2014-10-16",
        "revenue_yoy": -18.7
      },
      {
        "date": "2015-01-16",
        "revenue_yoy": -13.1
      },
      {
        "date": "2015-02-14",
        "revenue_yoy": -1.33
      },
      {
        "date": "2015-03-16",
        "revenue_yoy": 15.1
      },
      {
        "date": "2015-04-15",
        "revenue_yoy": 5.23
      },
      {
        "date": "2015-05-16",
        "revenue_yoy": -6.21
      },
      {
        "date": "2015-06-15",
        "revenue_yoy": -1.68
      },
      {
        "date": "2015-07-16",
        "revenue_yoy": 6.49
      },
      {
        "date": "2015-08-16",
        "revenue_yoy": 20.3
      },
      {
        "date": "2015-09-15",
        "revenue_yoy": 12.4
      },
      {
        "date": "2015-10-16",
        "revenue_yoy": 6.76
      },
      {
        "date": "2015-11-15",
        "revenue_yoy": 5.8
      },
      {
        "date": "2015-12-16",
        "revenue_yoy": 19.9
      },
      {
        "date": "2016-01-16",
        "revenue_yoy": 20.7
      },
      {
        "date": "2016-02-15",
        "revenue_yoy": 7.47
      },
      {
        "date": "2016-03-16",
        "revenue_yoy": -7.01
      },
      {
        "date": "2016-04-15",
        "revenue_yoy": 7.07
      },
      {
        "date": "2016-05-16",
        "revenue_yoy": 15.2
      },
      {
        "date": "2016-06-15",
        "revenue_yoy": -4.45
      },
      {
        "date": "2016-07-16",
        "revenue_yoy": 15.4
      },
      {
        "date": "2016-08-16",
        "revenue_yoy": 9.71
      },
      {
        "date": "2016-09-15",
        "revenue_yoy": 7.57
      },
      {
        "date": "2016-10-16",
        "revenue_yoy": -1.25
      },
      {
        "date": "2016-11-15",
        "revenue_yoy": -9.77
      },
      {
        "date": "2016-12-16",
        "revenue_yoy": 0.31
      },
      {
        "date": "2017-01-16",
        "revenue_yoy": 2.23
      },
      {
        "date": "2017-02-14",
        "revenue_yoy": 8.91
      },
      {
        "date": "2017-03-16",
        "revenue_yoy": 7.73
      },
      {
        "date": "2017-04-15",
        "revenue_yoy": 1.27
      },
      {
        "date": "2017-05-16",
        "revenue_yoy": -1.91
      },
      {
        "date": "2017-06-15",
        "revenue_yoy": 0.62
      },
      {
        "date": "2017-07-16",
        "revenue_yoy": -6.18
      },
      {
        "date": "2017-08-16",
        "revenue_yoy": 7.59
      },
      {
        "date": "2017-09-15",
        "revenue_yoy": -6.63
      },
      {
        "date": "2017-10-16",
        "revenue_yoy": 13.6
      },
      {
        "date": "2017-11-15",
        "revenue_yoy": -6.9
      },
      {
        "date": "2017-12-16",
        "revenue_yoy": 13.6
      },
      {
        "date": "2018-01-16",
        "revenue_yoy": -3.47
      },
      {
        "date": "2018-02-14",
        "revenue_yoy": -1.14
      },
      {
        "date": "2018-03-16",
        "revenue_yoy": 4.69
      },
      {
        "date": "2018-04-15",
        "revenue_yoy": 6.14
      },
      {
        "date": "2018-05-16",
        "revenue_yoy": 8.79
      },
      {
        "date": "2018-06-15",
        "revenue_yoy": 15.0
      },
      {
        "date": "2018-07-16",
        "revenue_yoy": 6.56
      },
      {
        "date": "2018-08-16",
        "revenue_yoy": -12.0
      },
      {
        "date": "2018-09-15",
        "revenue_yoy": -6.72
      },
      {
        "date": "2018-10-16",
        "revenue_yoy": -15.2
      },
      {
        "date": "2018-11-15",
        "revenue_yoy": 16.7
      },
      {
        "date": "2018-12-16",
        "revenue_yoy": -1.47
      },
      {
        "date": "2019-01-16",
        "revenue_yoy": 1.52
      },
      {
        "date": "2019-02-14",
        "revenue_yoy": 8.0
      },
      {
        "date": "2019-03-16",
        "revenue_yoy": -7.19
      },
      {
        "date": "2019-04-15",
        "revenue_yoy": -3.73
      },
      {
        "date": "2019-05-16",
        "revenue_yoy": -3.94
      },
      {
        "date": "2019-06-15",
        "revenue_yoy": 7.36
      },
      {
        "date": "2019-07-16",
        "revenue_yoy": 7.42
      },
      {
        "date": "2019-08-16",
        "revenue_yoy": 4.52
      },
      {
        "date": "2019-09-15",
        "revenue_yoy": 9.72
      },
      {
        "date": "2019-10-16",
        "revenue_yoy": 4.66
      },
      {
        "date": "2019-11-15",
        "revenue_yoy": 3.65
      },
      {
        "date": "2019-12-16",
        "revenue_yoy": 10.8
      },
      {
        "date": "2020-01-16",
        "revenue_yoy": 7.66
      },
      {
        "date": "2020-02-15",
        "revenue_yoy": 7.72
      },
      {
        "date": "2020-03-16",
        "revenue_yoy": 6.47
      },
      {
        "date": "2020-04-15",
        "revenue_yoy": 19.8
      },
      {
        "date": "2020-05-16",
        "revenue_yoy": 15.2
      },
      {
        "date": "2020-06-15",
        "revenue_yoy": 26.2
      },
      {
        "date": "2020-07-16",
        "revenue_yoy": 9.89
      },
      {
        "date": "2020-08-16",
        "revenue_yoy": 38.3
      },
      {
        "date": "2020-09-15",
        "revenue_yoy": 23.4
      },
      {
        "date": "2020-10-16",
        "revenue_yoy": 14.3
      },
      {
        "date": "2020-11-15",
        "revenue_yoy": 8.82
      },
      {
        "date": "2020-12-16",
        "revenue_yoy": 5.69
      },
      {
        "date": "2021-01-16",
        "revenue_yoy": 27.8
      },
      {
        "date": "2021-02-14",
        "revenue_yoy": 31.5
      },
      {
        "date": "2021-03-16",
        "revenue_yoy": 28.3
      },
      {
        "date": "2021-04-15",
        "revenue_yoy": 13.6
      },
      {
        "date": "2021-05-16",
        "revenue_yoy": 16.5
      },
      {
        "date": "2021-06-15",
        "revenue_yoy": 1.04
      },
      {
        "date": "2021-07-16",
        "revenue_yoy": 27.0
      },
      {
        "date": "2021-08-16",
        "revenue_yoy": 2.93
      },
      {
        "date": "2021-09-15",
        "revenue_yoy": 17.2
      },
      {
        "date": "2021-10-16",
        "revenue_yoy": 14.9
      },
      {
        "date": "2021-11-15",
        "revenue_yoy": 13.0
      },
      {
        "date": "2021-12-16",
        "revenue_yoy": 7.91
      },
      {
        "date": "2022-01-16",
        "revenue_yoy": 17.2
      },
      {
        "date": "2022-02-14",
        "revenue_yoy": 10.5
      },
      {
        "date": "2022-03-16",
        "revenue_yoy": 7.87
      },
      {
        "date": "2022-04-15",
        "revenue_yoy": 2.42
      },
      {
        "date": "2022-05-16",
        "revenue_yoy": 4.05
      },
      {
        "date": "2022-06-15",
        "revenue_yoy": 12.8
      },
      {
        "date": "2022-07-16",
        "revenue_yoy": -1.13
      },
      {
        "date": "2022-08-16",
        "revenue_yoy": 1.79
      },
      {
        "date": "2022-09-15",
        "revenue_yoy": -8.42
      },
      {
        "date": "2022-10-16",
        "revenue_yoy": 27.0
      },
      {
        "date": "2022-11-15",
        "revenue_yoy": -0.93
      },
      {
        "date": "2022-12-16",
        "revenue_yoy": -0.8
      },
      {
        "date": "2023-01-16",
        "revenue_yoy": -2.8
      },
      {
        "date": "2023-02-14",
        "revenue_yoy": -7.84
      },
      {
        "date": "2023-03-16",
        "revenue_yoy": 4.92
      },
      {
        "date": "2023-04-15",
        "revenue_yoy": 12.0
      },
      {
        "date": "2023-05-16",
        "revenue_yoy": 12.8
      },
      {
        "date": "2023-06-15",
        "revenue_yoy": -13.1
      },
      {
        "date": "2023-07-16",
        "revenue_yoy": 9.03
      },
      {
        "date": "2023-08-16",
        "revenue_yoy": 6.14
      },
      {
        "date": "2023-09-15",
        "revenue_yoy": 12.7
      },
      {
        "date": "2023-10-16",
        "revenue_yoy": -10.0
      },
      {
        "date": "2023-11-15",
        "revenue_yoy": 10.9
      },
      {
        "date": "2023-12-16",
        "revenue_yoy": -10.7
      },
      {
        "date": "2024-01-16",
        "revenue_yoy": 4.93
      },
      {
        "date": "2024-02-15",
        "revenue_yoy": 8.75
      },
      {
        "date": "2024-03-16",
        "revenue_yoy": 5.32
      },
      {
        "date": "2024-04-15",
        "revenue_yoy": 2.24
      },
      {
        "date": "2024-05-16",
        "revenue_yoy": 4.19
      },
      {
        "date": "2024-06-15",
        "revenue_yoy": 5.61
      },
      {
        "date": "2024-07-16",
        "revenue_yoy": 6.71
      },
      {
        "date": "2024-08-16",
        "revenue_yoy": 18.3
      },
      {
        "date": "2024-09-15",
        "revenue_yoy": 16.1
      },
      {
        "date": "2024-10-16",
        "revenue_yoy": 14.2
      },
      {
        "date": "2024-11-15",
        "revenue_yoy": 23.7
      },
      {
        "date": "2024-12-16",
        "revenue_yoy": 65.1
      },
      {
        "date": "2025-01-16",
        "revenue_yoy": 12.8
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 21.3
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": 16.2
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": 8.84
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": 8.23
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 17.6
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": 4.98
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": 1.59
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": 5.84
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": 5.96
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": 5.87
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -10.2
      },
      {
        "date": "2026-01-16",
        "revenue_yoy": 11.5
      },
      {
        "date": "2026-02-14",
        "revenue_yoy": 5.3
      },
      {
        "date": "2026-03-16",
        "revenue_yoy": 21.6
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
| 3個月 | 13.2 | -15.3% | 1.000 | 2025-12 (-7.2%) | 2025-11 (-23.3%) |


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
*數據更新時間: 2026-05-16 13:53:46 CST*
