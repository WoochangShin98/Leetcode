import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    result = sales.merge(product,on='product_id')
    s8_buyer = result.loc[result['product_name'] == 'S8']
    ip_buyer = result.loc[result['product_name'] == 'iPhone']

    result = s8_buyer[
        ~s8_buyer['buyer_id'].isin(ip_buyer['buyer_id'])
    ]

    return result[['buyer_id']].drop_duplicates()