import pandas as pd

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    pairs = point2_d.merge(point2_d,how='cross',suffixes=('_1', '_2'))

    pairs = pairs[
        (pairs['x_1'] != pairs['x_2']) |
        (pairs['y_1'] != pairs['y_2'])
    ]

    pairs['distance'] = np.sqrt(
        (pairs['x_2'] - pairs['x_1']) ** 2 +
        (pairs['y_2'] - pairs['y_1']) ** 2
    )


    return pd.DataFrame({
        'shortest': [round(pairs['distance'].min(), 2)]
    })