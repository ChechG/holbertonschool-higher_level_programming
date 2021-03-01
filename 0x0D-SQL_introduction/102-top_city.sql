-- Script that displays top 3 of cities temp during Jul and Aug ord by temp (desc).
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
