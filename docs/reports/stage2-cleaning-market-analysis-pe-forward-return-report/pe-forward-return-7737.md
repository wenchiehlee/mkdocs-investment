---
title: "7737 凱鈿 - 本益比與未來報酬率分析 (互動式)"
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
description: "7737 凱鈿 (數位雲端) 本益比與未來報酬率關係分析 - 互動式多期間版本"
---

# 7737 凱鈿 - 本益比與未來報酬率分析

!!! info "報告資訊"
    - **股票代號**: 7737
    - **公司名稱**: 凱鈿
    - **產業別**: 數位雲端
    - **報告類型**: 互動式多期間分析
    - **可選期間**: 3個月, 6個月
    - **報告生成時間**: 2026-01-25 20:41:46 CST

## 📈 互動式圖表

使用下拉選單切換不同投資期間的回測結果。選擇「全部期間」可同時顯示所有期間的數據進行比較。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7737 凱鈿 - 本益比與未來報酬率分析",
  "data": {
    "values": [
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-02-14",
        "pe_ratio": NaN,
        "forward_return": -86.11,
        "start_price": 71.4,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-03-16",
        "pe_ratio": NaN,
        "forward_return": -38.44,
        "start_price": 59.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-04-15",
        "pe_ratio": NaN,
        "forward_return": 40.38,
        "start_price": 46.5,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-05-16",
        "pe_ratio": NaN,
        "forward_return": 20.9,
        "start_price": 43.9,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-06-15",
        "pe_ratio": NaN,
        "forward_return": -48.25,
        "start_price": 48.4,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-07-16",
        "pe_ratio": NaN,
        "forward_return": -28.5,
        "start_price": 50.6,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-08-16",
        "pe_ratio": NaN,
        "forward_return": -43.74,
        "start_price": 46.05,
        "start_year": 2025
      },
      {
        "horizon": "0.25y",
        "horizon_label": "3個月",
        "start_date": "2025-09-15",
        "pe_ratio": NaN,
        "forward_return": -26.29,
        "start_price": 41.0,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-02-14",
        "pe_ratio": NaN,
        "forward_return": -58.53,
        "start_price": 71.4,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-03-16",
        "pe_ratio": NaN,
        "forward_return": -34.35,
        "start_price": 59.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-04-15",
        "pe_ratio": NaN,
        "forward_return": 0.0,
        "start_price": 46.5,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-05-16",
        "pe_ratio": NaN,
        "forward_return": -21.83,
        "start_price": 43.9,
        "start_year": 2025
      },
      {
        "horizon": "0.5y",
        "horizon_label": "6個月",
        "start_date": "2025-06-15",
        "pe_ratio": NaN,
        "forward_return": -38.3,
        "start_price": 48.4,
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


## 📊 月營收年增率

月營收與去年同期相比的成長率。紅色柱狀代表正成長，綠色代表衰退。

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "7737 凱鈿 - 月營收年增率",
  "data": {
    "values": [
      {
        "date": "2025-01-16",
        "revenue_yoy": -9.14
      },
      {
        "date": "2025-02-14",
        "revenue_yoy": 14.4
      },
      {
        "date": "2025-03-16",
        "revenue_yoy": -9.88
      },
      {
        "date": "2025-04-15",
        "revenue_yoy": -4.32
      },
      {
        "date": "2025-05-16",
        "revenue_yoy": -2.2
      },
      {
        "date": "2025-06-15",
        "revenue_yoy": 2.53
      },
      {
        "date": "2025-07-16",
        "revenue_yoy": -12.9
      },
      {
        "date": "2025-08-16",
        "revenue_yoy": -19.0
      },
      {
        "date": "2025-09-15",
        "revenue_yoy": -28.1
      },
      {
        "date": "2025-10-16",
        "revenue_yoy": -27.1
      },
      {
        "date": "2025-11-15",
        "revenue_yoy": -30.2
      },
      {
        "date": "2025-12-16",
        "revenue_yoy": -29.4
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
| 3個月 | nan | -26.3% | 0.000 | 2025-04 (+40.4%) | 2025-02 (-86.1%) |
| 6個月 | nan | -30.6% | 0.000 | 2025-04 (+0.0%) | 2025-02 (-58.5%) |


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
*數據更新時間: 2026-01-25 20:41:46 CST*
