-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres INNER JOIN tv_shows WHERE tv_show_genres.genre_id >= 1 ORDER BY tv_shows.title, tv_show_genres.genre_id;
