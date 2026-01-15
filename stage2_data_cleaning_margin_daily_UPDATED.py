# src/pipelines/stage2_data_cleaning_margin_daily.py
"""
Stage 2 Specialized Tool: Margin Daily Report Generator v1.0.0
Generate comprehensive margin financing balance reports for market index or individual stocks.

Features:
- Daily/weekly/monthly margin financing trends
- Correlation with market index movements
- Historical highs/lows analysis
- Change rate analysis (DoD, WoW, MoM)
- Warning signals for excessive margin usage
- Visual chart data preparation
"""

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
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Make SVGs portable: embed text as paths
matplotlib.rcParams['svg.fonttype'] = 'path'

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def safe_echo(message: str):
    """Safe echo that handles Unicode encoding issues on Windows"""
    try:
        click.echo(message)
    except UnicodeEncodeError:
        clean_message = re.sub(r'[^\x00-\x7F]+', '', message)
        click.echo(clean_message)


class MarginDailyReportGenerator:
    """Generate comprehensive margin financing daily reports"""

    def __init__(self, input_dir: str, output_dir: str, summary_output: str,
                 min_days: int = 30):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.summary_output = Path(summary_output)
        self.min_days = min_days

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Data storage
        self.margin_df = None
        self.margin_weekly_df = None
        self.margin_monthly_df = None
        self.company_info_df = None
        self.total_market_cap = None  # 市場總市值（億元）

    def load_margin_data(self) -> pd.DataFrame:
        """Load and validate margin daily data from stage1 raw CSV"""
        margin_file = self.input_dir / 'raw_margin_daily.csv'

        if not margin_file.exists():
            raise FileNotFoundError(f"Margin daily data not found: {margin_file}")

        logger.info(f"Loading margin daily data from {margin_file}")
        # Force stock_code to be read as string to handle '0000' correctly
        df = pd.read_csv(margin_file, dtype={'stock_code': str})

        # Validate required columns
        required_columns = [
            'stock_code', 'company_name', '期別',
            '收盤_價格_元', '融資_餘額_張', '融券_餘額_張'
        ]

        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # Filter out duplicate "加權指數" (use "0000" instead, which has more recent data)
        # Both represent Taiwan Weighted Index, but "0000" is the standard code
        df = df[df['stock_code'] != '加權指數'].copy()

        logger.info(f"Loaded {len(df)} margin records for {df['stock_code'].nunique()} stocks")
        return df

    def load_margin_weekly_data(self) -> pd.DataFrame:
        """Load margin weekly data for extended historical range"""
        weekly_file = self.input_dir / 'raw_margin_weekly.csv'

        if not weekly_file.exists():
            logger.warning(f"Margin weekly data not found: {weekly_file}")
            return pd.DataFrame()

        logger.info(f"Loading margin weekly data from {weekly_file}")
        df = pd.read_csv(weekly_file, dtype={'stock_code': str}, encoding='utf-8-sig')

        # Filter out duplicate "加權指數"
        df = df[df['stock_code'] != '加權指數'].copy()

        logger.info(f"Loaded {len(df)} weekly margin records for {df['stock_code'].nunique()} stocks")
        return df

    def load_margin_monthly_data(self) -> pd.DataFrame:
        """Load margin monthly data for extended historical range"""
        monthly_file = self.input_dir / 'raw_margin_monthly.csv'

        if not monthly_file.exists():
            logger.warning(f"Margin monthly data not found: {monthly_file}")
            return pd.DataFrame()

        logger.info(f"Loading margin monthly data from {monthly_file}")
        df = pd.read_csv(monthly_file, dtype={'stock_code': str}, encoding='utf-8-sig')

        # Filter out duplicate "加權指數"
        df = df[df['stock_code'] != '加權指數'].copy()

        logger.info(f"Loaded {len(df)} monthly margin records for {df['stock_code'].nunique()} stocks")
        return df

    def load_company_info(self) -> pd.DataFrame:
        """Load and parse company info data including market cap"""
        company_info_file = self.input_dir / 'raw_companyinfo.csv'

        if not company_info_file.exists():
            logger.warning(f"Company info not found: {company_info_file}")
            return pd.DataFrame()

        logger.info(f"Loading company info from {company_info_file}")
        df = pd.read_csv(company_info_file, dtype={'代號': str}, encoding='utf-8-sig')

        # Parse market cap column
        if '市值' in df.columns:
            df['市值_億元'] = df['市值'].apply(self._parse_market_cap)
            logger.info(f"Loaded company info for {len(df)} companies")

            # Calculate total market cap for market index (0000)
            # Use market cap ratio to estimate real total market cap
            # (instead of just summing sample companies which only covers ~78% of market)
            if '市值佔大盤比重' in df.columns:
                # Find a large cap stock with reliable data (e.g., TSMC 2330)
                tsmc = df[df['代號'] == '2330']
                if not tsmc.empty and pd.notna(tsmc.iloc[0]['市值佔大盤比重']) and pd.notna(tsmc.iloc[0]['市值_億元']):
                    # Parse ratio (e.g., "43.0957%" -> 0.430957)
                    ratio_str = str(tsmc.iloc[0]['市值佔大盤比重']).replace('%', '')
                    tsmc_ratio = float(ratio_str) / 100
                    tsmc_market_cap = tsmc.iloc[0]['市值_億元']
                    # Reverse calculate real total market cap
                    self.total_market_cap = tsmc_market_cap / tsmc_ratio
                    sample_sum = df[df['市值_億元'].notna()]['市值_億元'].sum()
                    logger.info(f"Real total market cap (from TSMC ratio): {self.total_market_cap:,.0f} 億元 ({self.total_market_cap/10000:.2f} 兆元)")
                    logger.info(f"Sample coverage: {len(df)} companies = {sample_sum:,.0f} 億元 ({sample_sum/self.total_market_cap*100:.1f}% of market)")
                else:
                    # Fallback: use sample sum (incomplete)
                    valid_market_caps = df[df['市值_億元'].notna()]['市值_億元']
                    self.total_market_cap = valid_market_caps.sum()
                    logger.warning(f"Using sample sum (incomplete): {self.total_market_cap:,.0f} 億元 ({self.total_market_cap/10000:.2f} 兆元)")
            else:
                # Fallback: use sample sum (incomplete)
                valid_market_caps = df[df['市值_億元'].notna()]['市值_億元']
                self.total_market_cap = valid_market_caps.sum()
                logger.warning(f"No ratio data, using sample sum: {self.total_market_cap:,.0f} 億元 ({self.total_market_cap/10000:.2f} 兆元)")
        else:
            logger.warning("Market cap column not found in company info")

        return df

    def _parse_market_cap(self, market_cap_str: str) -> Optional[float]:
        """Parse market cap string to 億元 (e.g., '43.57兆' -> 435700, '1,302.31億' -> 1302.31)"""
        if pd.isna(market_cap_str) or market_cap_str == '':
            return None

        try:
            # Remove commas
            clean_str = str(market_cap_str).replace(',', '')

            # Check for 兆 (trillion, 10^12 TWD = 10^4 億)
            if '兆' in clean_str:
                value = float(clean_str.replace('兆', ''))
                return value * 10000  # Convert 兆 to 億
            # Check for 億 (hundred million, 10^8 TWD)
            elif '億' in clean_str:
                value = float(clean_str.replace('億', ''))
                return value
            else:
                # Assume it's already in basic unit
                return float(clean_str)
        except (ValueError, AttributeError):
            return None

    def prepare_stock_data(self, stock_code: str) -> Optional[pd.DataFrame]:
        """Prepare and validate data for a specific stock"""
        stock_data = self.margin_df[self.margin_df['stock_code'] == stock_code].copy()

        if stock_data.empty:
            logger.warning(f"No data found for stock {stock_code}")
            return None

        if len(stock_data) < self.min_days:
            logger.warning(f"Insufficient data for stock {stock_code}: {len(stock_data)} days < {self.min_days} minimum")        
            return None

        # Parse date column ('26/01/07 format -> 2026-01-07)
        stock_data['date'] = pd.to_datetime(stock_data['期別'].str.replace("'", ""), format='%y/%m/%d')
        stock_data = stock_data.sort_values('date', ascending=False).reset_index(drop=True)

        # Convert margin balance from lots (張) to 100 million TWD (億元)
        # For market index (0000), the data already contains 融資_餘額_億 column from stage1
        if stock_code == '0000' and '融資_餘額_億' in stock_data.columns:
            # Market index data already has margin balance in 億元
            # Just ensure the column exists (it's already created by stage1)
            pass
        else:
            # Individual stocks: calculate from lots and price
            # 1 lot = 1000 shares, convert to 100 million TWD
            stock_data['融資_餘額_億'] = (stock_data['融資_餘額_張'] * stock_data['收盤_價格_元'] * 1000) / 1e8

        # Add market cap information if available
        if self.company_info_df is not None and not self.company_info_df.empty:
            if stock_code == '0000':
                # For market index, use total market cap
                stock_data['市值_億元'] = self.total_market_cap
            else:
                # For individual stocks, get market cap from company info
                company_info = self.company_info_df[self.company_info_df['代號'] == stock_code]
                if not company_info.empty and '市值_億元' in company_info.columns:
                    market_cap = company_info.iloc[0]['市值_億元']
                    stock_data['市值_億元'] = market_cap
                else:
                    stock_data['市值_億元'] = None
        else:
            stock_data['市值_億元'] = None

        return stock_data

    def calculate_changes(self, df: pd.DataFrame) -> Dict[str, any]:
        """Calculate various change metrics"""
        if len(df) < 2:
            return {}

        latest = df.iloc[0]
        prev_day = df.iloc[1] if len(df) > 1 else None
        prev_week = df.iloc[min(5, len(df)-1)] if len(df) > 5 else None
        prev_month = df.iloc[min(20, len(df)-1)] if len(df) > 20 else None

        changes = {
            'latest_balance': latest['融資_餘額_億'],
            'latest_balance_lots': latest['融資_餘額_張'],
            'latest_price': latest['收盤_價格_元'],
            'latest_date': latest['date'].strftime('%Y-%m-%d'),
        }

        # Add market cap and margin-to-cap ratio
        if '市值_億元' in latest.index and pd.notna(latest['市值_億元']) and latest['市值_億元'] > 0:
            changes['market_cap'] = latest['市值_億元']
            changes['margin_to_cap_ratio'] = (latest['融資_餘額_億'] / latest['市值_億元']) * 100
            changes['has_market_cap'] = True
        else:
            changes['market_cap'] = None
            changes['margin_to_cap_ratio'] = None
            changes['has_market_cap'] = False

        # Day-over-day change
        if prev_day is not None:
            changes['dod_change'] = latest['融資_餘額_億'] - prev_day['融資_餘額_億']
            changes['dod_pct'] = (changes['dod_change'] / prev_day['融資_餘額_億'] * 100) if prev_day['融資_餘額_億'] > 0 else 0 

        # Week-over-week change
        if prev_week is not None:
            changes['wow_change'] = latest['融資_餘額_億'] - prev_week['融資_餘額_億']
            changes['wow_pct'] = (changes['wow_change'] / prev_week['融資_餘額_億'] * 100) if prev_week['融資_餘額_億'] > 0 else 0

        # Month-over-month change
        if prev_month is not None:
            changes['mom_change'] = latest['融資_餘額_億'] - prev_month['融資_餘額_億']
            changes['mom_pct'] = (changes['mom_change'] / prev_month['融資_餘額_億'] * 100) if prev_month['融資_餘額_億'] > 0 else 0

        # Historical extremes
        changes['max_balance'] = df['融資_餘額_億'].max()
        changes['min_balance'] = df['融資_餘額_億'].min()
        changes['avg_balance'] = df['融資_餘額_億'].mean()
        changes['std_balance'] = df['融資_餘額_億'].std()

        return changes

    def calculate_recent_weekly_change_pct(self, stock_code: str, weeks: int) -> Optional[float]:
        """Calculate recent weekly margin balance change percentage."""
        change = self.calculate_recent_weekly_change(stock_code, weeks)
        if not change or change.get('pct') is None:
            return None
        return change['pct']

    def calculate_recent_weekly_change(self, stock_code: str, weeks: int) -> Optional[Dict[str, float]]:
        """Calculate recent weekly margin balance change (amount and percentage)."""
        if self.margin_weekly_df is None or self.margin_weekly_df.empty:
            return None

        weekly_data = self.margin_weekly_df[self.margin_weekly_df['stock_code'] == stock_code].copy()
        if weekly_data.empty:
            return None

        def parse_week_date(week_str: str):
            try:
                year_part = week_str[:2]
                week_part = week_str[3:]
                year = int('20' + year_part)
                week = int(week_part)
                return pd.to_datetime(f'{year}-W{week:02d}-1', format='%Y-W%W-%w')
            except Exception:
                return pd.NaT

        weekly_data['date'] = weekly_data['期別'].apply(parse_week_date)
        weekly_data = weekly_data.dropna(subset=['date'])
        if weekly_data.empty:
            return None

        # Calculate weekly margin balance in 億元
        if stock_code == '0000':
            if '融資_使用率_pct' not in weekly_data.columns:
                return None
            weekly_data['融資_餘額_億'] = pd.to_numeric(weekly_data['融資_使用率_pct'], errors='coerce')
        else:
            weekly_data['融資_餘額_張'] = pd.to_numeric(weekly_data.get('融資_餘額_張'), errors='coerce')
            weekly_data['收盤_價格_元'] = pd.to_numeric(weekly_data.get('收盤_價格_元'), errors='coerce')
            weekly_data['融資_餘額_億'] = (weekly_data['融資_餘額_張'] * weekly_data['收盤_價格_元'] * 1000) / 1e8

        weekly_data = weekly_data.dropna(subset=['融資_餘額_億'])
        if len(weekly_data) <= weeks:
            return None

        weekly_data = weekly_data.sort_values('date', ascending=False)
        latest = weekly_data.iloc[0]['融資_餘額_億']
        prev = weekly_data.iloc[weeks]['融資_餘額_億']
        if prev <= 0:
            return None

        change = latest - prev
        pct = round(change / prev * 100, 2)
        return {'change': change, 'pct': pct}

    def prepare_chart_data_3year(self, stock_code: str, stock_data: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare 4-year range chart data by combining daily and weekly data
        - Recent 1 year (or available daily range): Use daily data for fine granularity
        - 1-4 years ago: Use weekly data for broader coverage
        - Total range: 4 years (consistent across all stocks)
        """
        # Get the latest date from daily data
        latest_date = stock_data['date'].max()
        daily_start_available = stock_data['date'].min()

        # Target cutoff is 1 year ago
        target_daily_cutoff = latest_date - pd.Timedelta(days=365)

        # The actual split point is the LATER of the target cutoff and the available data start
        # This ensures we use weekly data to fill any gap if daily data is shorter than 1 year
        split_date = max(target_daily_cutoff, daily_start_available)

        # Prepare daily data (from split_date onwards)
        recent_daily = stock_data[stock_data['date'] >= split_date].copy()

        # Track combined data
        combined_datasets = []
        combined_datasets.append(recent_daily)

        # Prepare weekly data (1-4 years ago)
        if self.margin_weekly_df is not None and not self.margin_weekly_df.empty:
            weekly_data = self.margin_weekly_df[self.margin_weekly_df['stock_code'] == stock_code].copy()

            if not weekly_data.empty:
                # Parse weekly date format (e.g., '21W03' -> week 3 of 2021)
                def parse_week_date(week_str):
                    try:
                        # Format: '26W02' means year 2026, week 02
                        year_part = week_str[:2]
                        week_part = week_str[3:]  # After 'W'
                        year = int('20' + year_part)
                        week = int(week_part)
                        # Convert to date (Monday of that week)
                        return pd.to_datetime(f'{year}-W{week:02d}-1', format='%Y-W%W-%w')
                    except:
                        return pd.NaT

                weekly_data['date'] = weekly_data['期別'].apply(parse_week_date)
                weekly_data = weekly_data.dropna(subset=['date'])

                # Filter weekly data for 1-4 years ago (limit to 4-year total range)
                weekly_cutoff_start = latest_date - pd.Timedelta(days=365 * 4)
                weekly_cutoff_end = split_date  # Use split_date to ensure continuity

                historical_weekly = weekly_data[
                    (weekly_data['date'] >= weekly_cutoff_start) &
                    (weekly_data['date'] < weekly_cutoff_end)
                ].copy()

                # Calculate margin balance in 億元 for weekly data
                if stock_code == '0000':
                    # Market index: in weekly data, the column named '融資_使用率_pct' actually contains margin balance in 億元  
                    # This is a quirk of GoodInfo's data format for market index
                    if '融資_使用率_pct' in historical_weekly.columns:
                        historical_weekly['融資_餘額_億'] = historical_weekly['融資_使用率_pct']
                        logger.info(f"Using weekly data for market index {stock_code}: {len(historical_weekly)} weeks")
                    else:
                        logger.warning(f"Weekly data missing 融資_使用率_pct column for {stock_code}")
                        return stock_data.copy()
                else:
                    # Individual stocks
                    historical_weekly['融資_餘額_億'] = (
                        historical_weekly['融資_餘額_張'] * historical_weekly['收盤_價格_元'] * 1000
                    ) / 1e8

                # Add market cap to weekly data if available
                if self.company_info_df is not None and not self.company_info_df.empty:
                    if stock_code == '0000':
                        historical_weekly['市值_億元'] = self.total_market_cap
                    else:
                        company_info = self.company_info_df[self.company_info_df['代號'] == stock_code]
                        if not company_info.empty and '市值_億元' in company_info.columns:
                            historical_weekly['市值_億元'] = company_info.iloc[0]['市值_億元']

                # Select common columns
                common_cols = ['date', '收盤_價格_元', '融資_餘額_億', '市值_億元', 'company_name']
                existing_cols = [col for col in common_cols if col in historical_weekly.columns]
                combined_datasets.append(historical_weekly[existing_cols])

        # NOTE: Monthly data integration is disabled to maintain consistent 4-year range across all stocks
        # If longer historical data is needed, it can be enabled here with appropriate date filtering

        # Combine all datasets
        if len(combined_datasets) > 1:
            combined = pd.concat(combined_datasets, ignore_index=True)
            combined = combined.sort_values('date').reset_index(drop=True)
            return combined
        else:
            # Only daily data available
            return stock_data.copy()

    def export_interactive_json(self, stock_code: str, df: pd.DataFrame, output_dir: Path):
        """
        Export data for interactive chart
        Format: [[timestamp_ms, value], ...]
        """
        try:
            # Ensure df is sorted by date ascending
            df = df.sort_values('date')
            
            # Prepare data: convert date to timestamp in milliseconds
            chart_data = []
            for _, row in df.iterrows():
                if pd.notna(row['date']) and pd.notna(row['融資_餘額_億']):
                    timestamp = int(row['date'].timestamp() * 1000)
                    value = float(row['融資_餘額_億'])
                    chart_data.append([timestamp, value])
            
            # Save to JSON
            output_file = output_dir / f"margin_daily-{stock_code}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(chart_data, f)
                
            logger.info(f"Interactive JSON exported: {output_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to export interactive JSON for {stock_code}: {e}")
            return False

    def create_margin_chart(self, stock_code: str, stock_data: pd.DataFrame, output_file: Path) -> bool:
        """
        Create triple-axis margin balance chart with bars and lines
        - Left axis: Black line for closing price (元)
        - Right axis 1: Golden bars for margin balance (億元)
        - Right axis 2: Red line for margin/market-cap ratio (%)
        """
        try:
            safe_echo(f"\nGenerating margin balance visualization chart...")

            # Set up Chinese font (use system fonts)
            plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'Noto Sans CJK TC', 'Noto Sans CJK SC', 'WenQuanYi Zen Hei']
            plt.rcParams['axes.unicode_minus'] = False

            # Diagnostic: Print the font that will be used
            from matplotlib.font_manager import FontProperties
            font = FontProperties(family=plt.rcParams['font.sans-serif'])
            safe_echo(f"Selected font for chart: {font.get_name()}")

            # Create figure with dual axes
            fig, ax1 = plt.subplots(figsize=(20, 10))

            # Prepare TWO datasets:
            # 1. Daily-only data for golden bars (融資餘額)
            # 2. Long-term data for red line (融資餘額/市值) and black line (股價)

            latest_date = stock_data['date'].max()
            daily_start_available = stock_data['date'].min()
            target_daily_cutoff = latest_date - pd.Timedelta(days=365)

            # Use same split logic as prepare_chart_data_3year to ensure visual consistency
            split_date = max(target_daily_cutoff, daily_start_available)

            daily_only_data = stock_data[stock_data['date'] >= split_date].copy().sort_values('date')

            long_term_data = self.prepare_chart_data_3year(stock_code, stock_data)

            company_name = stock_data['company_name'].iloc[0]

            # Long-term data for price line (black) and ratio line (red)
            long_dates = long_term_data['date'].values
            long_closing_prices = long_term_data['收盤_價格_元'].values

            # Daily-only data for yellow bars (日資料)
            daily_dates = daily_only_data['date'].values
            daily_margin_balances = daily_only_data['融資_餘額_億'].values

            # Weekly/Monthly data for green bars (週/月資料 - excluding daily data range)
            weekly_monthly_data = long_term_data[long_term_data['date'] < split_date].copy()
            weekly_monthly_dates = weekly_monthly_data['date'].values
            weekly_monthly_balances = weekly_monthly_data['融資_餘額_億'].values

            # Calculate margin/market-cap ratio from long-term data
            has_ratio_data = False
            long_margin_ratio = None
            if '市值_億元' in long_term_data.columns:
                # Calculate ratio for each data point (using fixed current market cap - limitation noted)
                long_margin_ratio = (long_term_data['融資_餘額_億'] / long_term_data['市值_億元'] * 100).values
                # Check if we have valid ratio data (not all NaN)
                has_ratio_data = not pd.isna(long_margin_ratio).all()

            # Right axis 1: Margin balance bars (green for weekly/monthly, yellow for daily)
            ax2 = ax1.twinx()
            ax2.set_ylabel('融資餘額 (億元)', fontsize=12, fontweight='bold', color='#228B22')
            ax2.tick_params(axis='y', labelcolor='#228B22')

            # Draw green bars for weekly/monthly data (長期歷史)
            if len(weekly_monthly_balances) > 0:
                green_bars = ax2.bar(weekly_monthly_dates, weekly_monthly_balances,
                                    color='#90EE90', alpha=0.85, width=5.0,
                                    label=f'{company_name} 融資餘額 (週/月)', zorder=2)

            # Draw yellow bars for daily data (最近1年)
            if len(daily_margin_balances) > 0:
                yellow_bars = ax2.bar(daily_dates, daily_margin_balances,
                                     color='#FFD700', alpha=0.85, width=1.5,
                                     label=f'{company_name} 融資餘額 (日)', zorder=4)

            # Scale down the bars to make them more realistic (0.25x scale)
            # Calculate max from both datasets
            all_balances = []
            if len(daily_margin_balances) > 0:
                all_balances.extend(daily_margin_balances.tolist())
            if len(weekly_monthly_balances) > 0:
                all_balances.extend(weekly_monthly_balances.tolist())

            if len(all_balances) > 0:
                all_max = max(all_balances)
                # Set y-axis upper limit to 4x of max value to make bars appear smaller (0.25x scale)
                ax2.set_ylim(0, all_max * 4.0)

            # Left axis: Closing price (black line) - LONG-TERM DATA
            color_line = '#000000'
            ax1.set_xlabel('日期', fontsize=12, fontweight='bold')
            ax1.set_ylabel('收盤價 (元)', fontsize=12, fontweight='bold', color=color_line)
            line1 = ax1.plot(long_dates, long_closing_prices, color=color_line, linewidth=2.5,
                            label=f'{company_name} 收盤價 (長期)', zorder=10)
            ax1.tick_params(axis='y', labelcolor=color_line)
            ax1.grid(axis='y', alpha=0.3, linestyle='--')

            # Right axis 2: Margin/Market-cap ratio (red line) - LONG-TERM DATA
            line2 = []
            if has_ratio_data:
                ax3 = ax1.twinx()
                # Offset the right spine of ax3
                ax3.spines['right'].set_position(('outward', 60))
                color_ratio = '#FF0000'  # Red color
                ax3.set_ylabel('融資餘額/市值 (%) [長期趨勢]', fontsize=12, fontweight='bold', color=color_ratio)
                line2 = ax3.plot(long_dates, long_margin_ratio, color=color_ratio, linewidth=2.5,
                               label='融資餘額/市值 (長期)', zorder=10, linestyle='-', marker='')
                ax3.tick_params(axis='y', labelcolor=color_ratio)
                # Set y-axis limits for ratio to scale it down (0.25x scale)
                if not pd.isna(long_margin_ratio).all():
                    ratio_min = np.nanmin(long_margin_ratio)
                    ratio_max = np.nanmax(long_margin_ratio)
                    ratio_range = ratio_max - ratio_min
                    # To make red line occupy 25% of chart height: expand range by (1/0.25 - 1)/2 = 1.5 on each side
                    ax3.set_ylim(max(0, ratio_min - ratio_range * 1.5), ratio_max + ratio_range * 1.5)

            # Calculate statistics for title (using long-term data for comprehensive view)
            latest_balance = long_term_data['融資_餘額_億'].iloc[-1]
            max_balance = long_term_data['融資_餘額_億'].max()
            min_balance = long_term_data['融資_餘額_億'].min()
            avg_balance = long_term_data['融資_餘額_億'].mean()
            latest_price = long_closing_prices[-1]

            # Add market cap and ratio information if available
            market_cap_info = ""
            if '市值_億元' in long_term_data.columns and pd.notna(long_term_data['市值_億元'].iloc[-1]):
                market_cap = long_term_data['市值_億元'].iloc[-1]
                ratio = (latest_balance / market_cap) * 100

                # Format market cap display
                if market_cap >= 10000:
                    market_cap_display = f"{market_cap/10000:.2f} 兆元"
                else:
                    market_cap_display = f"{market_cap:,.0f} 億元"

                # Determine risk level
                if ratio < 0.3:
                    risk_level = "低風險"
                elif ratio < 0.5:
                    risk_level = "正常"
                elif ratio < 1.0:
                    risk_level = "偏高"
                else:
                    risk_level = "過熱"

                # Removed emojis to prevent font rendering issues in Matplotlib title
                market_cap_info = f'\n市值: {market_cap_display} (當前) | 融資餘額/市值: {ratio:.2f}% ({risk_level}) *註:比率使用當前市值估算'

            # Title with key metrics
            title = (f'{company_name} ({stock_code}): 融資餘額與股價分析\n'
                    f'(長期資料: {len(long_term_data)} 點, {long_term_data["date"].iloc[0].strftime("%Y-%m-%d")} ~ '
                    f'{long_term_data["date"].iloc[-1].strftime("%Y-%m-%d")} | 日資料: 最近1年)\n\n'
                    f'最新融資餘額: {latest_balance:.1f} 億元 | 最新收盤價: {latest_price:.2f} 元 | '
                    f'歷史區間: {min_balance:.1f}~{max_balance:.1f} 億元 | 平均: {avg_balance:.1f} 億元'
                    f'{market_cap_info}')

            plt.title(title, fontsize=13, fontweight='bold', pad=20)

            # Format x-axis dates (show year-month only for 3-year range)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
            ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

            # Combine legends
            lines1, labels1 = ax1.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            all_lines = lines1 + lines2
            all_labels = labels1 + labels2

            # Add ratio line to legend if available
            if has_ratio_data and line2:
                lines3, labels3 = ax3.get_legend_handles_labels()
                all_lines = all_lines + lines3
                all_labels = all_labels + labels3

            ax1.legend(all_lines, all_labels, loc='upper left', fontsize=10)

            # Adjust layout
            plt.tight_layout()

            # Save figure as SVG (vector format for better clarity)
            plt.savefig(output_file, format='svg', bbox_inches='tight')
            safe_echo(f"Chart saved to: {output_file}")

            plt.close()
            return True

        except Exception as e:
            logger.error(f"Failed to create margin chart: {e}")
            return False

    def generate_markdown_report(self, stock_code: str, stock_data: pd.DataFrame) -> str:
        """Generate markdown report for a specific stock"""
        company_name = stock_data['company_name'].iloc[0]
        changes = self.calculate_changes(stock_data)

        if not changes:
            return ""

        # Get Taiwan timezone
        tz = pytz.timezone('Asia/Taipei')
        now_cst = datetime.now(tz)

        # Prepare chart data (last 120 days)
        chart_data = stock_data.head(120).sort_values('date')

        md_content = f"""
---
authors: [wenchiehlee]
date: {now_cst.strftime('%Y-%m-%d')}
categories:
  - 股票
  - 融資餘額
tags:
  - 股票
  - 融資
  - 市場情緒
title: 融資餘額報告 {company_name} ({stock_code})
comments: false
draft: false
description: 融資餘額報告 {company_name} ({stock_code}) - 自動產生
---

# 📈 {company_name} ({stock_code}) 融資餘額報告

!!! info "基本資訊"
    **🏗️ 名稱**: {company_name}
    **🪪 代號**: {stock_code}
    **📅 分析期間**: {chart_data['date'].min().strftime('%Y-%m-%d')} ~ {chart_data['date'].max().strftime('%Y-%m-%d')} (共 {len(stock_data)} 個交易日)
    **🕒 最新資料**: {changes['latest_date']}
    **🕒 更新時間**: {now_cst.strftime('%Y-%m-%d %H:%M:%S')} CST

## 💰 融資餘額現況

| 📊 指標 | 🔢 數值 | 🚦 狀態 |
|:------------:|:----------:|:-------------------:|
| **最新融資餘額** | {changes['latest_balance']:.1f} 億元 ({changes['latest_balance_lots']:,.0f} 張) | - |
| **最新收盤價** | {changes['latest_price']:.2f} 元 | - |
"

        # Add market cap and ratio if available
        if changes.get('has_market_cap', False):
            market_cap = changes['market_cap']
            ratio = changes['margin_to_cap_ratio']

            # Format market cap display
            if market_cap >= 10000:
                market_cap_display = f"{market_cap/10000:.2f} 兆元"
            else:
                market_cap_display = f"{market_cap:,.0f} 億元"

            # Determine risk level based on margin-to-cap ratio
            if ratio < 0.3:
                risk_emoji = "🟢"
                risk_level = "低風險"
            elif ratio < 0.5:
                risk_emoji = "🟡"
                risk_level = "正常"
            elif ratio < 1.0:
                risk_emoji = "🟠"
                risk_level = "偏高"
            else:
                risk_emoji = "🔴"
                risk_level = "過熱"

            md_content += f"| **市值** | {market_cap_display} | - |\n"
            md_content += f"| **融資餘額/市值** | {ratio:.2f}% | {risk_emoji} {risk_level} |\n"

        # Add change metrics if available
        if 'dod_change' in changes:
            dod_emoji = "📈" if changes['dod_change'] > 0 else "📉" if changes['dod_change'] < 0 else "➡️"
            md_content += f"| **日變化 (DoD)** | {changes['dod_change']:+.1f} 億元 ({changes['dod_pct']:+.2f}%) | {dod_emoji} |\n"

        if 'wow_change' in changes:
            wow_emoji = "📈" if changes['wow_change'] > 0 else "📉" if changes['wow_change'] < 0 else "➡️"
            md_content += f"| **週變化 (WoW)** | {changes['wow_change']:+.1f} 億元 ({changes['wow_pct']:+.2f}%) | {wow_emoji} |\n"

        two_week_change = self.calculate_recent_weekly_change(stock_code, weeks=2)
        if two_week_change:
            two_week_emoji = "📈" if two_week_change['change'] > 0 else "📉" if two_week_change['change'] < 0 else "➡️"
            md_content += (
                f"| **兩週變化 (2Wo2W)** | {two_week_change['change']:+.1f} 億元 "
                f"({two_week_change['pct']:+.2f}%) | {two_week_emoji} |\n"
            )

        four_week_change = self.calculate_recent_weekly_change(stock_code, weeks=4)
        if four_week_change:
            four_week_emoji = "📈" if four_week_change['change'] > 0 else "📉" if four_week_change['change'] < 0 else "➡️"
            md_content += (
                f"| **月變化 (MoM)** | {four_week_change['change']:+.1f} 億元 "
                f"({four_week_change['pct']:+.2f}%) | {four_week_emoji} |\n"
            )

        # JSON file path for the chart
        json_filename = f"margin_daily-{stock_code}.json"

        md_content += f"""

---

## 📊 歷史統計

| 📊 指標 | 🔢 數值 |
|:------------:|:----------:|
| **歷史最高** | {changes['max_balance']:.1f} 億元 |
| **歷史最低** | {changes['min_balance']:.1f} 億元 |
| **平均值** | {changes['avg_balance']:.1f} 億元 |
| **標準差** | {changes['std_balance']:.1f} 億元 |
| **當前相對位置** | {((changes['latest_balance'] - changes['min_balance']) / (changes['max_balance'] - changes['min_balance']) * 100):.1f}% |

---

## 📈 融資餘額趨勢圖

<div class="chart-container" style="text-align: center; margin: 20px 0;" markdown="1">
<div class="margin-chart" data-url="../{json_filename}" data-title="融資餘額"></div>
</div>

---

## 📋 詳細歷史記錄 (最近30日)

<table class="sortable-table">
<thead>
<tr>
<th markdown="span">📅 日期</th>
<th markdown="span">💸 收盤價(元)</th>
<th markdown="span">📊 漲跌(元)</th>
<th markdown="span">📈 漲跌(%)</th>
<th markdown="span">📦 融資餘額(億元)</th>
<th markdown="span">📦 融資餘額(張)</th>
<th markdown="span">↕️ 融資增減(張)</th>
<th markdown="span">📊 融券餘額(張)</th>
<th markdown="span">⚖️ 券資比(%)</th>
</tr>
</thead>
<tbody>
"

        # Add recent 30 days data
        for _, row in stock_data.head(30).iterrows():
            change_emoji = "🔺" if row['漲跌_價格_元'] > 0 else "🔻" if row['漲跌_價格_元'] < 0 else "➖"
            margin_change_emoji = "📈" if row.get('融資_增減_張', 0) > 0 else "📉" if row.get('融資_增減_張', 0) < 0 else "➡️"   

            md_content += f"""<tr>
<td>{row['date'].strftime('%Y-%m-%d')}</td>
<td>{row['收盤_價格_元']:.2f}</td>
<td>{change_emoji} {row['漲跌_價格_元']:+.2f}</td>
<td>{row.get('漲跌_pct', 0):+.2f}%</td>
<td>{row['融資_餘額_億']:.1f}</td>
<td>{row['融資_餘額_張']:,.0f}</td>
<td>{margin_change_emoji} {row.get('融資_增減_張', 0):+,.0f}</td>
<td>{row.get('融券_餘額_張', 0):,.0f}</td>
<td>{row.get('券資比_pct', 0):.2f}%</td>
</tr>
"""

        md_content += """
</tbody>
</table>

---

## ℹ️ 資料來源與方法

!!! note "資料來源說明"
    - **主要來源**: `raw_margin_daily.csv` (Type 13: ShowMarginChart)
    - **資料頻率**: 每日更新
    - **資料範圍**: 近1年交易日資料

!!! info "報告元資訊"
    - **報告產生時間**: """ + now_cst.strftime('%Y-%m-%d %H:%M:%S') + f""
    - **分析期間**: {len(stock_data)} 個交易日
    - **資料來源**: Stage 1 Raw Margin Daily Data

---

<div class="result" markdown>

:material-information-outline: **本報告僅供參考，投資決策請審慎評估**

</div>
"""

        return md_content

    def generate_report(self, stock_code: str) -> bool:
        """Generate report for a specific stock"""
        logger.info(f"Generating margin daily report for stock {stock_code}")

        stock_data = self.prepare_stock_data(stock_code)
        if stock_data is None:
            return False

        # Generate SVG chart
        chart_file = self.output_dir / f"margin_daily-{stock_code}.svg"
        chart_success = self.create_margin_chart(stock_code, stock_data, chart_file)
        if not chart_success:
            logger.warning(f"Failed to generate chart for stock {stock_code}, continuing with report")

        # Export data for interactive chart
        self.export_interactive_json(stock_code, stock_data, self.output_dir)

        # Generate markdown content
        md_content = self.generate_markdown_report(stock_code, stock_data)
        if not md_content:
            return False

        # Write to file
        output_file = self.output_dir / f"stage2-cleaning-margin_daily-report-{stock_code}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)

        logger.info(f"Report generated: {output_file}")
        return True

    def generate_summary_report(self, generated_stocks: List[str]) -> bool:
        """Generate summary report listing all individual stock reports"""
        if not generated_stocks:
            logger.warning("No reports generated, skipping summary report")
            return False

        logger.info(f"Generating summary report for {len(generated_stocks)} stocks")

        taipei_tz = pytz.timezone('Asia/Taipei')
        now_cst = datetime.now(taipei_tz)

        # Collect stock information
        stock_info_list = []
        for stock_code in sorted(generated_stocks):
            # Use prepare_stock_data to get processed data (with calculated columns and parsed dates)
            stock_data = self.prepare_stock_data(stock_code)
            if stock_data is None or stock_data.empty:
                continue

            # Handle company name for market index
            if stock_code == '0000':
                company_name = "台灣加權指數"
            else:
                company_name = stock_data['company_name'].iloc[0]

            latest_data = stock_data.iloc[0] # stock_data is sorted descending by date
            latest_balance = latest_data.get('融資_餘額_億', 0)
            latest_balance = 0 if pd.isna(latest_balance) else latest_balance
            latest_price = latest_data.get('收盤_價格_元', 0)
            latest_price = 0 if pd.isna(latest_price) else latest_price

            # Use parsed date
            latest_date = latest_data['date'].strftime('%Y-%m-%d') if pd.notna(latest_data['date']) else "N/A"

            # Get market cap and ratio if available
            market_cap_display = "N/A"
            ratio_display = "N/A"
            risk_level = "-"

            # Check for pre-calculated market cap in stock_data (prepare_stock_data adds it)
            if '市值_億元' in latest_data and pd.notna(latest_data['市值_億元']) and latest_data['市值_億元'] > 0:
                market_cap = latest_data['市值_億元']
                if market_cap >= 10000:
                    market_cap_display = f"{market_cap/10000:.2f} 兆元"
                else:
                    market_cap_display = f"{market_cap:.1f} 億元"

                if latest_balance > 0:
                    ratio = (latest_balance / market_cap) * 100
                    ratio_display = f"{ratio:.2f}%"

                    # Risk level
                    if ratio < 0.3:
                        risk_level = "🟢"
                    elif ratio < 0.5:
                        risk_level = "🟡"
                    elif ratio < 1.0:
                        risk_level = "🟠"
                    else:
                        risk_level = "🔴"

            change_4w_pct = self.calculate_recent_weekly_change_pct(stock_code, weeks=4)
            change_2w_pct = self.calculate_recent_weekly_change_pct(stock_code, weeks=2)

            stock_info_list.append({
                'code': stock_code,
                'name': company_name,
                'balance': latest_balance,
                'change_4w_pct': change_4w_pct,
                'change_2w_pct': change_2w_pct,
                'price': latest_price,
                'date': latest_date,
                'market_cap': market_cap_display,
                'ratio': ratio_display,
                'risk': risk_level
            })

        # Generate markdown content
        md_content = f"""
---
authors: [wenchiehlee]
date: {now_cst.strftime('%Y-%m-%d')}
categories:
  - 股票
  - 融資餘額
  - 彙總報告
tags:
  - 股票
  - 融資
  - 市場情緒
  - 彙總
title: 融資餘額報告彙總
comments: false
draft: false
description: 融資餘額報告彙總 - 包含所有股票的融資餘額分析報告
---

# 📈 融資餘額報告彙總

!!! info "報告資訊"
    **📅 產生時間**: {now_cst.strftime('%Y-%m-%d %H:%M:%S')} CST
    **🔢 報告數量**: {len(stock_info_list)} 支股票
    **🔍 資料來源**: Stage 1 Raw Margin Daily Data

---

## 📋 所有股票融資餘額報告清單

<table class="sortable-table">
<thead>
<tr>
<th markdown="span">🪪 代號</th>
<th markdown="span">🏗️ 名稱</th>
<th markdown="span">📦 融資餘額(億元)</th>
<th markdown="span">📉 近四周融資變化</th>
<th markdown="span">📉 近兩周融資變化</th>
<th markdown="span">💸 收盤價(元)</th>
<th markdown="span">🏦 市值</th>
<th markdown="span">📊 比率</th>
<th markdown="span">🚦 風險</th>
<th markdown="span">📅 最新日期</th>
</tr>
</thead>
<tbody>
"

        # Add rows for each stock
        for info in stock_info_list:
            # Construct link according to requirement: ../folder/filename/ (no .md)
            report_link = f"../stage2-cleaning-margin_daily-report/stage2-cleaning-margin_daily-report-{info['code']}/"
            change_4w = "-" if info['change_4w_pct'] is None else f"{info['change_4w_pct']:+.2f}%"
            change_2w = "-" if info['change_2w_pct'] is None else f"{info['change_2w_pct']:+.2f}%"
            md_content += f"""<tr>
<td markdown="span">[**{info['code']}**]({report_link})</td>
<td>{info['name']}</td>
<td>{info['balance']:.1f}</td>
<td>{change_4w}</td>
<td>{change_2w}</td>
<td>{info['price']:.2f}</td>
<td>{info['market_cap']}</td>
<td>{info['ratio']}</td>
<td>{info['risk']}</td>
<td>{info['date']}</td>
</tr>
"""

        md_content += """
</tbody>
</table>

---

## ℹ️ 風險等級說明

| 等級 | 比率範圍 | 說明 |
|:---:|:---:|:---:|
| 🟢 | < 0.3% | 低風險 - 融資使用率低 |
| 🟡 | 0.3% - 0.5% | 正常 - 融資使用率正常 |
| 🟠 | 0.5% - 1.0% | 偏高 - 融資使用率偏高，需注意 |
| 🔴 | > 1.0% | 過熱 - 融資使用率過高，風險較大 |

---

<div class="result" markdown>

:material-information-outline: **本報告僅供參考，投資決策請審慎評估**

</div>
"""

        # Write summary report
        with open(self.summary_output, 'w', encoding='utf-8') as f:
            f.write(md_content)

        logger.info(f"Summary report generated: {self.summary_output}")
        return True

    def run(self, stock_code: Optional[str] = None, all_stocks: bool = False) -> bool:
        """Main execution method"""
        # Load data
        self.margin_df = self.load_margin_data()
        self.margin_weekly_df = self.load_margin_weekly_data()
        self.margin_monthly_df = self.load_margin_monthly_data()
        self.company_info_df = self.load_company_info()

        if stock_code:
            # Single stock report
            return self.generate_report(stock_code)
        elif all_stocks:
            # All stocks reports
            unique_stocks = self.margin_df['stock_code'].unique()
            success_count = 0
            generated_stocks = []
            for code in unique_stocks:
                if self.generate_report(code):
                    success_count += 1
                    generated_stocks.append(code)
            logger.info(f"Generated {success_count}/{len(unique_stocks)} reports successfully")

            # Generate summary report
            if generated_stocks:
                self.generate_summary_report(generated_stocks)

            return success_count > 0
        else:
            raise ValueError("Must specify either --stock-code or --all-stocks")


@click.command()
@click.option('--stock-code', '-s', type=str, help='Specific stock code to analyze (e.g., "0000" for Taiwan Weighted Index)')    
@click.option('--all-stocks', '-a', is_flag=True, help='Generate reports for all stocks')
@click.option('--input-dir', '-i', type=str, default='data/stage1_raw/',
              help='Input directory containing raw CSV files')
@click.option('--output-dir', '-o', type=str,
              default='data/stage2_cleaned/stage2-cleaning-margin_daily-report/',
              help='Output directory for individual reports')
@click.option('--summary-output', type=str,
              default='data/stage2_cleaned/stage2-cleaning-margin_daily-report-all.md',
              help='Summary report output path')
@click.option('--min-days', type=int, default=30,
              help='Minimum days of data required to generate report')
@click.option('--debug', is_flag=True, help='Enable debug logging')
def main(stock_code: str, all_stocks: bool, input_dir: str,
         output_dir: str, summary_output: str, min_days: int, debug: bool):
    """
    Generate comprehensive margin financing daily reports

    Examples:
        # Generate report for Taiwan Weighted Index (0000)
        python stage2_data_cleaning_margin_daily.py -s 0000

        # Generate report for specific stock
        python stage2_data_cleaning_margin_daily.py -s 2330

        # Generate reports for all stocks
        python stage2_data_cleaning_margin_daily.py -a
    """
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)

    if not stock_code and not all_stocks:
        safe_echo("Error: Must specify either --stock-code or --all-stocks")
        return

    try:
        generator = MarginDailyReportGenerator(
            input_dir=input_dir,
            output_dir=output_dir,
            summary_output=summary_output,
            min_days=min_days
        )

        success = generator.run(stock_code=stock_code, all_stocks=all_stocks)

        if success:
            safe_echo(f"✅ Margin daily report generation completed successfully")
        else:
            safe_echo(f"⚠️ Margin daily report generation completed with warnings")

    except Exception as e:
        logger.error(f"Failed to generate margin daily report: {e}", exc_info=True)
        safe_echo(f"❌ Error: {e}")
        raise


if __name__ == '__main__':
    main()
