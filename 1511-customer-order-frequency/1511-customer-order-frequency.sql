# Write your MySQL query statement below
# at least $100 in each month of June and July 2020.
SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
JOIN Product p
    ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING
    SUM(
        CASE 
            WHEN o.order_date >= '2020-06-01'
             AND o.order_date < '2020-07-01'
            THEN p.price * o.quantity
            ELSE 0
        END
    ) >= 100
AND
    SUM(
        CASE 
            WHEN o.order_date >= '2020-07-01'
             AND o.order_date < '2020-08-01'
            THEN p.price * o.quantity
            ELSE 0
        END
    ) >= 100;