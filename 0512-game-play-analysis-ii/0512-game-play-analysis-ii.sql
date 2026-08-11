# Write your MySQL query statement below
SELECT a.player_id, a.device_id
FROM Activity a 
JOIN (
    SELECT player_id, MIN(event_date) as first_date
    FROM Activity
    GROUP BY player_id
) b
ON a.player_id = b.player_id
AND a.event_date = b.first_date
