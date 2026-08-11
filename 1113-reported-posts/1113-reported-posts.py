import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:

    actions = actions[
        (actions['action_date'] == '2019-07-04') &
        (actions['action'] == 'report')
    ]

    result = (
        actions.groupby('extra')
        .agg(report_count=('post_id', 'nunique'))
        .reset_index()
        .rename(columns={'extra': 'report_reason'})
    )

    return result