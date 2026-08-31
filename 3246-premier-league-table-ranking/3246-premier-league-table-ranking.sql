# Write your MySQL query statement below
SELECT
    team_id,team_name,points,
    RANK() OVER (ORDER BY points DESC) AS position
FROM (
    SELECT
        team_id,team_name,wins * 3 + draws AS points
    FROM TeamStats
) t
ORDER BY points DESC, team_name ASC;