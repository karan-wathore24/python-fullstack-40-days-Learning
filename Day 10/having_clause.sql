--HAVING clause

SELECT course, COUNT(*) 
FROM student 
GROUP BY course 
HAVING COUNT(*)>2;