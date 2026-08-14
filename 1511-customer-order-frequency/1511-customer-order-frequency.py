import pandas as pd

def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df = orders.merge(customers, on='customer_id', how='left')
    df = df.merge(product, on='product_id', how='left')

    df = df[
        (df['order_date'] >= '2020-06-01') &
        (df['order_date'] < '2020-08-01')
    ]

    df['total'] = df['price'] * df['quantity']

    df['month'] = df['order_date'].dt.month

    df = (
        df.groupby(['customer_id', 'name', 'month'])['total']
          .sum()
          .reset_index()
    )

    df = df[df['total'] >= 100]

    df = (
        df.groupby(['customer_id', 'name'])
          .filter(lambda x: len(x) == 2)
    )

    return df[['customer_id', 'name']].drop_duplicates()