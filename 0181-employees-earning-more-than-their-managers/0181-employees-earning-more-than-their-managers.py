import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(employee,left_on='managerId',right_on='id')
    result = result[result['salary_x'] > result['salary_y']]
    result = result.rename(columns={'name_x':'Employee'})
    return result[['Employee']]
# if는 안되고 이렇게 필터링 