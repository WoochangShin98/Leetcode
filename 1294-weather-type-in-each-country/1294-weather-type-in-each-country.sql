# Write your MySQL query statement below
SELECT c.country_name,
    CASE
    WHEN AVG(w.Weather_state) <= 15 THEN 'Cold'
    WHEN AVG(w.Weather_state) >= 25 THEN 'Hot'
    ELSE 'Warm'
    END AS weather_type
FROM Countries c
LEFT JOIN Weather w
ON c.country_id = w.country_id
WHERE w.day  BETWEEN '2019-11-01' AND '2019-11-30'
GROUP BY c.country_id, country_name
