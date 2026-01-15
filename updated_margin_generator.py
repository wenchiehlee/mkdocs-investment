# -*- coding: utf-8 -*-
# src/pipelines/stage2_data_cleaning_margin_daily.py
import pandas as pd
import numpy as np
import click
from pathlib import Path
import logging
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import pytz
import re
import matplotlib
import json
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

matplotlib.rcParams['svg.fonttype'] = 'path'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def safe_echo(message: str):
    try:
        click.echo(message)
    except UnicodeEncodeError:
        clean_message = re.sub(r'[^\x00-\x7F]+', '', message)
        click.echo(clean_message)

class MarginDailyReportGenerator:
    def __init__(self, input_dir: str, output_dir: str, summary_output: str, min_days: int = 30):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.summary_output = Path(summary_output)
        self.min_days = min_days
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.margin_df = None
        self.margin_weekly_df = None
        self.margin_monthly_df = None
        self.company_info_df = None
        self.total_market_cap = None

    def load_margin_data(self) -> pd.DataFrame:
        margin_file = self.input_dir / 'raw_margin_daily.csv'
        if not margin_file.exists():
            raise FileNotFoundError(f"Margin daily data not found: {margin_file}")
        df = pd.read_csv(margin_file, dtype={'stock_code': str})
        required_columns = ['stock_code', 'company_name', '期別', '收盤_價格_元', '融資_餘額_張', '融券_餘額_張']
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        df = df[df['stock_code'] != '加權指數'].copy()
        return df

    def load_margin_weekly_data(self) -> pd.DataFrame:
        weekly_file = self.input_dir / 'raw_margin_weekly.csv'
        if not weekly_file.exists():
            return pd.DataFrame()
        df = pd.read_csv(weekly_file, dtype={'stock_code': str}, encoding='utf-8-sig')
        df = df[df['stock_code'] != '加權指數'].copy()
        return df

    def load_margin_monthly_data(self) -> pd.DataFrame:
        monthly_file = self.input_dir / 'raw_margin_monthly.csv'
        if not monthly_file.exists():
            return pd.DataFrame()
        df = pd.read_csv(monthly_file, dtype={'stock_code': str}, encoding='utf-8-sig')
        df = df[df['stock_code'] != '加權指數'].copy()
        return df

    def load_company_info(self) -> pd.DataFrame:
        company_info_file = self.input_dir / 'raw_companyinfo.csv'
        if not company_info_file.exists():
            return pd.DataFrame()
        df = pd.read_csv(company_info_file, dtype={'代號': str}, encoding='utf-8-sig')
        if '市值' in df.columns:
            df['市值_億元'] = df['市值'].apply(self._parse_market_cap)
            tsmc = df[df['代號'] == '2330']
            if not tsmc.empty and pd.notna(tsmc.iloc[0]['市值佔大盤比重']) and pd.notna(tsmc.iloc[0]['市值_億元']):
                ratio_str = str(tsmc.iloc[0]['市值佔大盤比重']).replace('%', '')
                tsmc_ratio = float(ratio_str) / 100
                tsmc_market_cap = tsmc.iloc[0]['市值_億元']
                self.total_market_cap = tsmc_market_cap / tsmc_ratio
            else:
                valid_market_caps = df[df['市值_億元'].notna()]['市值_億元']
                self.total_market_cap = valid_market_caps.sum()
        return df

    def _parse_market_cap(self, market_cap_str: str) -> Optional[float]:
        if pd.isna(market_cap_str) or market_cap_str == '':
            return None
        try:
            clean_str = str(market_cap_str).replace(',', '')
            if '兆' in clean_str:
                return float(clean_str.replace('兆', '')) * 10000
            elif '億' in clean_str:
                return float(clean_str.replace('億', ''))
            else:
                return float(clean_str)
        except:
            return None

    def prepare_stock_data(self, stock_code: str) -> Optional[pd.DataFrame]:
        stock_data = self.margin_df[self.margin_df['stock_code'] == stock_code].copy()
        if stock_data.empty or len(stock_data) < self.min_days:
            return None
        stock_data['date'] = pd.to_datetime(stock_data['期別'].str.replace("'", ""), format='%y/%m/%d')
        stock_data = stock_data.sort_values('date', ascending=False).reset_index(drop=True)
        if stock_code == '0000' and '融資_餘額_億' in stock_data.columns:
            pass
        else:
            stock_data['融資_餘額_億'] = (stock_data['融資_餘額_張'] * stock_data['收盤_價格_元'] * 1000) / 1e8
        if self.company_info_df is not None and not self.company_info_df.empty:
            if stock_code == '0000':
                stock_data['市值_億元'] = self.total_market_cap
            else:
                company_info = self.company_info_df[self.company_info_df['代號'] == stock_code]
                stock_data['市值_億元'] = company_info.iloc[0]['市值_億元'] if not company_info.empty else None
        else:
            stock_data['市值_億元'] = None
        return stock_data

    def calculate_changes(self, df: pd.DataFrame) -> Dict[str, any]:
        if len(df) < 2: return {}
        latest = df.iloc[0]
        prev_day = df.iloc[1]
        prev_week = df.iloc[min(5, len(df)-1)]
        prev_month = df.iloc[min(20, len(df)-1)]
        changes = {
            'latest_balance': latest['融資_餘額_億'],
            'latest_balance_lots': latest['融資_餘額_張'],
            'latest_price': latest['收盤_價格_元'],
            'latest_date': latest['date'].strftime('%Y-%m-%d'),
            'has_market_cap': '市值_億元' in latest.index and pd.notna(latest['市值_億元']) and latest['市值_億元'] > 0
        }
        if changes['has_market_cap']:
            changes['market_cap'] = latest['市值_億元']
            changes['margin_to_cap_ratio'] = (latest['融資_餘額_億'] / latest['市值_億元']) * 100
        changes['dod_change'] = latest['融資_餘額_億'] - prev_day['融資_餘額_億']
        changes['dod_pct'] = (changes['dod_change'] / prev_day['融資_餘額_億'] * 100) if prev_day['融資_餘額_億'] > 0 else 0
        changes['wow_change'] = latest['融資_餘額_億'] - prev_week['融資_餘額_億']
        changes['wow_pct'] = (changes['wow_change'] / prev_week['融資_餘額_億'] * 100) if prev_week['融資_餘額_億'] > 0 else 0
        changes['mom_change'] = latest['融資_餘額_億'] - prev_month['融資_餘額_億']
        changes['mom_pct'] = (changes['mom_change'] / prev_month['融資_餘額_億'] * 100) if prev_month['融資_餘額_億'] > 0 else 0
        changes['max_balance'] = df['融資_餘額_億'].max()
        changes['min_balance'] = df['融資_餘額_億'].min()
        changes['avg_balance'] = df['融資_餘額_億'].mean()
        changes['std_balance'] = df['融資_餘額_億'].std()
        return changes

    def calculate_recent_weekly_change_pct(self, stock_code: str, weeks: int) -> Optional[float]:
        change = self.calculate_recent_weekly_change(stock_code, weeks)
        return change['pct'] if change else None

    def calculate_recent_weekly_change(self, stock_code: str, weeks: int) -> Optional[Dict[str, float]]:
        if self.margin_weekly_df is None or self.margin_weekly_df.empty: return None
        weekly_data = self.margin_weekly_df[self.margin_weekly_df['stock_code'] == stock_code].copy()
        if weekly_data.empty: return None
        def parse_week_date(ws):
            try: return pd.to_datetime(f"20{ws[:2]}-W{ws[3:]}-1", format='%Y-W%W-%w')
            except: return pd.NaT
        weekly_data['date'] = weekly_data['期別'].apply(parse_week_date)
        weekly_data = weekly_data.dropna(subset=['date'])
        if stock_code == '0000':
            if '融資_使用率_pct' not in weekly_data.columns: return None
            weekly_data['融資_餘額_億'] = pd.to_numeric(weekly_data['融資_使用率_pct'], errors='coerce')
        else:
            weekly_data['融資_餘額_億'] = (pd.to_numeric(weekly_data.get('融資_餘額_張'), errors='coerce') * pd.to_numeric(weekly_data.get('收盤_價格_元'), errors='coerce') * 1000) / 1e8
        weekly_data = weekly_data.dropna(subset=['融資_餘額_億'])
        if len(weekly_data) <= weeks: return None
        weekly_data = weekly_data.sort_values('date', ascending=False)
        latest = weekly_data.iloc[0]['融資_餘額_億']
        prev = weekly_data.iloc[weeks]['融資_餘額_億']
        if prev <= 0: return None
        return {'change': latest - prev, 'pct': round((latest - prev) / prev * 100, 2)}

    def prepare_chart_data_3year(self, stock_code: str, stock_data: pd.DataFrame) -> pd.DataFrame:
        latest_date = stock_data['date'].max()
        split_date = max(latest_date - pd.Timedelta(days=365), stock_data['date'].min())
        combined_datasets = [stock_data[stock_data['date'] >= split_date].copy()]
        if self.margin_weekly_df is not None and not self.margin_weekly_df.empty:
            weekly_data = self.margin_weekly_df[self.margin_weekly_df['stock_code'] == stock_code].copy()
            def parse_week_date(ws):
                try: return pd.to_datetime(f"20{ws[:2]}-W{ws[3:]}-1", format='%Y-W%W-%w')
                except: return pd.NaT
            weekly_data['date'] = weekly_data['期別'].apply(parse_week_date)
            weekly_data = weekly_data.dropna(subset=['date'])
            historical_weekly = weekly_data[(weekly_data['date'] >= latest_date - pd.Timedelta(days=365*4)) & (weekly_data['date'] < split_date)].copy()
            if not historical_weekly.empty:
                if stock_code == '0000':
                    historical_weekly['融資_餘額_億'] = historical_weekly.get('融資_使用率_pct', 0)
                else:
                    historical_weekly['融資_餘額_億'] = (historical_weekly['融資_餘額_張'] * historical_weekly['收盤_價格_元'] * 1000) / 1e8
                if self.company_info_df is not None and not self.company_info_df.empty:
                    cinfo = self.company_info_df[self.company_info_df['代號'] == stock_code]
                    historical_weekly['市值_億元'] = cinfo.iloc[0]['市值_億元'] if not cinfo.empty else self.total_market_cap if stock_code == '0000' else None
                combined_datasets.append(historical_weekly[['date', '收盤_價格_元', '融資_餘額_億', '市值_億元', 'company_name']])
        if len(combined_datasets) > 1:
            return pd.concat(combined_datasets, ignore_index=True).sort_values('date').reset_index(drop=True)
        return stock_data.copy()

    def export_interactive_json(self, stock_code: str, df: pd.DataFrame, output_dir: Path):
        try:
            df = df.sort_values('date')
            chart_data = [[int(r['date'].timestamp() * 1000), float(r['融資_餘額_億'])] for _, r in df.iterrows() if pd.notna(r['date']) and pd.notna(r['融資_餘額_億'])]
            with open(output_dir / f"margin_daily-{stock_code}.json", 'w', encoding='utf-8') as f:
                json.dump(chart_data, f)
            return True
        except: return False

    def create_margin_chart(self, stock_code: str, stock_data: pd.DataFrame, output_file: Path) -> bool:
        try:
            plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'Noto Sans CJK TC', 'WenQuanYi Zen Hei']
            plt.rcParams['axes.unicode_minus'] = False
            fig, ax1 = plt.subplots(figsize=(20, 10))
            latest_date = stock_data['date'].max()
            split_date = max(latest_date - pd.Timedelta(days=365), stock_data['date'].min())
            daily_only = stock_data[stock_data['date'] >= split_date].copy().sort_values('date')
            long_term = self.prepare_chart_data_3year(stock_code, stock_data)
            company_name = stock_data['company_name'].iloc[0]
            ax2 = ax1.twinx()
            weekly_monthly = long_term[long_term['date'] < split_date]
            if not weekly_monthly.empty:
                ax2.bar(weekly_monthly['date'], weekly_monthly['融資_餘額_億'], color='#90EE90', alpha=0.85, width=5.0, label='融資餘額 (週/月)')
            if not daily_only.empty:
                ax2.bar(daily_only['date'], daily_only['融資_餘額_億'], color='#FFD700', alpha=0.85, width=1.5, label='融資餘額 (日)')
            all_max = long_term['融資_餘額_億'].max()
            ax2.set_ylim(0, all_max * 4.0)
            ax1.plot(long_term['date'], long_term['收盤_價格_元'], color='#000000', linewidth=2.5, label='收盤價 (長期)')
            if '市值_億元' in long_term.columns:
                ratio = (long_term['融資_餘額_億'] / long_term['市值_億元'] * 100)
                if not ratio.isna().all():
                    ax3 = ax1.twinx()
                    ax3.spines['right'].set_position(('outward', 60))
                    ax3.plot(long_term['date'], ratio, color='#FF0000', linewidth=2.5, label='融資餘額/市值')
                    rmin, rmax = ratio.min(), ratio.max()
                    ax3.set_ylim(max(0, rmin - (rmax-rmin)*1.5), rmax + (rmax-rmin)*1.5)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
            plt.savefig(output_file, format='svg', bbox_inches='tight')
            plt.close()
            return True
        except: return False

    def generate_markdown_report(self, stock_code: str, stock_data: pd.DataFrame) -> str:
        company_name = stock_data['company_name'].iloc[0]
        changes = self.calculate_changes(stock_data)
        if not changes: return ""
        now_cst = datetime.now(pytz.timezone('Asia/Taipei'))
        json_filename = f"margin_daily-{stock_code}.json"
        
        md = f"""---
authors: [wenchiehlee]
date: {now_cst.strftime('%Y-%m-%d')}
categories: [股票, 融資餘額]
tags: [股票, 融資, 市場情緒]
title: 融資餘額報告 {company_name} ({stock_code})
comments: false
draft: false
description: 融資餘額報告 {company_name} ({stock_code}) - 自動產生
---

# \U0001f4c8 {company_name} ({stock_code}) \u87a2\u8cc7\u9918\u984d\u5831\u544a

!!! info "\u57fa\u672c\u8cc7\u8a0a"
    **\U0001f3d7\ufe0f \u540d\u7a31**: {company_name}
    **\U0001faaa \u4ee3\u865f**: {stock_code}
    **\U0001f4c5 \u5206\u6790\u671f\u9593**: {stock_data['date'].min().strftime('%Y-%m-%d')} ~ {stock_data['date'].max().strftime('%Y-%m-%d')}
    **\u23f3 \u6700\u65b0\u8cc7\u6599**: {changes['latest_date']}

## \U0001f4ca \u87a2\u8cc7\u9918\u984d\u8da8\u52e2\u5716

<div class="chart-container" style="text-align: center; margin: 20px 0;" markdown="1">
<div class="margin-chart" data-url="../{json_filename}" data-title="\u87a2\u8cc7\u9918\u984d"></div>
</div>

## \U0001f4cb \u8a73\u7d30\u6b77\u53f2\u8a18\u9304

<table class="sortable-table">
<thead><tr><th>\U0001f4c5 \u65e5\u671f</th><th>\U0001f4b8 \u6536\u76e4\u50f9</th><th>\U0001f4e6 \u87a2\u8cc7\u9918\u984d</th></tr></thead>
<tbody>"""
        for _, r in stock_data.head(30).iterrows():
            md += f"<tr><td>{r['date'].strftime('%Y-%m-%d')}</td><td>{r['收盤_價格_元']:.2f}</td><td>{r['融資_餘額_億']:.1f}</td></tr>"
        md += "</tbody></table>"
        return md

    def generate_report(self, stock_code: str) -> bool:
        stock_data = self.prepare_stock_data(stock_code)
        if stock_data is None: return False
        self.export_interactive_json(stock_code, stock_data, self.output_dir)
        md_content = self.generate_markdown_report(stock_code, stock_data)
        with open(self.output_dir / f"stage2-cleaning-margin_daily-report-{stock_code}.md", 'w', encoding='utf-8') as f:
            f.write(md_content)
        return True

    def generate_summary_report(self, generated_stocks: List[str]) -> bool:
        now_cst = datetime.now(pytz.timezone('Asia/Taipei'))
        md = f"""---
title: 融資餘額報告彙總
date: {now_cst.strftime('%Y-%m-%d')}
---
# \U0001f4c8 \u87a2\u8cc7\u9918\u984d\u5831\u544a\u5f59\u7e3d
<table class="sortable-table">
<thead><tr><th>\U0001faaa \u4ee3\u865f</th><th>\U0001f3d7\ufe0f \u540d\u7a31</th><th>\U0001f4e6 \u87a2\u8cc7\u9918\u984d</th></tr></thead>
<tbody>"""
        for sc in sorted(generated_stocks):
            sd = self.prepare_stock_data(sc)
            if sd is None: continue
            name = "加權指數" if sc == '0000' else sd['company_name'].iloc[0]
            link = f"../stage2-cleaning-margin_daily-report/stage2-cleaning-margin_daily-report-{sc}/"
            md += f"<tr><td markdown='span'>[**{sc}**]({link})</td><td>{name}</td><td>{sd['融資_餘額_億'].iloc[0]:.1f}</td></tr>"
        md += "</tbody></table>"
        with open(self.summary_output, 'w', encoding='utf-8') as f:
            f.write(md)
        return True

    def run(self, stock_code=None, all_stocks=False):
        self.margin_df = self.load_margin_data()
        self.margin_weekly_df = self.load_margin_weekly_data()
        self.company_info_df = self.load_company_info()
        if stock_code: return self.generate_report(stock_code)
        elif all_stocks:
            stocks = self.margin_df['stock_code'].unique()
            gen = [s for s in stocks if self.generate_report(s)]
            return self.generate_summary_report(gen)
        return False

@click.command()
@click.option('--stock-code', '-s')
@click.option('--all-stocks', '-a', is_flag=True)
@click.option('--input-dir', '-i', default='data/stage1_raw/')
@click.option('--output-dir', '-o', default='data/stage2_cleaned/stage2-cleaning-margin_daily-report/')
@click.option('--summary-output', default='data/stage2_cleaned/stage2-cleaning-margin_daily-report-all.md')
def main(stock_code, all_stocks, input_dir, output_dir, summary_output):
    gen = MarginDailyReportGenerator(input_dir, output_dir, summary_output)
    if gen.run(stock_code, all_stocks): safe_echo("\u2705 Success")
    else: safe_echo("\u274c Failed")

if __name__ == '__main__':
    main()