import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    condition = (delivery['order_date'] == delivery['customer_pref_delivery_date']).sum()
    
    percentage = (condition / delivery['delivery_id'].count()) * 100
    percentage = percentage.round(2)
    
    return pd.DataFrame({'immediate_percentage':[percentage]})