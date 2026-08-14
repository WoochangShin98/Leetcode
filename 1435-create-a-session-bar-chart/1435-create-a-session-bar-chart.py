import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    sessions['bin'] = sessions['duration'] / 60
    a = (sessions['bin'] < 5).sum()
    b = ((sessions['bin'] >= 5) & (sessions['bin'] < 10)).sum()
    c = ((sessions['bin'] >= 10) & (sessions['bin'] < 15)).sum()
    d = (sessions['bin'] >= 15).sum()

    return pd.DataFrame({
        'bin': ['[0-5>', '[5-10>', '[10-15>', '15 or more'],
        'total': [a, b, c, d]
    })