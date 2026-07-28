import os
import shutil
import subprocess
import time
import sys
from pathlib import Path

# Reconfigure stdout to use UTF-8 (especially on Windows)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Paths
analyzer_dir = Path("C:/Users/WJLEE/SynologyDrive/NAS/github.com/Python-Actions.GoodInfo.Analyzer")
mkdocs_dir = Path("C:/Users/WJLEE/SynologyDrive/NAS/github.com/mkdocs-investment")

# Mappings (src -> dest relative to their respective project roots)
sync_mappings = [
    # Revenue
    ("data/stage2_cleaned/stage2-cleaning-revenue-report", "docs/reports/stage2-cleaning-revenue-report"),
    ("data/stage2_cleaned/stage2-cleaning-revenue-report-all.md", "docs/reports/stage2-cleaning-revenue-report-all.md"),
    # Dividends
    ("data/stage2_cleaned/stage2-cleaning-dividends-report", "docs/reports/stage2-cleaning-dividends-report"),
    ("data/stage2_cleaned/stage2-cleaning-dividends-report-all.md", "docs/reports/stage2-cleaning-dividends-report-all.md"),
    # Drawdown
    ("data/stage2_cleaned/stage2-cleaning-market-analysis-drawdown-report-all.md", "docs/reports/stage2-cleaning-market-analysis-drawdown-report-all.md"),
    # PE
    ("data/stage2_cleaned/stage2-cleaning-market-analysis-pe-forward-return-report-tr-all.md", "docs/reports/stage2-cleaning-market-analysis-pe-forward-return-report-tr-all.md"),
    ("data/stage2_cleaned/stage2-cleaning-market-analysis-pe-forward-return-report", "docs/reports/stage2-cleaning-market-analysis-pe-forward-return-report"),
    # ROA/ROE
    ("data/stage2_cleaned/stage2-cleaning-roa-roe-report", "docs/reports/stage2-cleaning-roa-roe-report"),
    ("data/stage2_cleaned/stage2-cleaning-roa-roe-report-all.md", "docs/reports/stage2-cleaning-roa-roe-report-all.md"),
    # Margin
    ("data/stage2_cleaned/stage2-cleaning-margin_daily-report", "docs/reports/stage2-cleaning-margin_daily-report"),
    ("data/stage2_cleaned/stage2-cleaning-margin_daily-report-all.md", "docs/reports/stage2-cleaning-margin_daily-report-all.md")
]

commands = [
    ("Revenue Report", ["python", "src/pipelines/revenue_report.py"]),
    ("Dividends Report", ["python", "src/pipelines/dividends_report.py", "-a"]),
    ("ROA/ROE Report", ["python", "src/pipelines/roa_roe_report.py", "--md"]),
    ("Drawdown Report", ["python", "src/pipelines/market_analysis_drawdown_report.py", "-a"]),
    ("PE Forward Return Report", ["python", "src/pipelines/market_analysis_pe_forward_return_report.py", "-a"]),
    ("Margin Daily Report", ["python", "src/pipelines/margin_daily_report.py", "-a"])
]

def run_reports():
    print("=== STARTING REPORT GENERATION ===")
    for name, cmd in commands:
        start_time = time.time()
        print(f"Running {name}...")
        try:
            result = subprocess.run(cmd, cwd=str(analyzer_dir), capture_output=True, text=True, encoding='utf-8', check=True)
            elapsed = time.time() - start_time
            print(f"✅ Finished {name} in {elapsed:.1f}s")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running {name}:")
            print(e.stderr or e.stdout)
            raise e

def sync_files():
    print("\n=== SYNCING FILES TO MKDOCS ===")
    for src_rel, dest_rel in sync_mappings:
        src_path = analyzer_dir / src_rel
        dest_path = mkdocs_dir / dest_rel
        
        if not src_path.exists():
            print(f"⚠️ Source does not exist: {src_path}")
            continue
            
        # Ensure parent directory of destination exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        if src_path.is_dir():
            if dest_path.exists():
                shutil.rmtree(dest_path)
            shutil.copytree(src_path, dest_path)
            print(f"Synced Directory: {src_rel} -> {dest_rel}")
        else:
            if dest_path.exists():
                dest_path.unlink()
            shutil.copy2(src_path, dest_path)
            print(f"Synced File: {src_rel} -> {dest_rel}")

if __name__ == "__main__":
    start = time.time()
    try:
        run_reports()
        sync_files()
        print(f"\n🎉 ALL REPORTS SUCCESSFULLY GENERATED AND SYNCED in {time.time() - start:.1f}s!")
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
