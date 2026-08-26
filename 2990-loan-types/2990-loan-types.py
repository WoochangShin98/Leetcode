import pandas as pd

def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
    df = loans[loans['loan_type'].isin(['Mortgage','Refinance'])]
    df = df.groupby('user_id').nunique().reset_index()
    df = df[df['loan_type'] == 2]
    return df[['user_id']]
