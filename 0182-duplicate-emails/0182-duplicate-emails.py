import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person.groupby('email').size()
    result = result[result >= 2]
    return result.index.to_frame(name='Email')
# .index 는 index를 가져오는거 .to_frame() 은 series를 frame으로 