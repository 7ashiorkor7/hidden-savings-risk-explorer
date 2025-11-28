import streamlit as st
import os
import requests
import sqlite3

from scripts.analyze_procurement import (
    analyze_top_suppliers,
    analyze_top_categories,
    analyze_monthly_trends,
    analyze_supplier_concentration,
    analyze_spend_volatility,
    analyze_maverick_spend,
    analyze_long_tail_suppliers
)

DB_URL = "https://finnishprocurementdb.s3.eu-north-1.amazonaws.com/procurement.db"
LOCAL_DB_PATH = "procurement.db"   

def ensure_db():
    """Download DB from S3 when running on Streamlit Cloud."""
    if not os.path.exists(LOCAL_DB_PATH):
        st.info("Downloading procurement database from S3...")
        try:
            response = requests.get(DB_URL)
            response.raise_for_status()
            with open(LOCAL_DB_PATH, "wb") as f:
                f.write(response.content)
            st.success("Database downloaded successfully!")
        except Exception as e:
            st.error(f"Failed to download DB: {e}")
            st.stop()

ensure_db()


# Streamlit App
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
    df, fig = analyze_top_suppliers(LOCAL_DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Top Categories
with tabs[1]:
    df, fig = analyze_top_categories(LOCAL_DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Monthly Trends
with tabs[2]:
    df, fig = analyze_monthly_trends(LOCAL_DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Supplier Concentration
with tabs[3]:
    df, fig = analyze_supplier_concentration(LOCAL_DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Spend Volatility
with tabs[4]:
    df, fig = analyze_spend_volatility(LOCAL_DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)

# Maverick Spend
with tabs[5]:
    total, fig = analyze_maverick_spend(LOCAL_DB_PATH)
    if total:
        st.write(f"Total Unclassified Spend: €{total:,.2f}")
        st.pyplot(fig)
    else:
        st.write("No Maverick / Unclassified Spend found.")

# Long-tail Suppliers
with tabs[6]:
    df, fig = analyze_long_tail_suppliers(LOCAL_DB_PATH)
    st.dataframe(df)
    st.pyplot(fig)
