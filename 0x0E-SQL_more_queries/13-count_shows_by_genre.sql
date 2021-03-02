-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows FROM tv_genres GROUP BY tv_genres.name ORDER BY COUNT(tv_genres.id) DESC;
