# Stock Selection Engine

A Python-based fundamental stock analysis and screening system that helps identify high-quality companies using different metrics.

This project is designed to be:
- Data-driven
- Reproducible
- Extensible for quantitative research and backtesting

---

## Features

- Download financial statements from Financial Modeling Prep (FMP) API
- Clean and normalize income, balance sheet, and cash flow data
- Calculate professional-grade financial metrics:
  - Profitability (ROE, Net Margin, FCF Margin)
  - Growth (Revenue YoY, EPS YoY, EPS CAGR)
  - Efficiency (Asset Turnover)
  - Leverage (Equity Multiplier)
  - Valuation (PE, PB, PSR, PEG)
- Perform DuPont ROE decomposition
- Export all results to Excel for analysis
