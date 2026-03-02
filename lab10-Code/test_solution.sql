.read lab10_data.sql
SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;
