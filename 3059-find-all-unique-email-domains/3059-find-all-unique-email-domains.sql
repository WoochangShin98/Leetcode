# Write your MySQL query statement below
SELECT
SUBSTRING_INDEX(email,'@',-1) AS email_domain,
COUNT(*) AS count
FROM Emails
WHERE SUBSTRING_INDEX(email,'@',-1) LIKE '%.com'
GROUP BY email_domain
ORDER BY email_domain
