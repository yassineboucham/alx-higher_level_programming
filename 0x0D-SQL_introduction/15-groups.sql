-- script that computes the score average of all records in the table
SELECT score, SUM(score) AS number FROM second_table GROUP BY number ORDER BY score DESC;
