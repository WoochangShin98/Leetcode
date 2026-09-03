import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    result = survey_log.groupby('question_id')['action'].agg(
        show_count = lambda x: (x=='show').sum(),
        answer_count = lambda x: (x=='answer').sum()
    ).reset_index()

    result['answer_rate'] = result['answer_count'] / result['show_count'] 

    result = result.sort_values(
        by=['answer_rate', 'question_id'],
        ascending=[False, True]
    )

    return result[['question_id']].head(1).rename(columns={'question_id': 'survey_log'})