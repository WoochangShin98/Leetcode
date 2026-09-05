import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = department.merge(student,on='dept_id',how='left')
    df = (
        df.groupby('dept_name', as_index=False)
          .agg(student_number=('student_id', 'count'))
          .sort_values(
              ['student_number', 'dept_name'],
              ascending=[False, True]
          )
    )
    return df[['dept_name','student_number']]