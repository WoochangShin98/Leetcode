SELECT employee_id,
    CASE 
        WHEN employee_id % 2 = 1 
        AND LEFT(name,1) <> 'M'
    THEN salary 
    ELSE 0 
    END AS bonus
FROM Employees
ORDER BY employee_id; 

# 조건을 검색할땐 CASE에는 변수명을 적지 않는다. 다만, 값은 CASE 변수명을 기재한다 