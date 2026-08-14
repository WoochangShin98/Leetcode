import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    #unique orders, customer / >20, each dif mon
    
    orders = orders[orders['invoice']>20]
    orders['month'] = orders['order_date'].dt.strftime('%Y-%m')
    
    df = (
        orders.groupby(['month'])
        .agg(
            order_count=('order_id','nunique'),
            customer_count=('customer_id', 'nunique')
        )
        .reset_index()
    )
    return df