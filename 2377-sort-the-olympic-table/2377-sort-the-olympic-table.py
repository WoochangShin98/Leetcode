import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    df = olympic.sort_values(['gold_medals','silver_medals','bronze_medals','country'],
    ascending=[False,False,False,True])
    return df