import pandas as pd

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    condition = (
        (triangles['A']+ triangles['B'] <= triangles['C']) |
        (triangles['A']+ triangles['C'] <= triangles['B']) |
        (triangles['B']+ triangles['C'] <= triangles['A']),

        (triangles['A'] == triangles['B']) &
        (triangles['B'] == triangles['C']),

        (triangles['A'] == triangles['B']) |
        (triangles['A'] == triangles['C']) |
        (triangles['B'] == triangles['C'])
    )

    options = ['Not A Triangle','Equilateral','Isosceles']

    triangles['triangle_type'] = np.select(
        condition,
        options,
        default = 'Scalene'
    )

    return triangles[['triangle_type']]