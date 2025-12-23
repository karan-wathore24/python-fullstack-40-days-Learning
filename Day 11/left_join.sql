SELECT student.name, course.course_name
FROM student
LEFT JOIN course
ON student.course_id = course.id;
