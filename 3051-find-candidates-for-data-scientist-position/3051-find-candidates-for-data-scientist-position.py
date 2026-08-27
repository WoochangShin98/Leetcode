import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    
    candidates = candidates[ candidates['skill'].isin(['Python', 'Tableau', 'PostgreSQL'])]
    candidates = (
        candidates.groupby('candidate_id')['skill']
        .nunique()
        .reset_index(name='skill_count')
    )
    candidates = candidates[candidates['skill_count'] == 3]

    return candidates[['candidate_id']].sort_values('candidate_id')