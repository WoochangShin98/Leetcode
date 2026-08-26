import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    # distance / user , x -> 0 , user_Id asc
    df = users.merge(rides,on='user_id',how='left')
    df = (df.groupby(['user_id','name'])['distance']
            .sum()
            .reset_index(name='traveled distance')
    )
    df = df.sort_values('user_id',ascending=True)
    return df