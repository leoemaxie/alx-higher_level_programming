-- List all genres not linked to the show Dexter 
SELECT name
FROM tv_genres
WHERE name IN (
	SELECT genre
	FROM tv_shows
	WHERE title != 'Dexter';
)
ORDER BY name;
