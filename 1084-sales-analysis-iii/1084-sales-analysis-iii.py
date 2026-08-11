import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    result = (sales.groupby('product_id')['sale_date']
    .agg(first_date='min',last_date='max')
    .reset_index())

    condition = ((result['first_date'] >= '2019-01-01') & (result['last_date'] <= '2019-03-31'))
    result = result.loc[condition]
    result = result.merge(product,on='product_id')
    return result[['product_id','product_name']]