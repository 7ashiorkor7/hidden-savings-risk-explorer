import sqlite3
import pandas as pd
import os

def load_procurement_data():
    # Absolute path to CSV
    csv_path = r"C:\Users\nashi\Documents\GitHubProjects\Sievo\hidden-savings-risk-explorer\data\th_data_2025.csv"
    
    # Verify file exists
    if not os.path.exists(csv_path):
        print(f"CSV not found at {csv_path}")
        return
    
    # Load CSV
    df = pd.read_csv(csv_path, sep=";")  # Change sep="," if CSV uses commas
    print(f"CSV loaded successfully: {len(df)} rows, {len(df.columns)} columns")
    
    # Connect to SQLite
    conn = sqlite3.connect(r"C:\Users\nashi\Documents\GitHubProjects\Sievo\hidden-savings-risk-explorer\procurement.db")
    
    # Write to SQL table
    df.to_sql("procurement_data", conn, if_exists="replace", index=False)
    conn.close()
    
    print("Data loaded into SQLite successfully!")

if __name__ == "__main__":
    load_procurement_data()
