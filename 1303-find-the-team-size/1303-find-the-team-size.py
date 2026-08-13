import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    df= (
        employee.groupby('team_id')['employee_id']
        .nunique()
        .reset_index()
        )

    df = employee.merge(df,on='team_id',how='left')
    df=df.rename(columns={'employee_id_x':'employee_id','employee_id_y':'team_size'})
    
    return df[['employee_id','team_size']]