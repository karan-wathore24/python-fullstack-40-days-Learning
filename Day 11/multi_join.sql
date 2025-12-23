SELECT s.name, c.course_name
FROM student s
INNER JOIN course c
ON s.course_id = c.id;
