# communicate with FMP API
import requests

API_KEY = "VGgfhNYcvVr6wfqSMEXe2r5vwwut6f86"
BASE_URL = "https://financialmodelingprep.com/stable"


def get_income_statement(ticker):
    url = f"{BASE_URL}/income-statement?symbol={ticker}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def get_balance_sheet(ticker):
    url = f"{BASE_URL}/balance-sheet-statement?symbol={ticker}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def get_cash_flow(ticker):
    url = f"{BASE_URL}/cash-flow-statement?symbol={ticker}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def get_profile(ticker):
    url = f"{BASE_URL}/profile?symbol={ticker}&apikey={API_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()[0]
