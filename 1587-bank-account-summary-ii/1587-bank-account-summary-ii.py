import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # name, user w/ balance, > 10000
    
    df = transactions.merge(users,on='account',how='left')
    df = (
        df.groupby(['account','name'])['amount']
        .sum()
        .reset_index(name='balance')
    )
    df = df[df['balance']>10000]
    return df[['name','balance']]