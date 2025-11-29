# Hidden Savings Risk Explorer – Finnish Public Procurement Analysis
This is a data-driven exploration of Finnish public procurement, designed to uncover spending patterns, key suppliers and potential savings opportunities. Currently, I am learning Finnish and I am curious to work with data that has Finnish words to encourange and challenge myself. Also, I am curious on how public money is utilised in Finland and how it flows across different organizations. 

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
* Streamlit – Interactive dashboard for exploring top suppliers, categories, monthly trends, and hidden savings & risk indicators.

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

## Supplier Concentration Analysis
Is Finland relying too heavily on a handful of suppliers?

What I did:
* Measured the spend share of top suppliers versus all others
* Identified dependency risks using concentration indicators
* Highlighted opportunities to diversify supplier base

The business value is understanding supplier concentration helps organizations avoid over-reliance on a few vendors, mitigating supply risk and strengthening negotiation power.

## Spend Volatility (Category Instability)
Which procurement categories show unpredictable spending patterns?

What I did:
* Analyzed monthly trend instability
* Identified categories with large spend fluctuations
* Flagged categories that may pose forecasting or budgeting risks

The business value is recognizing volatility enables better planning, improves budgeting accuracy, and informs category management strategies.
  
## Unclassified/Maverick Spend
Where is data quality hiding real costs?

What I did:
* Detected transactions with missing or unclassified categories
* Identified unclassified suppliers or spend outside established procurement rules
* Highlighted potential data quality or compliance issues

The business value is revealing hidden or maverick spend uncovers cost leakages, ensures compliance, and improves transparency in procurement processes.
  
## Long-Tail Supplier Analysis
Is tail spend driving complexity and unnecessary costs?

What I did:
* Mapped the Pareto distribution of supplier spend
* Identified fragmented tail spend suppliers
* Highlighted opportunities for supplier consolidation

The business value is optimizing long-tail spend reduces transaction costs, streamlines supplier management, and unlocks potential savings by consolidating fragmented suppliers.

## Interactive Procurement Dashboard Using Streamlit
To make the procurement insights more interactive and actionable, a Streamlit web app was developed. 
The app allows users to explore the Finnish public procurement data visually and dynamically, helping uncover hidden savings opportunities and potential risks.

### Key Features
#### Tabbed Interface
The dashboard is organized into tabs, each reflecting a core area of analysis:
* Top Suppliers by Spend
* Top Procurement Categories
* Monthly Spend Trends
* Supplier Concentration & Hidden Risks
* Includes Maverick / Unclassified Spend, Spend Volatility, and Long-tail Supplier Analysis.

#### Interactive Visualizations
* Users can view bar charts, line charts, and pie charts for various procurement metrics.
* Each chart is dynamically generated from the SQLite database containing the cleaned procurement data.

#### Business & Consulting Insights
Beyond simple reporting, the dashboard highlights:
* Supplier dependency risks
* Category volatility and unpredictable spikes
* Areas where unclassified or maverick spend could hide costs
* Opportunities for supplier consolidation in long-tail spend

#### Streamlined Workflow
* The dashboard reads directly from the SQLite database generated in load_data.py.
* Database connections are cached efficiently using st.cache_resource, ensuring fast and smooth updates.


