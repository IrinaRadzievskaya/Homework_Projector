from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base = declarative_base()
#
#
# class Student(Base):
# 	__tablename__ = 'students'
#
# 	id = Column(Integer, primary_key=True)
# 	name = Column(String)
#
# 	subjects = relationship("StudentSubject", back_populates="student")
#
#
# class Subject(Base):
# 	__tablename__ = 'subjects'
#
# 	id = Column(Integer, primary_key=True)
# 	name = Column(String)
#
# 	students = relationship("StudentSubject", back_populates="subject")
#
#
# class StudentSubject(Base):
# 	__tablename__ = 'student_subjects'
#
# 	student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
# 	subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
#
# 	student = relationship("Student", back_populates="subjects")
# 	subject = relationship("Subject", back_populates="students")



# Assuming you have already created the engine and session
engine = create_engine('postgresql://username:password@localhost/database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Query the students who visited 'English' classes
english_students = session.query(Student).join(StudentSubject).join(Subject).filter(Subject.name == 'English').all()

# Print the names of English students
for student in english_students:
	print(student.name)