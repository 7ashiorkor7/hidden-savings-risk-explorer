import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = None


#  Standard Analyses 

def analyze_top_suppliers(db_path, top_n=10):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"""
        SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY toimittaja_nimi
        ORDER BY total_spend DESC
        LIMIT {top_n};
    """, conn)
    conn.close()

    # Plot
    fig, ax = plt.subplots()
    ax.barh(df['toimittaja_nimi'], df['total_spend']/1e6)
    ax.set_xlabel("Total Spend (Millions €)")
    ax.set_title(f"Top {top_n} Suppliers by Total Spend")
    ax.invert_yaxis()

    return df, fig


def analyze_top_categories(db_path, top_n=10):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"""
        SELECT hankintakategoria, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY hankintakategoria
        ORDER BY total_spend DESC
        LIMIT {top_n};
    """, conn)
    conn.close()

    fig, ax = plt.subplots()
    ax.barh(df['hankintakategoria'], df['total_spend']/1e6)
    ax.set_xlabel("Total Spend (Millions €)")
    ax.set_title(f"Top {top_n} Procurement Categories")
    ax.invert_yaxis()

    return df, fig


def analyze_monthly_trends(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("""
        SELECT strftime('%Y-%m', tositepvm) AS month, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY month
        ORDER BY month;
    """, conn)
    conn.close()

    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df['month'], df['total_spend']/1e6, marker='o')
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Spend (Millions €)")
    ax.set_title("Monthly Procurement Spend Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return df, fig


# Hidden Savings & Risk Indicators 

def analyze_supplier_concentration(db_path, top_n=10):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("""
        SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY toimittaja_nimi
        ORDER BY total_spend DESC
    """, conn)
    conn.close()

    top_suppliers = df.head(top_n)
    rest_sum = df['total_spend'][top_n:].sum()
    plot_df = top_suppliers.copy()
    plot_df.loc[len(plot_df)] = ['Other Suppliers', rest_sum]

    fig, ax = plt.subplots()
    ax.pie(plot_df['total_spend'], labels=plot_df['toimittaja_nimi'], autopct='%1.1f%%')
    ax.set_title("Supplier Concentration: Top 10 vs Others")

    return plot_df, fig


def analyze_spend_volatility(db_path, top_n=10):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"""
        SELECT hankintakategoria, MAX(tiliointisumma) - MIN(tiliointisumma) AS spend_range
        FROM procurement_data
        GROUP BY hankintakategoria
        ORDER BY spend_range DESC
        LIMIT {top_n};
    """, conn)
    conn.close()

    fig, ax = plt.subplots()
    ax.barh(df['hankintakategoria'], df['spend_range']/1e3)
    ax.set_xlabel("Spend Range (€ thousands)")
    ax.set_title("Top Categories by Spend Volatility")
    ax.invert_yaxis()

    return df, fig


def analyze_maverick_spend(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("""
        SELECT SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        WHERE hankintakategoria IS NULL OR hankintakategoria = '';
    """, conn)
    conn.close()

    total = df['total_spend'][0]
    fig = None
    if total and total > 0:
        fig, ax = plt.subplots()
        ax.barh(['Unclassified'], [total/1e3])
        ax.set_xlabel("Total Spend (€ thousands)")
        ax.set_title("Maverick / Unclassified Spend")
        plt.tight_layout()

    return total, fig


def analyze_long_tail_suppliers(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("""
        SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY toimittaja_nimi
        ORDER BY total_spend DESC
    """, conn)
    conn.close()

    df['cum_pct'] = df['total_spend'].cumsum() / df['total_spend'].sum()
    tail_suppliers = df[df['cum_pct'] > 0.8]

    fig, ax = plt.subplots()
    ax.barh(tail_suppliers['toimittaja_nimi'], tail_suppliers['total_spend']/1e3)
    ax.set_xlabel("Spend (€ thousands)")
    ax.set_title("Long-tail Supplier Analysis (bottom 20% of spend)")
    ax.invert_yaxis()

    return tail_suppliers, fig
