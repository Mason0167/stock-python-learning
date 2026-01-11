from universe import *
from financials import *
from metrics import *
from export_excel import *

# Step 1
# 1/10 end_row: 1497
print("\nFetching the tickers......")
universe_df = build_universe_step1(start_row=1497, end_row=)

print("Fetching ticker profiles and cache json ......")
profiles = []
for symbol in universe_df["Symbol"]:
    
    p = fetch_profile(symbol)
    if p:
        profiles.append({
            "Symbol": symbol,
            "Sector": p["sector"],
            "MarketCap": p["marketCap"]
        })
    
    profile_df = pd.DataFrame(profiles)
print("\n", profile_df)  

profile_df["MarketCap"] = (profile_df["MarketCap"] / 1e9).round(2)

print("\nFiltering, Merging, Exporting......")
filtered = profile_df[
    (profile_df["Sector"] == "Technology") &
    (profile_df["MarketCap"] >= 3)
].copy()

universe_df = universe_df.merge(filtered, on="Symbol", how="inner")
export_universe_1(universe_df)
'''

# Step 2
print("\nFetching the tickers......")
universe_df = build_universe_step2(start_row=0, end_row=1)

results = []
for symbol in universe_df["Symbol"]:
    print("Processing: ", symbol)
    income_df, cashflow_df = fetch_income_cashflow_statement(symbol)

    # Calculate
    fcf_margin_df = calc_fcf_margin(cashflow_df, income_df)
    net_margin_df = calc_net_margin(income_df)

    # Join metrics by date
    metrics_df = fcf_margin_df.merge(net_margin_df, on="date", how="inner")

    # Filter
    FCF_bad_years = (metrics_df["FCF_Margin"] < 0).sum()
    if FCF_bad_years >= 3:
        print("Rejected (FCF Margin)", symbol)
        continue
        
    Net_bad_years = (metrics_df["Net_Margin"] < 0).sum()
    if Net_bad_years >= 3:
        print("Rejected (Net Margin)", symbol)
        continue
    
    # Add symbol column for later use
    metrics_df["Symbol"] = symbol
    results.append(metrics_df)
    
if not results:
    print("No stocks passed filter")
    exit()

final_df = pd.concat(results, ignore_index=True)

print("\nFiltering and formatting......")
export_universe_2(final_df)
'''

'''
# Step 3
print("\nFetching the tickers......")
balance_df = build_universe_step3()

print("\nFiltering and formatting......")
export_universe(income_df)
export_universe(cashflow_df)
'''


# # Step 1: 計算時間序列指標
# roe_df = calc_roe(income_df, balance_df)

# revenue_yoy_df = calc_revenue_yoy(income_df)
# ni_yoy_df = calc_ni_yoy(income_df)
# eps_yoy_df = calc_eps_yoy(income_df)
# eps_cagr_df = calc_eps_cagr(income_df)
# tat_df = calc_tat(income_df, balance_df)
# em_df = calc_em(balance_df)
# dbr_df = calc_dbr(balance_df)
# dupont_df = calc_dupont(income_df, balance_df)

# # Step 2: 合併成一個 DataFrame
# metrics_df = roe_df.merge(revenue_yoy_df, on="date", how="outer")\
#                    .merge(ni_yoy_df, on="date", how="outer")\
#                    .merge(eps_yoy_df, on="date", how="outer")\
#                    .merge(eps_cagr_df, on="date", how="outer")\
#                    .merge(tat_df, on="date", how="outer")\
#                    .merge(em_df, on="date", how="outer")\
#                    .merge(dbr_df, on="date", how="outer")\
#                    .merge(dupont_df, on="date", how="outer")

# # Step 3: 計算單值指標 (最新年份)
# pe = calc_pe(profile, income_df)
# pb = calc_pb(profile, balance_df)
# psr = calc_psr(profile, income_df)

# non_na_eps = eps_cagr_df['EPS_CAGR'].dropna()
# peg = calc_peg(pe, non_na_eps.iloc[-1]) if len(non_na_eps) > 0 else None

# # 只放在最後一行
# latest_idx = metrics_df.index[-1]
# metrics_df['PE'] = None
# metrics_df['PB'] = None
# metrics_df['PSR'] = None
# metrics_df['PEG'] = None
# metrics_df.at[latest_idx, 'PE'] = pe
# metrics_df.at[latest_idx, 'PB'] = pb
# metrics_df.at[latest_idx, 'PSR'] = psr
# metrics_df.at[latest_idx, 'PEG'] = peg

# # Step 4: 匯出 Excel（自動欄寬 + 百分比格式化）
# export_to_excel(metrics_df, ticker)
