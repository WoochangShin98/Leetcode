import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person_condition = person.merge(address,on='personId',how='left')
    return person_condition[['firstName','lastName','city','state']]
    