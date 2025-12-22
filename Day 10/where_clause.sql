-- WHERE clause examples


SELECT * FROM student WHERE marks >70;
SELECT * FROM student WHERE marks BETWEEN 60 AND 90;
SELECT * FROM student WHERE name LIKE 'K%';
SELECT * FROM student WHERE name IN ('KARAN','NIKHIL','SUMEDH');