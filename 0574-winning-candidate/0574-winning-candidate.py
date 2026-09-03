import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    max_id = vote['candidateId'].value_counts().idxmax()
    df = candidate[candidate['id'] == max_id][['name']]
    return df