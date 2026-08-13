import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    
    df = users.merge(
        rides,
        left_on='id',
        right_on='user_id',
        how='left'
    )

    df = (
        df.groupby(['id_x', 'name'], as_index=False)
        .agg(travelled_distance=('distance', 'sum'))
    )

    df['travelled_distance'] = df['travelled_distance'].fillna(0)

    df = df.sort_values(
        by=['travelled_distance', 'name'],
        ascending=[False, True]
    )

    return df[['name', 'travelled_distance']]