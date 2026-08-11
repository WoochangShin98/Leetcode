import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    total_price = (
    sales.groupby('seller_id')['price']
    .sum()
    .reset_index(name='total_price')
)

    max_price = total_price['total_price'].max()
    result = total_price[total_price['total_price'] == max_price]
    return result[['seller_id' ]]