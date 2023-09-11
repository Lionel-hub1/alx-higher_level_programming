-- This script will return the number of records with the same score from the second_table table.
SELECT `score`, COUNT(*) AS `number` FROM second_table GROUP BY `score` ORDER BY `number` DESC;