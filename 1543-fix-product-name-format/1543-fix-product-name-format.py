import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    #.str.lower() 
    #.dt.strftime('%Y-%m')
    sales['product_name'] = sales['product_name'].str.strip().str.lower()

    sales['sale_date']=sales['sale_date'].dt.strftime('%Y-%m')
    
    df = (sales.groupby(['product_name','sale_date'])
    .size()
    .reset_index(name='total'))
    df = df.sort_values(['product_name','sale_date'])
    return df[['product_name','sale_date','total']]