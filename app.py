from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from data_analytics.analysis import build_dashboard_data, load_sales_data, summarize_sales


st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")
st.title("Sales Analytics Dashboard")

with st.spinner("Loading analytics data..."):
    df = load_sales_data(ROOT / "data" / "sales.csv")
    summary = summarize_sales(df)
    dashboard_data = build_dashboard_data(df)

st.metric("Total Revenue", f"${summary['total_revenue']:,.0f}")
st.metric("Total Units Sold", f"{summary['total_units_sold']}")
st.metric("Top Region", summary["top_region"])
st.metric("Average Revenue per Day", f"${summary['average_revenue_per_day']:,.0f}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Revenue by Region")
    st.bar_chart(dashboard_data["region_summary"])
with col2:
    st.subheader("Revenue by Product")
    st.bar_chart(dashboard_data["product_summary"])
