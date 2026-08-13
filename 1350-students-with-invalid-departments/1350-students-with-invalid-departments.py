import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    
    df = students.merge(departments,left_on='department_id',right_on='id',how='left')
    df = df[df['name_y'].isna()]
    df = df.rename(columns=({'id_x':'id','name_x':'name'}))
    return df[['id','name']]