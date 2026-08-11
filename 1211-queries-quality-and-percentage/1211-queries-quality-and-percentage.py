import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position']
    queries['poor'] = (queries['rating']<3).astype(int)*100

    result = (
    queries.groupby('query_name')
    .agg(
        quality=('quality','mean'),
        poor_query_percentage=('poor','mean')
        )
    .reset_index()
    )

    result['poor_query_percentage'] = result['poor_query_percentage'].round(2)
    result['quality'] = (result['quality'] + 1e-6).round(2)

    return result