import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    second_degree = follow[
        follow['followee'].isin(follow['follower'])
    ]

    df = (
        second_degree
        .groupby('followee')
        .size()
        .reset_index(name='num')
        .rename(columns={'followee':'follower'})
        .sort_values('follower')
    )

    return df 