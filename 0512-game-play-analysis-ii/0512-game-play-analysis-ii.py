import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = (
        activity
        .sort_values('event_date')
        .groupby('player_id', as_index=False)
        .first()
    )

    return result[['player_id', 'device_id']]