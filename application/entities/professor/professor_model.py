from application import db
from application.entities.user.user_model import User


class Professor(User):
    """ Professor Model for storing information about professors """
    __tablename__ = "professor"

    courses = db.relationship(
        "course", secondary="courses_x_professors",
        backref=db.backref("course", lazy="dynamic"), lazy="subquery"
    )

    def __repr__(self):
        return "Professor" + super.__repr__()