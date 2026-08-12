import pandas as pd


def average_selling_price(prices: pd.DataFrame,units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on='product_id', how='left')

    valid = (
        (df['purchase_date'] >= df['start_date']) &
        (df['purchase_date'] <= df['end_date'])
    )

    df = df[valid]

    df['total_price'] = df['price'] * df['units']

    result = (
        df.groupby('product_id', as_index=False)
        .agg(
            total_price=('total_price', 'sum'),
            total_units=('units', 'sum')
        )
    )

    result['average_price'] = (
        result['total_price'] / result['total_units']
    ).round(2)

    # 판매가 전혀 없는 product도 포함
    products = prices[['product_id']].drop_duplicates()

    result = products.merge(
        result[['product_id', 'average_price']],
        on='product_id',
        how='left'
    )

    result['average_price'] = result['average_price'].fillna(0)

    return result