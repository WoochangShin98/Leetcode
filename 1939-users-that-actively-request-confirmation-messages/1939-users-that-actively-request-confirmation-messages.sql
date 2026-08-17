# Write your MySQL query statement below
SELECT DISTINCT user_id
FROM (
    SELECT user_id,
    time_stamp,
    LAG(time_stamp) OVER(PARTITION BY user_id ORDER BY time_stamp) AS prev_time
    FROM Confirmations
) t
WHERE TIMESTAMPDIFF(SECOND,prev_time,time_stamp) <= 24*60*60
ORDER BY user_id