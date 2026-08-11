import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
   condition = ~(customers['id'].isin(orders['customerId']))
   result = customers[condition]
   result = result.rename(columns = {'name':'Customers'})
   return result[['Customers']]