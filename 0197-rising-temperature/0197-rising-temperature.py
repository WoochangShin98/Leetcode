import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather = weather.sort_values('recordDate')

    previous_temp = weather['temperature'].shift(1)
    previous_day = weather['recordDate'].shift(1)

    result = (
        (weather['temperature'] > previous_temp) &
        ((weather['recordDate'] - previous_day).dt.days == 1)
    )

    return weather.loc[result, ['id']]