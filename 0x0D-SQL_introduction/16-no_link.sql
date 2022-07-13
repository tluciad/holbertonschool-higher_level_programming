-- SELECT score, count(score) as number FROM 
-- second_table GROUP BY score ORDER BY score DESC
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;