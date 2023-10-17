-- lists all records of the second_table with a value in the database
SELECT score, name
FROM second_table
WHERE name is not NULL
ORDER BY score DESC;
