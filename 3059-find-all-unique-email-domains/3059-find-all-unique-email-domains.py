import pandas as pd

def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    df = emails.copy()

    df['email_domain'] = df['email'].str.split('@').str[1]
    df = df[df['email_domain'].str.endswith('.com')]
    df = (
        df.groupby('email_domain')
        .size()
        .reset_index(name='count')
        .sort_values('email_domain')
    )
    return df