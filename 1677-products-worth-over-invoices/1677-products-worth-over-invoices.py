import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    # If Join with Invoice table, the remain attribute who has 0 valuse will delete
    df = product.merge(invoice,on='product_id',how='left')
    cols = ['rest','paid','canceled','refunded']
    df[cols] = df[cols].fillna(0)
    df = (
        df.groupby(['name'])[['rest','paid','canceled','refunded']]
        .sum()
        .reset_index()
        .sort_values('name')
    )
    return df