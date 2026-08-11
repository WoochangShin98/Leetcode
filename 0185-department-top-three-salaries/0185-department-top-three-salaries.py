import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merge_table = employee.merge(department,left_on='departmentId',right_on='id',how='left')
    merge_table['rank'] = merge_table.groupby('departmentId')['salary'].rank(method='dense',ascending=False)
    result = merge_table[merge_table['rank']<= 3]
    result = result.rename(columns={
        'name_x': 'Employee',
        'name_y': 'Department',
        'salary': 'Salary'
    })

    return result[['Department','Employee','Salary']]

# 새롭게 배운 rank를 잊지말자