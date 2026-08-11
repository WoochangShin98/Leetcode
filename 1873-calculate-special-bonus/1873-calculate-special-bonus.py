import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    result = employees.copy()

    mask = (
        (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
        )

    result.loc[mask,'bonus'] = employees.loc[mask,'salary']

    return result[['employee_id','bonus']].sort_values(by='employee_id')

    # 내가 기존에 알던 변수 지정은 행들이 지워진다.
    # 따라서 copy() 복사를 해서 또 다른 데이터프레임을 생성한 뒤에 , 새로운 칼럼을 붙어준다
    # 여기서 새롭게 배운거는 변수.loc[조건,칼럼] = 값 이다 
    