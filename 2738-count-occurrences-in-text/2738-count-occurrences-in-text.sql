# Write your MySQL query statement below
SELECT 'bull' AS word,
SUM(content REGEXP ' bull ') AS count
FROM Files

UNION ALL

SELECT 'bear', 
SUM(content REGEXP ' bear ') 
FROM Files

#UNION ALL 을 잊지말고 그리고 글자를 셀때는 SUM()이 맞음 COUNT는 FALSE도 세어버림 