import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    df = (sales.groupby('product_id')['year']
                .min()
                .reset_index()
                .rename(columns={'year':'first_year'})
    )

    result = sales.merge(
        df,
        left_on=['product_id', 'year'],
        right_on=['product_id', 'first_year']
    )

    return result[['product_id', 'first_year', 'quantity', 'price']]
