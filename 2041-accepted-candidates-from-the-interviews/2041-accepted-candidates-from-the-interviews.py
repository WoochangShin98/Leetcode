import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    total_score = rounds.groupby('interview_id',as_index=False)['score'].sum()
    result = candidates.merge(total_score,on='interview_id',how='left')
    result = result[(result['years_of_exp'] >= 2) & (result['score']>15)]
    return result[['candidate_id']]