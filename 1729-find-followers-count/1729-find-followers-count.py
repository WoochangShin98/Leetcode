import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    followers = (
        followers.groupby('user_id')
        .size()
        .reset_index(name='followers_count')
    )

    return followers