import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df1 = employees[~employees['employee_id'].isin(salaries['employee_id'])]
    df2 = salaries[~salaries['employee_id'].isin(employees['employee_id'])]

    result = pd.concat([df1[['employee_id']], df2[['employee_id']]])

    return result.sort_values('employee_id')

    '''df1 = employees.merge(salaries, on='employee_id', how='left')
    df1 = df1[df1['salary'].isna()][['employee_id']]

    df2 = salaries.merge(employees, on='employee_id', how='left')
    df2 = df2[df2['name'].isna()][['employee_id']]

    result = pd.concat([df1, df2])

    return result.sort_values('employee_id')'''