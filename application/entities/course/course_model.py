from application import db


class Course(db.Model):
    """ Course Model for storing information about courses """
    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    professors = db.relationship(
        "professor",
        secondary="courses_x_professors",
        backref=db.backref("professor", lazy="dynamic"),
        lazy="subquery"
    )
    groups = db.relationship(
        "group",
        secondary="courses_x_groups",
        backref=db.backref("group", lazy="dynamic"),
        lazy="subquery"
    )

    def __repr__(self):
        return f"Course {self.name}"
