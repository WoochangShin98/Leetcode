import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    problems['percent'] = (problems['likes'] / (problems['likes'] + problems['dislikes'])) * 100
    df = problems[problems['percent'] < 60]
    df = df[['problem_id']].sort_values(
        by='problem_id',
        ascending=True
    )

    return df

