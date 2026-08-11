import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
   result = customer['referee_id'].isna() | ~(customer['referee_id'] == 2)
   customer = customer[result]
   return customer[['name']]