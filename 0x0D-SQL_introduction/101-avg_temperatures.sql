-- displays the average temperature (Fahrenheit) by city ordered by
--btemperature (descending).
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY avg_temp DESC
GROUP BY city;
