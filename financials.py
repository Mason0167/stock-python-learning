# Convert FMP JSON into clean tables
import pandas as pd
from fmp_client import get_income_statement, get_balance_sheet, get_cash_flow, get_profile

def fetch_financials(ticker):
    income_df = pd.DataFrame(get_income_statement(ticker))
    balance_df = pd.DataFrame(get_balance_sheet(ticker))
    cashflow_df = pd.DataFrame(get_cash_flow(ticker))
    profile = get_profile(ticker)
    
    # 選你要的欄位
    # income: 營收、NI、每股營收
    income_df = income_df[['date', 'revenue', 'netIncome', 'eps']]
    # balance: 總資產、SE、總負債
    balance_df = balance_df[['date', 'totalAssets', 'totalStockholdersEquity', 'totalDebt']]
    # cashflow: 營業現金流、資本支出
    cashflow_df = cashflow_df[['date', 'operatingCashFlow', 'capitalExpenditure']]
    
    return income_df, balance_df, cashflow_df, profile


