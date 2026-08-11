import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders.groupby(by='customer_number').size()
    customer = counts.idxmax()
    return pd.DataFrame({'customer_number':[customer]})

    # idxmax()