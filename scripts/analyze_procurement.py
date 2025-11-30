import pandas as pd
import plotly.express as px

def load_data(csv_url):
    df = pd.read_csv(csv_url, sep=';', encoding='utf-8')
    df['tiliointisumma'] = pd.to_numeric(df['tiliointisumma'], errors='coerce')
    df['tositepvm'] = pd.to_datetime(df['tositepvm'], errors='coerce')
    return df

def analyze_top_suppliers(df, top_n=10):
    top = df.groupby('toimittaja_nimi')['tiliointisumma'].sum().nlargest(top_n).reset_index()
    fig = px.bar(top, x='toimittaja_nimi', y='tiliointisumma', title='Top Suppliers')
    return top, fig

def analyze_top_categories(df, top_n=10):
    top = df.groupby('hankintakategoria')['tiliointisumma'].sum().nlargest(top_n).reset_index()
    fig = px.bar(top, x='hankintakategoria', y='tiliointisumma', title='Top Categories')
    return top, fig

def analyze_monthly_trends(df):
    monthly = df.groupby(df['tositepvm'].dt.to_period('M'))['tiliointisumma'].sum().reset_index()
    monthly['tositepvm'] = monthly['tositepvm'].dt.to_timestamp()
    fig = px.line(monthly, x='tositepvm', y='tiliointisumma', title='Monthly Spend Trends', markers=True)
    return monthly, fig

def analyze_supplier_concentration(df):
    concentration = df.groupby('toimittaja_nimi')['tiliointisumma'].sum().sort_values(ascending=False).reset_index()
    fig = px.pie(concentration.head(10), names='toimittaja_nimi', values='tiliointisumma', title='Top 10 Supplier Concentration')
    return concentration, fig

def analyze_spend_volatility(df):
    monthly = df.groupby(df['tositepvm'].dt.to_period('M'))['tiliointisumma'].sum()
    volatility = monthly.pct_change().fillna(0) * 100
    vol_df = volatility.reset_index()
    vol_df['tositepvm'] = vol_df['tositepvm'].dt.to_timestamp()
    fig = px.line(vol_df, x='tositepvm', y='tiliointisumma', title='Monthly Spend Volatility (%)', markers=True)
    return vol_df, fig

def analyze_maverick_spend(df):
    maverick = df[df['hankintakategoria'].isna()]
    total = maverick['tiliointisumma'].sum()
    fig = px.bar(maverick.groupby('toimittaja_nimi')['tiliointisumma'].sum().reset_index(),
                 x='toimittaja_nimi', y='tiliointisumma', title='Maverick / Unclassified Spend')
    return total, fig

def analyze_long_tail_suppliers(df, threshold=0.01):
    supplier_total = df.groupby('toimittaja_nimi')['tiliointisumma'].sum()
    total_sum = supplier_total.sum()
    long_tail = supplier_total[supplier_total / total_sum <= threshold].reset_index()
    fig = px.bar(long_tail, x='toimittaja_nimi', y='tiliointisumma', title='Long-tail Suppliers')
    return long_tail, fig
