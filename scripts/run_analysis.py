from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from data_analytics.analysis import run_analysis


if __name__ == "__main__":
    summary = run_analysis()
    print("Analysis complete")
    print(summary)
