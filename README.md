# Hidden Savings Risk Explorer – Finnish Public Procurement Analysis
You can explore the interactive dashboard here: [Hidden Savings & Risk Explorer](https://hidden-savings-risk-explorer-9tfurtuzd7gftgwbnra6xj.streamlit.app/)

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
* Python & Pandas – Data processing, cleaning, and aggregation (~1.7M rows).
* AWS S3 – Centralized storage for procurement CSV data; allows easy access and scalability.
* Streamlit & Plotly – Interactive dashboard with drill-downs: top suppliers, categories, monthly trends, spend volatility, and hidden savings/risk insights.

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

#### Business & Consulting Insights
Beyond simple reporting, the dashboard highlights:
* Supplier dependency risks
* Category volatility and unpredictable spikes
* Areas where unclassified or maverick spend could hide costs
* Opportunities for supplier consolidation in long-tail spend

#### Streamlined Workflow
* The dashboard reads directly from the CSV stored on AWS S3, eliminating the need for a local database.
* Data loading is cached using st.cache_data, ensuring fast and smooth updates.
* Visualizations are built with Plotly, providing interactive charts for supplier, category, and monthly trend analysis.

## Key Insights
* Helsingin kaupunki, HUS-yhtymä, and Senaatti-kiinteistöt are the top suppliers by total spend in 2025. Spending is concentrated in expert services and ICT-related categories, with noticeable seasonal trends across months. A few suppliers account for most of the procurement, while many smaller vendors form a long-tail. Maverick/unclassified spend is minimal, indicating generally clean and well-categorized data.
* The government’s procurement spending is concentrated in a few key areas. Asiakaspalvelujen ostot (Customer service purchases) leads with €1.33B, followed closely by Rakennusten ja alueiden ylläpito (Building and area maintenance, €1.27B) and ICT-hankinnat (IT purchases, including hardware, software, and services, €1.23B). Other significant categories include Alueet ja väylät (infrastructure), Rakentaminen (construction), and Hallinnolliset palvelut (administrative services), reflecting major investments in public services, infrastructure, and administration. Overall, the bulk of the procurement budget is focused on services, maintenance, IT, and infrastructure rather than smaller miscellaneous purchases.
* The monthly procurement spend shows notable fluctuations across the first ten months of 2025. Spending gradually increased from €728M in January to a peak of €1.08B in May, reflecting heightened activity in spring. After June, expenditure decreased sharply, dropping to around €435M by October, indicating possible seasonal patterns, project completions, or delayed payments. Overall, the data suggests that government procurement is uneven throughout the year, with significant spikes and troughs.
* 

## Recommendations
The government’s procurement is heavily concentrated among a few key suppliers and categories, so fostering closer partnerships with top vendors could unlock efficiencies and cost savings. Planning around seasonal spending spikes will help manage budgets more smoothly, while streamlining smaller, long-tail purchases can reduce administrative overhead. With most spend already well-categorized, the clean data allows for reliable insights and smarter decision-making across services, IT, and infrastructure investments.
