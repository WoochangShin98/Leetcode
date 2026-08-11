# Write your MySQL query statement below
SELECT user_id, 
CONCAT(UPPER(LEFT(name,1)),LOWER(SUBSTRING(name,2))) AS name
FROM Users
ORDER BY user_id;

# concat으로 붙이는 방법 잊지말기, substring(변수,시작순서)