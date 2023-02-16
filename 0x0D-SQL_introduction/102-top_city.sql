-- Select the three cities with highest avg temp for July and August
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month > 6 AND month < 9 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
