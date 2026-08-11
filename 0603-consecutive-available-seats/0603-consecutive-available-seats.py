import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    condition = (cinema['free'].eq(1) & (cinema['free'].shift(1).eq(1) | cinema['free'].shift(-1).eq(1)))
    cinema = cinema[condition]
    cinema = cinema.sort_values('seat_id')
    return cinema[['seat_id']]
# .eq(1) 은 == 1 이랑 같은거, bo