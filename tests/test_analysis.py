from pathlib import Path

from data_analytics.analysis import build_dashboard_data, load_sales_data, summarize_sales


def test_load_sales_data():
    df = load_sales_data(Path("data/sales.csv"))
    assert len(df) == 10
    assert "date" in df.columns


def test_summarize_sales():
    df = load_sales_data(Path("data/sales.csv"))
    summary = summarize_sales(df)
    assert summary["total_units_sold"] == 37
    assert summary["top_region"] == "South"


def test_build_dashboard_data():
    df = load_sales_data(Path("data/sales.csv"))
    dashboard = build_dashboard_data(df)
    assert dashboard["region_summary"].loc["South", "revenue"] == 2950
    assert dashboard["product_summary"].loc["Laptop", "revenue"] == 5600
