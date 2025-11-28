import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db_path = r"C:\Users\nashi\Documents\GitHubProjects\Sievo\hidden-savings-risk-explorer\procurement.db"
conn = sqlite3.connect(db_path)

# Top Suppliers by Spend
query_top_suppliers = """
SELECT toimittaja_nimi, SUM(tiliointisumma) AS total_spend
FROM procurement_data
GROUP BY toimittaja_nimi
ORDER BY total_spend DESC
LIMIT 10;
"""
top_suppliers = pd.read_sql(query_top_suppliers, conn)
print("Top 10 suppliers by total spend:")
print(top_suppliers)


plt.figure(figsize=(10,6))
plt.barh(top_suppliers['toimittaja_nimi'], top_suppliers['total_spend']/1e6)
plt.xlabel("Total Spend (Millions €)")
plt.title("Top 10 Suppliers by Total Spend")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# Top Categories by Spend
query_top_categories = """
SELECT hankintakategoria, SUM(tiliointisumma) AS total_spend
FROM procurement_data
GROUP BY hankintakategoria
ORDER BY total_spend DESC
LIMIT 10;
"""
top_categories = pd.read_sql(query_top_categories, conn)
print("\nTop 10 procurement categories by total spend:")
print(top_categories)


plt.figure(figsize=(10,6))
plt.barh(top_categories['hankintakategoria'], top_categories['total_spend']/1e6)
plt.xlabel("Total Spend (Millions €)")
plt.title("Top 10 Procurement Categories")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# Monthly Spend Trends
query_monthly_trends = """
SELECT strftime('%Y-%m', tositepvm) AS month, SUM(tiliointisumma) AS total_spend
FROM procurement_data
GROUP BY month
ORDER BY month;
"""
monthly_spend = pd.read_sql(query_monthly_trends, conn)
print("\nMonthly Spend Trend (first 10 months):")
print(monthly_spend.head(10))

# Plot
plt.figure(figsize=(12,6))
plt.plot(monthly_spend['month'], monthly_spend['total_spend']/1e6, marker='o')
plt.xticks(rotation=45)
plt.ylabel("Total Spend (Millions €)")
plt.title("Monthly Procurement Spend Trend")
plt.tight_layout()
plt.show()

