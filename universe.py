import pandas as pd

def build_universe(input_file="data_raw/nasdaqlisted_filtered.xlsx",
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
