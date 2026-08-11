SELECT d.name AS Department,
e.name AS Employee,
e.salary AS Salary
FROM Employee e
JOIN Department d
ON e.departmentID = d.id
JOIN(
SELECT departmentId, max(salary) as max_salary
FROM Employee
GROUP BY departmentId) m
on d.id = m.departmentId
and e.salary = m.max_salary