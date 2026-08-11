import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    condition1 = cinema['id'] % 2 == 1
    condition2 = cinema['description'] != 'boring'
    result = cinema[condition1 & condition2]
    result = result.sort_values('rating',ascending=False)
    return result