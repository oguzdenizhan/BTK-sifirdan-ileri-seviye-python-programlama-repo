alter table classlesson
add CONSTRAINT fk_classlesson_class
FOREIGN KEY (classId) REFERENCES class(id)

alter table classlesson
add CONSTRAINT fk_classlesson_lesson
FOREIGN KEY (lessonId) REFERENCES lesson(id)

alter table classlesson
add CONSTRAINT fk_classlesson_teacher
FOREIGN KEY (teacherId) REFERENCES teacher(id)