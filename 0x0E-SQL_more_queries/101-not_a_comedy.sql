-- List all shows without the genre Comedy.
SELECT title
FROM tv_shows
WHERE genre IN (
	SELECT name
	FROM tv_genres
	WHERE name != 'Comedy';
)
ORDER BY title;
