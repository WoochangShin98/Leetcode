import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_date = (
        activity.groupby('player_id')['event_date']
        .min()
        .rename('first_date')
    )

    activity = activity.merge(
        first_date,
        on='player_id'
    )

    returned = activity[
        activity['event_date'] == activity['first_date'] + pd.Timedelta(days=1)
    ]['player_id'].nunique()

    total = activity['player_id'].nunique()

    return pd.DataFrame({
        'fraction': [round(returned / total, 2)]
    })

    total = activity['player_id'].nunique()

    return pd.DataFrame({
        'fraction': [round(returned / total, 2)]
    })