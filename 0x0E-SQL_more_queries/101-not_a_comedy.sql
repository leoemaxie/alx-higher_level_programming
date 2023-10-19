-- List all shows without the genre Comedy.
SELECT DISTINCT title
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_show.id

LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title NOT IN (
	SELECT title
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.show_id = tv_show_genres.id

	INNER JOIN tv_genres
	ON tv_show_genres.id = s.genre_id
	WHERE tv_genres.name = "Comedy"
)
ORDER BY title;
