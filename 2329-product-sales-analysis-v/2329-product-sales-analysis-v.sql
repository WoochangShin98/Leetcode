# Write your MySQL query statement below
SELECT s.user_id,
SUM(s.quantity * p.price) AS spending
FROM Sales s
LEFT JOIN Product p
ON s.product_id = p.product_id
GROUP BY user_id
ORDER BY spending DESC, user_id ASC;