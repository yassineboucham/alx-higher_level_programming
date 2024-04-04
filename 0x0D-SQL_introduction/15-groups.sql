-- script that computes the score average of all records in the table
SELECT score, SUM(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
