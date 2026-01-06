# Connect all py file
from financials import fetch_financials
from metrics import calc_roe, calc_dupont, calc_fcf_margin, calc_eps_cagr, calc_pe, calc_pb, calc_psr, calc_peg
from export_excel import export_metrics_to_excel

ticker = "AAPL"
income_df, balance_df, cashflow_df, profile = fetch_financials(ticker)

roe_df = calc_roe(income_df, balance_df)
dupont_df = calc_dupont(income_df, balance_df)
fcf_df = calc_fcf_margin(cashflow_df, income_df)
eps_cagr_df = calc_eps_cagr(income_df)

pe = calc_pe(profile, income_df)
pb = calc_pb(profile, balance_df)
psr = calc_psr(profile, income_df)
peg = calc_peg(pe, eps_cagr_df.iloc[0]['EPS_CAGR'])

# 輸出到 Excel
export_metrics_to_excel(ticker, roe_df, dupont_df, fcf_df, eps_cagr_df, pe, pb, psr, peg)