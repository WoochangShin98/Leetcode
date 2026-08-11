import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    name = 'SecondHighestSalary'
    salary = employee['salary'].sort_values(ascending=False).drop_duplicates() 

    if len(salary) < 2:
        return pd.DataFrame({
            name : [None]
        })
    else:
         return pd.DataFrame({
            name : [salary.iloc[1]]
        })