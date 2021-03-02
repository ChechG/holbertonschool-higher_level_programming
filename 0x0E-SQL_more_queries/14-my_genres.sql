-- Script that lists all genres of the show Dexter.
SELECT tv_genres.name AS name FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE show_id = 8;