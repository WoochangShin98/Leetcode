import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:

    df = ads.merge(playback, on='customer_id')

    df = df[
        (df['start_time'] <= df['timestamp']) &
        (df['timestamp'] <= df['end_time'])
    ]

    ad_sessions = df['session_id'].unique()

    result = playback[~playback['session_id'].isin(ad_sessions)]

    return result[['session_id']]