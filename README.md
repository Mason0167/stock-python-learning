# Stock Selection Engine

A Python-based fundamental stock analysis and screening system that helps identify high-quality, stable companies using different metrics. (For stock learning beginner.)

---

## Learning goals
1. Play with APIs and use different endpoints.
2. Extract columns for calculating metrics.
3. Combine different dataframes or metrics data into a single dataframe.
4. Export results to Excel.
5. Format the Excel with openpyxl package.
6. Create figures with matplotlib package. (Still in progress...)

## Features

- Download financial statements from Financial Modeling Prep (FMP) API
- Clean and normalize income, balance sheet, and cash flow data
- Calculate financial metrics:
  - Profitability (ROE, Net Margin, FCF Margin)
  - Growth (Revenue YoY, NI YoY, EPS YoY, EPS CAGR)
  - Efficiency (Total Asset Turnover)
  - Leverage (Equity Multiplier, Debt Burden Ratio)
  - Valuation (PE, PB, PSR, PEG)
- Perform DuPont ROE decomposition
- Export all results to Excel for analysis
