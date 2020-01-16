from application import db
from application.entities.user.user_model import User


class Professor(User):
    """ Professor Model for storing information about professors """
    __tablename__ = "professor"

    courses = db.relationship(
        "Course", secondary="courses_and_professors",
        backref=db.backref("courses", lazy="dynamic"), lazy="subquery"
    )

    def __repr__(self):
        return "Professor" + super.__repr__()