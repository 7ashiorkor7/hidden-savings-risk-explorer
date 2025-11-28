import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = r"C:\Users\nashi\Documents\GitHubProjects\Sievo\hidden-savings-risk-explorer\procurement.db"

def get_connection(db_path=DB_PATH):
    return sqlite3.connect(db_path)

# Basic Procurement Analysis
def analyze_top_suppliers(conn, top_n=10):
    query = f"""
    SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
    FROM procurement_data
    GROUP BY toimittaja_nimi
    ORDER BY total_spend DESC
    LIMIT {top_n};
    """
    df = pd.read_sql(query, conn)
    print(df)
    plt.figure(figsize=(10,6))
    plt.barh(df['toimittaja_nimi'], df['total_spend']/1e6)
    plt.xlabel("Total Spend (Millions €)")
    plt.title(f"Top {top_n} Suppliers by Total Spend")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def analyze_top_categories(conn, top_n=10):
    query = f"""
    SELECT hankintakategoria, SUM(tiliointisumma) AS total_spend
    FROM procurement_data
    GROUP BY hankintakategoria
    ORDER BY total_spend DESC
    LIMIT {top_n};
    """
    df = pd.read_sql(query, conn)
    print(df)
    plt.figure(figsize=(10,6))
    plt.barh(df['hankintakategoria'], df['total_spend']/1e6)
    plt.xlabel("Total Spend (Millions €)")
    plt.title(f"Top {top_n} Procurement Categories")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def analyze_monthly_trends(conn):
    query = """
    SELECT strftime('%Y-%m', tositepvm) AS month, SUM(tiliointisumma) AS total_spend
    FROM procurement_data
    GROUP BY month
    ORDER BY month;
    """
    df = pd.read_sql(query, conn)
    print(df.head(10))
    plt.figure(figsize=(12,6))
    plt.plot(df['month'], df['total_spend']/1e6, marker='o')
    plt.xticks(rotation=45)
    plt.ylabel("Total Spend (Millions €)")
    plt.title("Monthly Procurement Spend Trend")
    plt.tight_layout()
    plt.show()

# Hidden Savings & Risk Indicators 

def analyze_supplier_concentration(conn):
    df = pd.read_sql("""
        SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY toimittaja_nimi
        ORDER BY total_spend DESC
    """, conn)

    top_n = 10
    top_suppliers = df.head(top_n)
    rest_sum = df['total_spend'][top_n:].sum()
    plot_df = top_suppliers.copy()
    plot_df.loc[len(plot_df)] = ['Other Suppliers', rest_sum]

    print("\nSupplier Concentration (Top 10 + Others):")
    print(plot_df)

    plt.figure(figsize=(8,6))
    plt.pie(plot_df['total_spend'], labels=plot_df['toimittaja_nimi'], autopct='%1.1f%%')
    plt.title("Supplier Concentration: Top 10 vs Others")
    plt.show()


def analyze_spend_volatility(conn):
    df = pd.read_sql("""
        SELECT hankintakategoria, MAX(tiliointisumma) - MIN(tiliointisumma) AS spend_range
        FROM procurement_data
        GROUP BY hankintakategoria
        ORDER BY spend_range DESC
        LIMIT 10
    """, conn)

    print("\nTop 10 Categories by Spend Volatility:")
    print(df)

    plt.figure(figsize=(10,6))
    plt.barh(df['hankintakategoria'], df['spend_range']/1e3)
    plt.xlabel("Spend Range (€ thousands)")
    plt.title("Top 10 Categories by Spend Volatility")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def analyze_maverick_spend(conn):
    df = pd.read_sql("""
        SELECT SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        WHERE hankintakategoria IS NULL OR hankintakategoria = ''
    """, conn)

    total = df['total_spend'][0]
    
    if total is None or pd.isna(total) or total == 0:
        print("\nNo Maverick / Unclassified Spend found.")
        return

    print("\nUnclassified Spend:")
    print(total)
    
    plt.figure(figsize=(6,4))
    plt.barh(['Unclassified'], [total/1e3])
    plt.xlabel("Total Spend (€ thousands)")
    plt.title("Unclassified Spend")
    plt.tight_layout()
    plt.show()


def analyze_long_tail_suppliers(conn):
    df = pd.read_sql("""
        SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
        FROM procurement_data
        GROUP BY toimittaja_nimi
        ORDER BY total_spend DESC
    """, conn)

    df['cum_pct'] = df['total_spend'].cumsum() / df['total_spend'].sum()
    tail_suppliers = df[df['cum_pct'] > 0.8]

    print("\nLong-tail Suppliers (bottom 20% of spend):")
    print(tail_suppliers)


if __name__ == "__main__":
    conn = get_connection()
    try:
        analyze_top_suppliers(conn)
        analyze_top_categories(conn)
        analyze_monthly_trends(conn)
        analyze_supplier_concentration(conn)
        analyze_spend_volatility(conn)
        analyze_maverick_spend(conn)
        analyze_long_tail_suppliers(conn)
    finally:
        conn.close()
        print("Database connection closed.")
