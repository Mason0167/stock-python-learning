from financials import fetch_financials
from metrics import *
from export_excel import *

ticker = "AAPL"

# Step 0: 取財報
income_df, balance_df, cashflow_df, profile = fetch_financials(ticker)

# Step 1: 計算時間序列指標
roe_df = calc_roe(income_df, balance_df)
fcf_margin_df = calc_fcf_margin(cashflow_df, income_df)
net_margin_df = calc_net_margin(income_df)
revenue_yoy_df = calc_revenue_yoy(income_df)
ni_yoy_df = calc_ni_yoy(income_df)
eps_yoy_df = calc_eps_yoy(income_df)
eps_cagr_df = calc_eps_cagr(income_df)
tat_df = calc_tat(income_df, balance_df)
em_df = calc_em(balance_df)
dbr_df = calc_dbr(balance_df)
dupont_df = calc_dupont(income_df, balance_df)

# Step 2: 合併成一個 DataFrame
metrics_df = roe_df.merge(fcf_margin_df, on="date", how="outer")\
                   .merge(net_margin_df, on="date", how="outer")\
                   .merge(revenue_yoy_df, on="date", how="outer")\
                   .merge(ni_yoy_df, on="date", how="outer")\
                   .merge(eps_yoy_df, on="date", how="outer")\
                   .merge(eps_cagr_df, on="date", how="outer")\
                   .merge(tat_df, on="date", how="outer")\
                   .merge(em_df, on="date", how="outer")\
                   .merge(dbr_df, on="date", how="outer")\
                   .merge(dupont_df, on="date", how="outer")

# Step 3: 計算單值指標 (最新年份)
pe = calc_pe(profile, income_df)
pb = calc_pb(profile, balance_df)
psr = calc_psr(profile, income_df)

non_na_eps = eps_cagr_df['EPS_CAGR'].dropna()
peg = calc_peg(pe, non_na_eps.iloc[-1]) if len(non_na_eps) > 0 else None

# 只放在最後一行
latest_idx = metrics_df.index[-1]
metrics_df['PE'] = None
metrics_df['PB'] = None
metrics_df['PSR'] = None
metrics_df['PEG'] = None
metrics_df.at[latest_idx, 'PE'] = pe
metrics_df.at[latest_idx, 'PB'] = pb
metrics_df.at[latest_idx, 'PSR'] = psr
metrics_df.at[latest_idx, 'PEG'] = peg

# Step 4: 匯出 Excel（自動欄寬 + 百分比格式化）
export_to_excel(metrics_df, ticker)
