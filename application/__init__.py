from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

from application import config


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

from application.entities.course.course_model import Course
# from application.entities.courses_x_professors.courses_x_professors_model import CoursesXProfessors
from application.entities.group.group_model import Group
# from application.entities.groups_x_courses.groups_x_courses_model import GroupsXCourses
from application.entities.professor.professor_model import Professor
# from application.entities.student.student_model import Student
