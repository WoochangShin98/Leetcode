import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    condition = r'(?<!\d)\d{3}(?!\d)'
    df = products[products['name'].str.contains(condition,regex=True)]
    return df.sort_values('product_id')