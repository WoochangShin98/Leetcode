import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients['conditions'].str.contains(r'( |^)DIAB1')
    return patients[result]

    # str. 에 match, contains, startswith 헷갈리지말자 
    # startswith는 정규표현식을 사용안한다 , 검사는 문자열 시작부터
    # contains는 정규표현식을 사용가능하다, 검사는 문자열 어디든
    # match  는 문자열 시작부터 정규표현식 매칭 