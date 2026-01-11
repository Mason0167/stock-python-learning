# Convert FMP JSON into clean tables
import pandas as pd
from fmp_client import *

# Step 1
def fetch_profile(symbol):
    raw = get_profile(symbol)
    return extract_profile(raw)
    

def extract_profile(profile_json):
    if not profile_json:
        return None
    p = profile_json[0]

    return {
        "sector": p["sector"],
        "marketCap": p["marketCap"]
    }


# Step 2
def fetch_income_cashflow_statement(symbol):
    raw_income = get_income_statement(symbol)
    raw_cashflow = get_cashflow_statement(symbol)

    income_df = extract_income_statement(raw_income)
    cashflow_df = extract_cashflow_statement(raw_cashflow)

    return income_df, cashflow_df

def extract_income_statement(income_json):
    if not income_json:
        return None
    income_df = pd.DataFrame(income_json)

    # income: 營收、NI、每股營收
    income_df = income_df[['date', 'revenue', 'netIncome', 'eps']]
    
    return income_df

def extract_cashflow_statement(cashflow_json):
    if not cashflow_json:
        return None
    cashflow_df = pd.DataFrame(cashflow_json)

    # cashflow: 營業現金流、資本支出
    cashflow_df = cashflow_df[['date', 'operatingCashFlow', 'capitalExpenditure']]
    
    return cashflow_df


# Step 3
def fetch_balance_statement(symbol):
    raw_balance = get_balance_sheet(symbol)
    balance_df = extract_balance_statement(raw_balance)
    
    return balance_df

def extract_balance_statement(balance_json):
    if not balance_json:
        return None
    balance_df = pd.DataFrame(balance_json)

    # balance: 總資產、總負債(欠所有對象)、SE、總債務(欠銀行或債主)
    balance_df = balance_df[['date', 'totalAssets', 'totalLiabilities', 'totalStockholdersEquity']]
    
    return balance_df