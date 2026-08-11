import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    single = counts[counts == 1]

    if single.empty:
        return pd.DataFrame({'num':[None]})

    return pd.DataFrame({'num':[single.index.max()]})