# Write your MySQL query statement below
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (
    SELECT MAX(cnt) 
    FROM (
        SELECT SUM(price) AS cnt
        FROM Sales
        GROUP BY seller_id
    ) t
 );
