# Convert financial statements to metrics
import pandas as pd
import numpy as np

# Profitability
# Step 4
def calc_roe(income_df, balance_df):
    # ROE = netIncome / totalStockholdersEquity
    merged = pd.merge(income_df, balance_df, on="date")
    merged['ROE'] = (merged['netIncome'] / merged['totalStockholdersEquity']) * 100
    merged['ROE'] = merged['ROE'].round(2)

    return merged[['date', 'ROE']]

# Step 2
def calc_fcf_margin(cashflow_df, income_df):
    # FCF = OCF - CapEx; FCF Margin = FCF / revenue
    merged = pd.merge(cashflow_df, income_df[['date', 'revenue']], on='date')
    merged['FCF'] = merged['operatingCashFlow'] + merged['capitalExpenditure']  # CapEx 是負的，所以加
    merged['FCF_Billions'] = (merged['FCF'] / 1e9).round(2)  

    merged['FCF_Margin'] = merged['FCF'] / merged['revenue']
    merged['FCF_Margin'] = merged['FCF_Margin'].round(2) * 100

    return merged[['date', 'FCF_BILLIONS', 'FCF_Margin']]

# Step 2
def calc_net_margin(income_df):
    # FCF = OCF - CapEx; FCF Margin = FCF / revenue
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['Net_Margin'] = income_df['netIncome'] / income_df['revenue']
    income_df['Net_Margin'] = income_df['Net_Margin'].round(2) * 100

    return income_df[['date', 'Net_Margin']]



# Growth
# Step 3
def calc_revenue_yoy(income_df):
    # Revenue YoY % = (本期revenue − 上期revenue) ÷ 上期revenue × 100
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['Revenue_YoY'] = income_df['revenue'].pct_change() * 100
    income_df['Revenue_YoY'] = income_df['Revenue_YoY'].round(2)

    return income_df[['date', 'Revenue_YoY']]

# Step 3
def calc_ni_yoy(income_df):
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['Net_Income_YoY'] = income_df['netIncome'].pct_change() * 100
    income_df['Net_Income_YoY'] = income_df['Net_Income_YoY'].round(2)

    return income_df[['date', 'Net_Income_YoY']]

# Step 3
def calc_eps_yoy(income_df):
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['EPS_YoY'] = income_df['eps'].pct_change() * 100
    income_df['EPS_YoY'] = income_df['EPS_YoY'].round(2)

    return income_df[['date', 'EPS_YoY']]

# Step 3
def calc_eps_cagr(income_df, years=5):
    df = income_df.sort_values('date', ascending=True).copy()
    df['EPS_CAGR'] = np.nan

    n = len(df)
    if n >= 2:  # at least 2 years needed
        actual_years = min(years, n - 1)
        start = df.iloc[n - 1 - actual_years]['eps']
        end = df.iloc[n - 1]['eps']
        if pd.notna(start) and start > 0 and pd.notna(end):
            df.at[df.index[n - 1], 'EPS_CAGR'] = ((end / start) ** (1 / actual_years) - 1) * 100

    # Round
    df['EPS_CAGR'] = df['EPS_CAGR'].round(2)

    return df[['date', 'EPS_CAGR']]



# Efficiency
# Step 4
def calc_tat(income_df, balance_df):
    # Total asset turnover = 銷貨額(Net Sales (Revenue))／平均總資產(Average Total Assets = (本期總資產 + 上期總資產) / 2)
    balance_df = balance_df.sort_values("date", ascending=True).copy()
    balance_df['avg_total_assets'] = (balance_df['totalAssets'] + balance_df['totalAssets'].shift(1)) / 2

    merged = pd.merge(income_df[['date', 'revenue']], balance_df[['date', 'avg_total_assets']], on='date')
    merged['TAT'] = merged['revenue'] / merged['avg_total_assets']
    merged['TAT'] = merged['TAT'].round(2)

    return merged[['date', 'TAT']]



# Leverage
# Step 4
def calc_em(balance_df):
    # EM = 總資產 ÷ SE * 100
    balance_df = balance_df.sort_values("date", ascending=True).copy()
    balance_df['Equity_Multiplier'] = balance_df['totalAssets'] / balance_df['totalStockholdersEquity']
    balance_df['Equity_Multiplier'] = balance_df['Equity_Multiplier'].round(2)
    return balance_df[['date', 'Equity_Multiplier']]

# Step 4
def calc_dbr(balance_df):
    # DBR = 總負債 ÷ 總資產
    balance_df = balance_df.sort_values("date", ascending=True).copy()
    balance_df['Debt_Burden_Ratio'] = balance_df['totalLiabilities'] / balance_df['totalAssets']
    balance_df['Debt_Burden_Ratio'] = balance_df['Debt_Burden_Ratio'].round(2) * 100

    return balance_df[['date', 'Debt_Burden_Ratio']]



# Valuation
# Step 3
def calc_pe(profile, income_df):
    # PE = marketCap / netIncome
    latest_income = income_df.iloc[0]['netIncome']
    pe = profile['marketCap'] / latest_income
    pe = pe.round(2)

    return pe

# Step 4
def calc_pb(profile, balance_df):
    # PB = marketCap / totalStockholdersEquity
    latest_equity = balance_df.iloc[0]['totalStockholdersEquity']
    pb = profile['marketCap'] / latest_equity
    pb = pb.round(2)

    return pb

# Step 3
def calc_psr(profile, income_df):
    # PSR = marketCap / revenue
    latest_revenue = income_df.iloc[0]['revenue']
    psr = profile['marketCap'] / latest_revenue
    psr = psr.round(2)

    return psr

# Step 3
def calc_peg(pe, eps_cagr):
    # PEG = PE / EPS_CAGR
    if pd.notna(eps_cagr) and eps_cagr > 0:
        return round(pe / eps_cagr, 2)
    else:
        return np.nan



# ROE的解剖報告
# Step 4
def calc_dupont(income_df, balance_df):
    # ROE = NetMargin * AssetTurnover * EquityMultiplier
    merged = pd.merge(income_df, balance_df, on="date")
    merged['NetMargin'] = merged['netIncome'] / merged['revenue']
    merged['AssetTurnover'] = merged['revenue'] / merged['totalAssets']
    merged['EquityMultiplier'] = merged['totalAssets'] / merged['totalStockholdersEquity']
    merged['ROE_DuPont'] = merged['NetMargin'] * merged['AssetTurnover'] * merged['EquityMultiplier']
    merged['ROE_DuPont'] = merged['ROE_DuPont'].round(2)

    return merged[['date', 'ROE_DuPont']]