# Hidden Savings Risk Explorer – Finnish Public Procurement Analysis
This is a data-driven exploration of Finnish public procurement, designed to uncover spending patterns, key suppliers and potential savings opportunities. Currently, I am learning Finnish and I am curious to work with data that has Finnish words to encourange and challenge myself. ALso, I am curious on how public money is utilised in Finland and how it flows across different organizations. 

## About the Data
I used the publicly available dataset from https://www.avoindata.fi/en which provides detailed procurement invoices from the Finnish central government and selected municipalities (Helsinki, Vantaa, Järvenpää, Forssa) as well as universities and wellbeing services counties.  The data spans multiple years (2016–2025) and includes invoice-level details such as supplier names, procurement units, categories, product/service groups, amounts, and posting dates. Sensitive information is anonymized where required by law. Sensitive information is anonymized based on Finnish law. Data is updated roughly monthly and contains ~1.7 million rows.

It includes fields such as:
* Supplier name (toimittaja_nimi)
* Procurement category (hankintakategoria)
* Invoice booking amount (tiliointisumma)
* Posting date (tositepvm)

This dataset is large and real-world, making it ideal for building a structured procurement analytics pipeline.

## Problem Statement
Public procurement datasets are large, noisy, and complex. Organizations need visibility into:
* Supplier concentration risks
* Spend trends
* Category-level cost drivers
* Potential savings opportunities
* Unclassified spend

The challenge: How  millions of raw rows be transformed into insights that support better sourcing decisions? This project builds an end-to-end workflow to do exactly that.

## Key Questions
* Which suppliers contribute the most to total spend?
* Which procurement categories and product/service groups are the largest cost drivers?
* Are there anomalies, redundancies, or unusually high concentrations of spending?
* Can spending be consolidated to reduce costs or supplier dependency?
* How do trends vary across different procurement units, sectors, and years?

## Tech Stack
* Python – Data processing, analysis, and visualization.
* Pandas – Data manipulation and aggregation.
* SQLite – Scalable storage for large datasets (~1.7M rows).
* Matplotlib – Visualizations for trends and anomalies.

## Data Ingestion
Spend analytics beings with a reliable data ingestion since scaling is dependent on that. I built a Python ETL that loads raw CSV data into a SQLite mini-warehouse. This ensured that the data can be queried repeatedly and efficiently. 

## Data Understanding
I assessed the data to know what cleaning steps I would have to take. I checked column completeness, date and numeric field quality, any patterns in suppliers, categoried and spend sizes.

## Data Cleaning and Standardization
* Convert date fields into a standard format
* Standardize supplier names
* Identify missing or suspicious values
* Prepare category fields for classification

## Exploratory Spend Analysis
I started exploring the business questions I had and executing SQL analytics.
* Top suppliers by spend - Reveals dependency risks and negotiation opportunities.
* Top procurement categories - Shows where budgets are actually going and where optimization is possible.
* Monthly spend trends - Helps detect seasonality, budget cycles, or abnormalities.

<!-- The goal of this project is to identify potential savings and risk areas in procurement data and generate actionable insights. Raw data is transformed into meaningful outputs, demonstrating my skills in data engineering, SQL, Python, and business consulting. -->
