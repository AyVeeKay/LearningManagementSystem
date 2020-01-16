from application import db



class CoursesXProfessors(db.Model):
    """ CoursesXProfessors Model for storing relations between courses and professors """
    __tablename__ = "courses_x_professors"

    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey("professor.id"), primary_key=True)
