import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    n = len(seat)

    seat['id'] = np.where(
        seat['id'] % 2 == 1,
        seat['id'] + 1,
        seat['id'] - 1,
    )

    if n % 2 == 1:
        seat.loc[seat['id']==n+1,'id'] = n

    return seat.sort_values('id')