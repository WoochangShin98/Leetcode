# Write your MySQL query statement below
SELECT c.name
FROM Candidate c
JOIN Vote v
  ON c.id = v.candidateId
GROUP BY c.id, c.name
ORDER BY COUNT(*) DESC
LIMIT 1;