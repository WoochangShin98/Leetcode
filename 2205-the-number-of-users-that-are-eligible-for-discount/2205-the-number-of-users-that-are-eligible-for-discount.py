import pandas as pd
from datetime import datetime

def count_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    filtered = purchases[
        purchases['time_stamp'].between(start_date, end_date)
        & (purchases['amount'] >= min_amount)
    ]

    return pd.DataFrame({
        'user_cnt': [filtered['user_id'].nunique()]
    })
