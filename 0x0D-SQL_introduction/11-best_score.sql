-- This script will return the top score from the second_table table.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;