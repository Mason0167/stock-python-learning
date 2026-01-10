import pandas as pd
import os

from financials import fetch_profile


# Step 1: Filtering by Sector and Market Cap
def build_universe_step1(input_file="data_raw/nasdaqlisted_filtered.xlsx",
                    start_row=None, end_row=None):
    
    origin_file = pd.read_excel(input_file).copy()

    # Select subset if needed
    if start_row is not None and end_row is not None:
        subset = origin_file.iloc[start_row:end_row]
    else:
        subset = origin_file

    # Keep only the basic columns
    universe_df = subset[['Symbol', 'Name']].copy()

    return universe_df

'''
# Step 2: Net Margin < 0 & FCF_Margin < 0。
# Remember to store the JSON
def build_universe_step2():

    input_file = "data_clean/universe_step1.xlsx"
    start_row=0
    end_row=1

    origin_file = pd.read_excel(input_file).copy()

    # Select subset if needed
    if start_row is not None and end_row is not None:
        subset = origin_file.iloc[start_row:end_row]

    



    output_file = f"data_metrics/{symbol}"
'''
