import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product,on='product_id',how='left')
    df['spending'] = df['quantity'] * df['price']
    df = (
        df.groupby(['user_id'],as_index = False)['spending']
        .sum()
    )

    return df.sort_values(['spending','user_id'],ascending=[False,True])