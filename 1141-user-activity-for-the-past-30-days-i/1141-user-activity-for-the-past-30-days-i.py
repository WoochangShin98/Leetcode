import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    condition = activity['activity_date'].between('2019-06-28','2019-07-27') # boolean
    activity = activity[condition]

    result = (
        activity.groupby('activity_date')['user_id']
        .nunique()
        .reset_index(name='active_users')
        .rename(columns={'activity_date':'day'})
    )

    return result