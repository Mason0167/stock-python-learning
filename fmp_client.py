# communicate with FMP API
import os, json, requests

# mason74...
# API_KEY = "5eke07FPyWg4KUePACwvquplzFZvqBqM"

# cold...
# API_KEY = "JJs04hlrp3XP7zBpuGHsrdFA4Sn39bT3"

# mason...
API_KEY = "VGgfhNYcvVr6wfqSMEXe2r5vwwut6f86"

BASE_URL = "https://financialmodelingprep.com/stable"

# Step 1: Fetch profile data to filter by market cap and sector
def get_profile(symbol: str):
    url = f"{BASE_URL}/profile?symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    return data

# Step 2
def get_income_statement(symbol: str):
    path = f"data_raw/income-statement/{symbol}.json"

    # Return cached JSON if exists
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    url = f"{BASE_URL}/income-statement?symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    # Save JSON
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return data

def get_cashflow_statement(symbol: str):
    path = f"data_raw/cash-flow-statement/{symbol}.json"

    # Return cached JSON if exists
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    url = f"{BASE_URL}/cash-flow-statement?symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    # Save JSON
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return data
    

# Step 3
def get_balance_sheet(symbol: str):
    path = f"data_raw/income-statement/{symbol}.json"

    # Return cached JSON if exists
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    url = f"{BASE_URL}/balance-sheet-statement?symbol={symbol}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    # Save JSON
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return data



