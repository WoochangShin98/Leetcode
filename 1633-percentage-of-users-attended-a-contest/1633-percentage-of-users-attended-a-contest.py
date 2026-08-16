import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    count = users['user_id'].nunique()

    df = register.merge(users,on='user_id',how='left')
    df = (
        df.groupby('contest_id')['user_id']
          .nunique()
          .reset_index()
    )

    df['percentage'] = ((df['user_id'] / count) * 100).round(2)

    df = df.sort_values(
        ['percentage','contest_id'],
        ascending=[False,True]
        )

    return df[['contest_id', 'percentage']]