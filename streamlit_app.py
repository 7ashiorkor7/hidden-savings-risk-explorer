import streamlit as st
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

from analyze_procurement import (
    analyze_top_suppliers,
    analyze_top_categories,
    analyze_monthly_trends,
    analyze_supplier_concentration,
    analyze_spend_volatility,
    analyze_maverick_spend,
    analyze_long_tail_suppliers
)

DB_PATH = os.path.join(os.path.dirname(__file__), "procurement.db")

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

# Top Suppliers
with tabs[0]:
    df, fig = analyze_top_suppliers(DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Top Categories
with tabs[1]:
    df, fig = analyze_top_categories(DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Monthly Trends
with tabs[2]:
    df, fig = analyze_monthly_trends(DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Supplier Concentration
with tabs[3]:
    df, fig = analyze_supplier_concentration(DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Spend Volatility
with tabs[4]:
    df, fig = analyze_spend_volatility(DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Maverick / Unclassified Spend
with tabs[5]:
    total, fig = analyze_maverick_spend(DB_PATH)
    if total:
        st.write(f"Total Unclassified Spend: €{total:,.2f}")
        st.pyplot(fig)
    else:
        st.write("No Maverick / Unclassified Spend found.")

# Long-tail Suppliers
with tabs[6]:
    df, fig = analyze_long_tail_suppliers(DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)
