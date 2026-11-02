import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    df = enrollments.sort_values(
        by=['student_id','grade','course_id'],
        ascending=[True,False,True]
    )
    df = df.drop_duplicates(subset='student_id',keep='first')
    return df