import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    request = friend_request[['sender_id', 'send_to_id']].drop_duplicates().shape[0]
    accepted = request_accepted[['requester_id', 'accepter_id']].drop_duplicates().shape[0]

    if request == 0:
        result = 0.00
    else:
        result = round(accepted / request, 2)

    return pd.DataFrame({'accept_rate': [result]})