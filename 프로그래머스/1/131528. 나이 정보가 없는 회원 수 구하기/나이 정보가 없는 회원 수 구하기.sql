SELECT COUNT(*) AS USERS
FROM USER_INFO
GROUP BY AGE
HAVING AGE IS NULL
