import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    posts = (
        submissions[submissions['parent_id'].isna()][['sub_id']]
        .drop_duplicates()
        .rename(columns={'sub_id':'post_id'})
    )

    comment = (
        submissions[submissions['parent_id'].notna()]
        .drop_duplicates()
    )

    result = posts.merge(
        comment,
        left_on='post_id',
        right_on='parent_id',
        how='left'
    )

    result = (
        result.groupby('post_id',as_index=False)['sub_id']
        .nunique()
        .rename(columns={'sub_id':'number_of_comments'})
        .sort_values('post_id')
    )
    
    return result