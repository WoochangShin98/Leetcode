import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    join_employee = employee.merge(department, left_on='departmentId', right_on = 'id', how='left')
    max_salary = join_employee.groupby(by='departmentId')['salary'].transform('max')

    join_employee = join_employee[join_employee['salary'] == max_salary]    
    join_employee = join_employee.rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})

    return join_employee[['Department','Employee','Salary']]

    # join 하러면 pandas 에서는 merge를 사용함
    # 사용법은 merge(df,left_on,right_on,how)