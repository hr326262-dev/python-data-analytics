from pathlib import Path

from data_analytics.analysis import load_sales_data, summarize_sales


def test_load_sales_data():
    df = load_sales_data(Path("data/sales.csv"))
    assert len(df) == 10
    assert "date" in df.columns


def test_summarize_sales():
    df = load_sales_data(Path("data/sales.csv"))
    summary = summarize_sales(df)
    assert summary["total_units_sold"] == 37
    assert summary["top_region"] == "South"
