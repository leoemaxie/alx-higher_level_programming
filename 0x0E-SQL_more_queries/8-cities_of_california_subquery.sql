-- Lists all the cities of California that can be found in the database
--hbtn_0d_usa.
SELECT id, cities
FROM hbtn_0d_usa
WHERE name = 'California' IN (
	SELECT ;
