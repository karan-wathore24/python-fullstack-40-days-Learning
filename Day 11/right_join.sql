SELECT student.name, course.course_name
FROM student
RIGHT JOIN course
ON student.course_id = course.id;
