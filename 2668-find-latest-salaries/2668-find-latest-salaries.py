import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    df = (salary.groupby(['firstname','lastname'])[['emp_id','firstname','lastname','salary','department_id']]
          .max())

    return df.sort_values('emp_id',ascending=True)