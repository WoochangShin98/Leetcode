import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    tiv_count = insurance.groupby('tiv_2015')['pid'].transform('count')
    location_count = insurance.groupby(['lat','lon'])['pid'].transform('count')

    result = insurance[(tiv_count > 1)&(location_count == 1)]

    return pd.DataFrame({
        'tiv_2016':[round(result['tiv_2016'].sum(),2)]
    })
