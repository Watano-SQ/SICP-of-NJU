.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
  FROM dogs AS d
  JOIN sizes AS s ON d.height > s.min AND d.height <= s.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d.name
  FROM dogs AS d
  JOIN parents AS p ON p.child = d.name
  JOIn dogs AS parent_d ON p.parent = parent_d.name
  ORDER BY parent_d.height DESC;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


-- The almighty midterm score of the SICP'25 students
CREATE TABLE midterm_almighty AS 
  SELECT MAX(p1_wwpd) + MAX(p2_env) + MAX(p3_lists) + MAX(p4_functions) + MAX(p5_abstraction) + MAX(p6_tests) + MAX(p7_generators) + MAX(p8_bonus) FROM midterm;




-- The total score distribution of SICP'25 midterm exam
CREATE TABLE midterm_distribution AS 
  WITH student_totals AS (
        SELECT total
        FROM midterm
  )
  SELECT 
    CAST(FLOOR(total/10)*10 AS FLOAT) AS section,
    COUNT(*)
  FROM student_totals
  GROUP BY section
  ORDER BY section DESC;

