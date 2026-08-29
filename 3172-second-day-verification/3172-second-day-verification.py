import pandas as pd

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    df = emails.merge(texts,on='email_id',how='left')
    df = df[
        (df['signup_action'] == 'Verified') &
        (df['action_date'].dt.date == 
        (df['signup_date'] + pd.Timedelta(days=1)).dt.date)
        ]

    return df[['user_id']].sort_values('user_id',ascending=True)