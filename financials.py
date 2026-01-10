# Convert FMP JSON into clean tables
import pandas as pd
from fmp_client import *

# Step 1
def extract_profile(profile_json):
    if not profile_json:
        return None
    p = profile_json[0]

    return {
        "sector": p["sector"],
        "marketCap": p["marketCap"]
    }

def fetch_profile(symbol):
    raw = get_profile(symbol)
    return extract_profile(raw)

'''
# Step 2
def fetch_financials(ticker):

    income_df = pd.DataFrame(get_income_statement(ticker))
    cashflow_df = pd.DataFrame(get_cash_flow(ticker))
    
    # 選你要的欄位
    # income: 營收、NI、每股營收
    income_df = income_df[['date', 'revenue', 'netIncome', 'eps']]
    # cashflow: 營業現金流、資本支出
    cashflow_df = cashflow_df[['date', 'operatingCashFlow', 'capitalExpenditure']]
    
    return income_df, cashflow_df
'''
# Step 3
# def fetch_financials(ticker):
#     balance_df = pd.DataFrame(get_balance_sheet(ticker))
    
#     # 選你要的欄位
#     # balance: 總資產、總負債(欠所有對象)、SE、總債務(欠銀行或債主)
#     balance_df = balance_df[['date', 'totalAssets', 'totalLiabilities', 'totalStockholdersEquity']]

#     return balance_df
