import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    result = department.pivot(index='id',columns='month',values='revenue')

    result = result.reindex(columns=months)

    result.columns = [f'{m}_Revenue' for m in result.columns]

    return result.reset_index()