import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # axis=0 -> vertical 
    friends = pd.concat([
        request_accepted['requester_id'],
        request_accepted['accepter_id']
    ])
    
    counts = friends.value_counts()

    return pd.DataFrame({
        'id':[counts.idxmax()],
        'num':[counts.max()]
    })