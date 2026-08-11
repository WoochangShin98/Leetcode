import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
   result = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$')]
   return result

   # str.match() 와 정규표현식을 잊지말자 0개 이상은 '*'을 붙인다 