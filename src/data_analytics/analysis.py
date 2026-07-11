from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "sales.csv"
OUTPUT_DIR = Path(__file__).resolve().parents[2] / "output"


def load_sales_data(csv_path: str | Path | None = None) -> pd.DataFrame:
    path = Path(csv_path) if csv_path is not None else DATA_PATH
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df


def summarize_sales(df: pd.DataFrame) -> dict[str, float | int | str]:
    revenue = float(df["revenue"].sum())
    units = int(df["units_sold"].sum())
    top_region = str(df.groupby("region")["revenue"].sum().idxmax())
    avg_order_value = float(df["revenue"].mean())
    return {
        "total_revenue": revenue,
        "total_units_sold": units,
        "top_region": top_region,
        "average_revenue_per_day": avg_order_value,
    }


def build_dashboard_data(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    region_summary = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
    product_summary = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
    return {
        "region_summary": region_summary.to_frame(name="revenue"),
        "product_summary": product_summary.to_frame(name="revenue"),
    }


def create_visualizations(df: pd.DataFrame, output_dir: str | Path | None = None) -> None:
    output_path = Path(output_dir) if output_dir is not None else OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid")

    daily_revenue = df.groupby("date")["revenue"].sum()
    plt.figure(figsize=(8, 4))
    daily_revenue.plot(marker="o")
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(output_path / "daily_revenue.png")
    plt.close()

    region_summary = df.groupby("region")["revenue"].sum().sort_values()
    plt.figure(figsize=(8, 4))
    region_summary.plot(kind="bar", color="steelblue")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(output_path / "revenue_by_region.png")
    plt.close()


def run_analysis(csv_path: str | Path | None = None, output_dir: str | Path | None = None) -> dict[str, float | int | str]:
    df = load_sales_data(csv_path)
    summary = summarize_sales(df)
    create_visualizations(df, output_dir)
    return summary
