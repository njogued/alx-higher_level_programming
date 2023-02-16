-- Select subquery Nested
SELECT * FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = 'California');
