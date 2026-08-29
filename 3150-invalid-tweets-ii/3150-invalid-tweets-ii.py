import pandas as pd

def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    df = tweets[
        (tweets['content'].str.count('#') > 3) |
        (tweets['content'].str.count('@') > 3) |
        (tweets['content'].str.len() > 140)
    ]

    return df[['tweet_id']].sort_values('tweet_id')