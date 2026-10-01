import pandas as pd

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    
    traffic = traffic[traffic['activity'] == 'login']
    
    traffic = (
        traffic.groupby('user_id',as_index=False)
                .agg(login_date=('activity_date','min'))
    )

    today = pd.to_datetime('2019-06-30')

    traffic = traffic[
        (traffic['login_date'] >= today - pd.Timedelta(days=90)) &
        (traffic['login_date'] <= today)
    ]

    traffic = (
        traffic.groupby('login_date',as_index=False)
        .agg(user_count=('user_id','count'))
        )

    return traffic[['login_date','user_count']]

    
