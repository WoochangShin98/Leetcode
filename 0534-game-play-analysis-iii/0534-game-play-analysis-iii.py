import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # cumsum -> 누적합 
    activity = activity.sort_values(['player_id','event_date'])
    activity['games_played_so_far'] = (
        activity.groupby('player_id')['games_played'].cumsum()
    )

    return activity[['player_id', 'event_date', 'games_played_so_far']]