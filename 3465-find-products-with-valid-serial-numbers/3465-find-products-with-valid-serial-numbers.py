import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    # SN , 4 digits, - 4 digits
    setting = r'\bSN\d{4}-\d{4}(?!\d)\b'
    df = products[products['description'].str.contains(setting,regex=True)]
    return df.sort_values('product_id')