--Aggregate functions

SELECT COUNT(*) FROM student;
SELECT AVG(marks) FROM student;
SELECT MAX(marks) FROM student;
SELECT MIN(marks) FROM student;



--GROUP BY

SELECT course, COUNT(*) FROM student GROUP BY course;