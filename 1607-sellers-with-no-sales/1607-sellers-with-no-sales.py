import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    # 2020 x , orderby asc 'seller_name'
    
    sold_2020 = orders[
        (orders['sale_date'] >= '2020-01-01') &
        (orders['sale_date'] < '2021-01-01')
    ]['seller_id']

    df = seller[
        ~seller['seller_id'].isin(sold_2020)
    ]

    return df[['seller_name']].sort_values('seller_name')