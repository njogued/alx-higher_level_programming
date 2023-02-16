-- Show how many students got a certain score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
