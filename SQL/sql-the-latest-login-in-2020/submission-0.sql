-- Write your query below
SELECT l.user_id, MAX(l.time_stamp) AS last_stamp
FROM logins l
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
GROUP BY user_id;

