import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.merge(countries,on='country_id',how='left')

    df = df[(df['day'] >= '2019-11-01') & (df['day'] <= '2019-11-30')]

    df = (
        df.groupby(['country_name','country_id'])
        .agg(weather=('weather_state','mean'))
        .reset_index()
        )
    
    df['weather_type'] = df['weather'].apply(
        lambda x: 'Cold' if x <= 15 else 'Hot' if x >= 25 else 'Warm'
    )

    return df[['country_name','weather_type']]


'''def classify_weather(x):
    if x <= 15:
        return 'Cold'
    elif x >= 25:
        return 'Hot'
    else:
        return 'Warm'
df['weather_type'] = df['weather'].apply(classify_weather)'''