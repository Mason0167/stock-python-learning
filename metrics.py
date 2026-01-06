# Convert financial statements to metrics
import pandas as pd
import numpy as np

# Profitability
def calc_roe(income_df, balance_df):
    # ROE = netIncome / totalStockholdersEquity
    merged = pd.merge(income_df, balance_df, on="date")
    merged['ROE'] = merged['netIncome'] / merged['totalStockholdersEquity']
    return merged[['date', 'ROE']]

def calc_fcf_margin(cashflow_df, income_df):
    # FCF = OCF - CapEx; FCF Margin = FCF / revenue
    merged = pd.merge(cashflow_df, income_df[['date', 'revenue']], on='date')
    merged['FCF'] = merged['operatingCashFlow'] + merged['capitalExpenditure']  # CapEx 是負的，所以加
    merged['FCF_Margin'] = merged['FCF'] / merged['revenue']
    return merged[['date', 'FCF', 'FCF_Margin']]

def calc_net_margin(income_df):
    # FCF = OCF - CapEx; FCF Margin = FCF / revenue
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['net_margin'] = income_df['netIncome'] / income_df['revenue']
    return income_df[['date', 'net_margin']]



# Growth
def calc_revenue_yoy(income_df):
    # Revenue YoY % = (本期revenue − 上期revenue) ÷ 上期revenue × 100
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['revenue_YoY'] = income_df['revenue'].pct_change() * 100
    return income_df[['date', 'revenue_YoY']]

def calc_ni_yoy(income_df):
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['netIncome_YoY'] = income_df['netIncome'].pct_change() * 100
    return income_df[['date', 'netIncome_YoY']]

def calc_eps_yoy(income_df):
    income_df = income_df.sort_values("date", ascending=True).copy()
    income_df['eps_YoY'] = income_df['eps'].pct_change() * 100
    return income_df[['date', 'eps_YoY']]

def calc_eps_cagr(income_df):
    # EPS 5Y CAGR
    income_df = income_df.sort_values('date', ascending=True).copy()
    income_df['EPS_CAGR'] = np.nan
    for i in range(5, len(income_df)):
        start = income_df.iloc[i-5]['eps']
        end = income_df.iloc[i]['eps']
        if pd.notna(start) and start > 0 and pd.notna(end):
            income_df.at[income_df.index[i], 'EPS_CAGR'] = ((end / start) ** (1/5) - 1) * 100
    return income_df[['date', 'EPS_CAGR']]



# Efficiency
def calc_tat(income_df, balance_df):
    # Total asset turnover = 銷貨額(Net Sales (Revenue))／平均總資產(Average Total Assets = (本期總資產 + 上期總資產) / 2)
    balance_df = balance_df.sort_values("date", ascending=True).copy()
    balance_df['avg_total_assets'] = (balance_df['totalAssets'] + balance_df['totalAssets'].shift(1)) / 2

    merged = pd.merge(income_df[['date', 'revenue']], balance_df[['date', 'avg_total_assets']], on='date')
    merged['TAT'] = merged['revenue'] / merged['avg_total_assets']
    return merged[['date', 'TAT']]



# Leverage
def calc_em(balance_df):
    # EM = 總資產 ÷ SE * 100
    balance_df = balance_df.sort_values("date", ascending=True).copy()
    balance_df['EquityMultiplier'] = balance_df['totalAssets'] / balance_df['totalStockholdersEquity']
    return balance_df[['date', 'EquityMultiplier']]



# Valuation
def calc_pe(profile, income_df):
    # PE = marketCap / netIncome
    latest_income = income_df.iloc[0]['netIncome']
    pe = profile['marketCap'] / latest_income
    return pe

def calc_pb(profile, balance_df):
    # PB = marketCap / totalStockholdersEquity
    latest_equity = balance_df.iloc[0]['totalStockholdersEquity']
    pb = profile['marketCap'] / latest_equity
    return pb

def calc_psr(profile, income_df):
    # PSR = marketCap / revenue
    latest_revenue = income_df.iloc[0]['revenue']
    psr = profile['marketCap'] / latest_revenue
    return psr

def calc_peg(pe, eps_cagr):
    # PEG = PE / EPS_CAGR
    if eps_cagr > 0:
        return pe / (eps_cagr * 100)  # 把百分比轉回比例
    else:
        return np.nan



# ROE的解剖報告
def calc_dupont(income_df, balance_df):
    # ROE = NetMargin * AssetTurnover * EquityMultiplier
    merged = pd.merge(income_df, balance_df, on="date")
    merged['NetMargin'] = merged['netIncome'] / merged['revenue']
    merged['AssetTurnover'] = merged['revenue'] / merged['totalAssets']
    merged['EquityMultiplier'] = merged['totalAssets'] / merged['totalStockholdersEquity']
    merged['ROE_DuPont'] = merged['NetMargin'] * merged['AssetTurnover'] * merged['EquityMultiplier']
    return merged[['date', 'ROE_DuPont']]





