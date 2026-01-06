import pandas as pd
import os

def export_metrics_to_excel(ticker, roe_df, dupont_df, fcf_df, eps_cagr_df, pe, pb, psr, peg, folder="data_metrics"):
    # 確保資料夾存在
    os.makedirs(folder, exist_ok=True)
    
    # 合併 DataFrame
    metrics_df = pd.merge(roe_df, dupont_df, on="date", how="outer")
    metrics_df = pd.merge(metrics_df, fcf_df, on="date", how="outer")
    metrics_df = pd.merge(metrics_df, eps_cagr_df, on="date", how="outer")
    
    # 將單值指標加到 DataFrame
    metrics_df['PE'] = pe
    metrics_df['PB'] = pb
    metrics_df['PSR'] = psr
    metrics_df['PEG'] = peg
    
    # 輸出 Excel
    file_path = os.path.join(folder, f"{ticker}_metrics.xlsx")
    metrics_df.to_excel(file_path, index=False)
    print(f"Metrics exported to {file_path}")
