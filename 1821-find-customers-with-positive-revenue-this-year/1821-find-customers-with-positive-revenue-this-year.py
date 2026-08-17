import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers[(customers['year'] == 2021) & (customers['revenue'] > 0)]
    
    return customers[['customer_id']]