-- Displays the 3 cities with the highest averagebtemperatures between
-- July and August.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
ORDER BY avg_temp DESC
LIMIT 3;
