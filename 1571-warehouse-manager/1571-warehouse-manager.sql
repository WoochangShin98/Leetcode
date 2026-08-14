# Write your MySQL query statement below
SELECT name AS warehouse_name,
SUM((Width*Length*Height)*units) AS volume
FROM Warehouse w
LEFT JOIN Products p
ON w.product_id = p.product_id
GROUP BY name