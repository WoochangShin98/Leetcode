import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    condition = (
        (triangle['x'] + triangle['y'] > triangle['z'])
        & (triangle['x'] + triangle['z'] > triangle['y'])
        & (triangle['y'] + triangle['z'] > triangle['x'])
    )

    triangle['triangle'] = np.where(condition, 'Yes', 'No')

    return triangle

# np.where 를 외우자 np.where(조건,참,거짓)