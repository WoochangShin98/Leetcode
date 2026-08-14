import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products['total'] = products['Width'] * products['Length'] * products['Height']

    df = warehouse.merge(products,on='product_id',how='left')
    df['volume'] = df['total'] * df['units']
    df = (
        df.groupby('name')['volume']
        .sum()
        .reset_index()
    )

    df = df.rename(columns={'name': 'warehouse_name'})

    return df