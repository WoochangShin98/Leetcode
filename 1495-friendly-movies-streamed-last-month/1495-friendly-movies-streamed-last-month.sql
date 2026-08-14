# Write your MySQL query statement below
SELECT DISTINCT c.title
FROM Content c
LEFT JOIN TVProgram t
    ON c.content_id = t.content_id
WHERE t.program_date >= '2020-06-01'
  AND t.program_date < '2020-07-01'
  AND c.content_type = 'Movies'
  AND c.Kids_content = 'Y';