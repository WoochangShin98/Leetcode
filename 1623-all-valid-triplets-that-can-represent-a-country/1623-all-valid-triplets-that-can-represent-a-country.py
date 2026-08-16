import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
# merge(,,suffixes=())
    df = (
        school_a.merge(school_b,how='cross',suffixes=('_a','_b'))
                .merge(school_c,how='cross')
    )

    df = df[
        (df['student_id_a'] != df['student_id_b']) &
        (df['student_id_a'] != df['student_id']) &
        (df['student_id_b'] != df['student_id']) &
        (df['student_name_a'] != df['student_name_b']) &
        (df['student_name_a'] != df['student_name']) &
        (df['student_name_b'] != df['student_name']) 
    ]
    
    df = df.rename(columns={
        "student_name_a": "member_A",
        "student_name_b": "member_B",
        "student_name": "member_C"
    })

    return df[["member_A","member_B","member_C"]]

