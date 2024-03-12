-- list number of records grouped by score
-- and ordered by score
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;