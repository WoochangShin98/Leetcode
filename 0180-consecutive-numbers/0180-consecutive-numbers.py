import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
 result = (
    logs['num'].eq(logs['num'].shift(1)) & logs['num'].eq(logs['num'].shift(2))
    )

 result = logs.loc[result,['num']].drop_duplicates().rename(columns={'num':'ConsecutiveNums'})
 return result

 #.eq 랑 .shift(숫자)