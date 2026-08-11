import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull = files['content'].str.contains(' bull ').sum()
    bear = files['content'].str.contains(' bear ').sum()

    return pd.DataFrame({
        'word':['bull','bear'],
        'count':[bull,bear]
        })