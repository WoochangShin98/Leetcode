import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    df = queries.merge(npv, on=['id', 'year'], how='left')
    df['npv'] = df['npv'].fillna(0)
    return df