import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    condition = activity['activity_date'].between('2019-06-28','2019-07-27')
    activity = activity[condition]
    result = (
        activity
        .groupby('user_id')['session_id']
        .nunique()
        .reset_index(name='count')
    )

    avg = round(result['count'].mean() if not result.empty else 0, 2)

    return pd.DataFrame({
        'average_sessions_per_user': [avg]
    })