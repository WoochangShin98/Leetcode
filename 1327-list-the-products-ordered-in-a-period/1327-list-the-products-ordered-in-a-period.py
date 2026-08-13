import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #2월안에 ,최소 100개인것만
    df = orders.merge(products,on='product_id',how='left')
    df = df[df['order_date'].between('2020-02-01', '2020-02-29')]
    df = (
        df.groupby(['product_id','product_name'])['unit']
        .sum()
        .reset_index()
        )
    df = df[df['unit'] >= 100]
    
    return df[['product_name','unit']]