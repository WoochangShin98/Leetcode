import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    name = f'getNthHighestSalary({N})'
    salary = employee['salary'].sort_values(ascending=False).drop_duplicates()

    if N <= 0 or len(salary) < N:
        return pd.DataFrame({
            name : [None]
            })
    else:
        return pd.DataFrame({
            name : [salary.iloc[N-1]]
            })
# 문자열은 f'' 로 해야함
# salary 변수로 넣는 이유는 employee 로 하면 우측이 시리즈라서 내가 원하는 결과가 안나옴
# 순차적으로 오름차순 해야함, 중복인것도 지워야함
# 입력값 보다 작거나, 음수일 경우 도 있으니 넣어야함 

    