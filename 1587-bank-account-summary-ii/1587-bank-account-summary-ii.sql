# Write your MySQL query statement below
SELECT name,
SUM(amount) AS balance
FROM Transactions t 
LEFT JOIN Users u
ON t.account = u.account
GROUP BY t.account, name
HAVING SUM(amount) > 10000