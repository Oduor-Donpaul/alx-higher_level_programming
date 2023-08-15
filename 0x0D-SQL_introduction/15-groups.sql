-- script that list number of records with the same score 
-- in table second_table of the database hbtn_0c_0 in MYSQL Server
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;
