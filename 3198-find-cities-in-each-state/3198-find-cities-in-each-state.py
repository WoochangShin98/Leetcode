import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    df = (
        cities
                .sort_values(['state','city'])
                .groupby('state')
                .agg(cities=('city',', '.join))
                .reset_index()
                .sort_values('state')
    )

    return df