# Write your MySQL query statement below

SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) = (
    SELECT MAX(cnt)
    FROM (
    SELECT COUNT(project_id) as cnt 
    FROM Project
    GROUP BY project_id
) t
);
