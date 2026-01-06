import pandas as pd
import os

from openpyxl import load_workbook
from openpyxl.styles import numbers
from openpyxl.utils import get_column_letter
from typing import Optional

def export_to_excel(metrics_df: pd.DataFrame, ticker: str, file_path: Optional[str] = None):
    file_path = os.path.abspath(f"data_metrics/{ticker}_metrics.xlsx")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 匯出初步 Excel
    metrics_df.to_excel(file_path, index=False)

    # 載入 Excel
    wb = load_workbook(file_path)
    ws = wb.active
    if ws is None:
        raise ValueError("No active worksheet found in workbook")

    # 自動調整欄寬
    def get_display_width(text):
        width = 0
        for ch in str(text):
            if ord(ch) > 255:  # 中文或全形
                width += 4
            else:
                width += 2
        return width

    for col_cells in ws.iter_cols(min_row=1, max_row=ws.max_row):
        col_letter = get_column_letter(col_cells[0].column or 1)
        max_length = 0

        for cell in col_cells:
            if cell.value is not None:
                max_length = max(max_length, get_display_width(cell.value))

        ws.column_dimensions[col_letter].width = max_length + 2

    # 儲存並開啟 Excel
    wb.save(file_path)
    os.startfile(file_path)
    print(f"Excel exported and formatted: {file_path}")
