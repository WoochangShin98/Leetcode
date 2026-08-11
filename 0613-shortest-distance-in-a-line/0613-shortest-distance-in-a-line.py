import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    point = point.sort_values('x')
    point['x1'] = point['x'].shift(1)
    point['shortest'] = point['x'] - point['x1']
    result = point['shortest'].min()

    return pd.DataFrame({'shortest':[result]})

