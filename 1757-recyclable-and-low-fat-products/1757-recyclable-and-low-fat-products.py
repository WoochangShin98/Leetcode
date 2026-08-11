import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
   option = (products['low_fats'] == "Y") & (products['recyclable'] == "Y")
   result = products[option]
   return result[['product_id']]