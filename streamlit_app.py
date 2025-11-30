import streamlit as st
from scripts.analyze_procurement import (
    load_data,
    analyze_top_suppliers,
    analyze_top_categories,
    analyze_monthly_trends,
    analyze_supplier_concentration,
    analyze_spend_volatility,
    analyze_maverick_spend,
    analyze_long_tail_suppliers
)

CSV_URL = "https://finnishprocurementdata.s3.eu-north-1.amazonaws.com/th_data_2025.csv"

# Load data once
df = load_data(CSV_URL)

st.title("Finnish Government Procurement Analysis")

tabs = st.tabs([
    "Top Suppliers",
    "Top Categories",
    "Monthly Trends",
    "Supplier Concentration",
    "Spend Volatility",
    "Maverick / Unclassified Spend",
    "Long-tail Suppliers"
])

with tabs[0]:
    top, fig = analyze_top_suppliers(df)
    st.dataframe(top)
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    top, fig = analyze_top_categories(df)
    st.dataframe(top)
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    monthly, fig = analyze_monthly_trends(df)
    st.dataframe(monthly)
    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:
    concentration, fig = analyze_supplier_concentration(df)
    st.dataframe(concentration)
    st.plotly_chart(fig, use_container_width=True)

with tabs[4]:
    vol_df, fig = analyze_spend_volatility(df)
    st.dataframe(vol_df)
    st.plotly_chart(fig, use_container_width=True)

with tabs[5]:
    total, fig = analyze_maverick_spend(df)
    st.write(f"Total Unclassified Spend: €{total:,.2f}")
    st.plotly_chart(fig, use_container_width=True)

with tabs[6]:
    long_tail, fig = analyze_long_tail_suppliers(df)
    st.dataframe(long_tail)
    st.plotly_chart(fig, use_container_width=True)
