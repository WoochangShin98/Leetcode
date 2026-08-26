import pandas as pd

def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    # number & occurrence count , desc , if = artist asc

    df = spotify.groupby('artist').size().reset_index()
    df = df.rename(columns={0:'occurrences'})
    return df.sort_values(['occurrences','artist'],ascending=[False,True])