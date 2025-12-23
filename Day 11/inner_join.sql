select student.name, course.course_name 
from student
INNER JOIN cource 
ON student.cource_id=cource_id;