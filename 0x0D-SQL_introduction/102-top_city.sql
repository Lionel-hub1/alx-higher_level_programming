-- This script will return the top 3 of the average temperature of July and August (ordered from the highest to lowest temperature values) of all cities.
SELECT `city`, AVG(`value`) AS`avg_temp`
FROM `temperatures`
WHERE `month` IN (`July`, `August`)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;