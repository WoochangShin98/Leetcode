import pandas as pd

def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    eng = salaries[salaries['department'] == 'Engineering']
    mar = salaries[salaries['department'] == 'Marketing']

    eng = eng['salary'].max()
    mar = mar['salary'].max()
    result = abs(eng-mar)

    return pd.DataFrame({'salary_difference':[result]})
'''
    en_max = eng.groupby('department')['salary'].max().reset_index()
    ma_max = mar.groupby('department')['salary'].max().reset_index()
'''