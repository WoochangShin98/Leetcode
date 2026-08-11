import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    condition = views['author_id'] == views['viewer_id']
    result = views[condition]
    result = result.sort_values(by='author_id')
    result = result.drop_duplicates(subset=['author_id'])
    result = result.rename(columns={'author_id':'id'})
    return result[['id']]

# drop_duplicates() -> subset=['변수'] don't forget