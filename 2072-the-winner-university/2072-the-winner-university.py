import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    ncount= (new_york['score'] >= 90).sum()
    ccount = (california['score'] >= 90).sum()

    if ncount > ccount:
        return pd.DataFrame({'winner':['New York University']})
    elif ccount > ncount:
        return pd.DataFrame({'winner':['California University']})
    else:
        return pd.DataFrame({'winner':['No Winner']})