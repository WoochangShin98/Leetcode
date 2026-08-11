# Write your MySQL query statement below

    SELECT project_id, ROUND(SUM(experience_years)/COUNT(project_id),2) as average_years
    FROM Employee e
    JOIN Project p
    ON e.employee_id = p.employee_id 
    GROUP BY project_id
