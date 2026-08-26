import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    # find the 'last time' each bike , most recently
    df = (bikes.groupby('bike_number')['end_time']
                .max()
                .reset_index()
    )

    return df.sort_values('end_time', ascending=False)