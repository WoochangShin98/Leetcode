import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
   result = (employee.merge(project,on='employee_id')
   .groupby('project_id', as_index=False)['experience_years']
   .mean()
   .rename(columns={'experience_years':'average_years'}))

   result['average_years'] = result['average_years'].round(2)

   return result