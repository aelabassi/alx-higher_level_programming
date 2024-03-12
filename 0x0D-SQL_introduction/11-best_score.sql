-- list records with score >= 10
-- order by score with top first
SELECT `score`, `name`
WHERE `score` >= 10
ORDER BY `score` DESC;