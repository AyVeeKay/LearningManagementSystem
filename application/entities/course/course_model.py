from application import db


class Course(db.Model):
    """ Course Model for storing information about courses """
    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    professors = db.relationship(
        "Professor",
        secondary="courses_and_professors",
        backref=db.backref("professors", lazy="dynamic"),
        lazy="subquery"
    )
    groups = db.relationship(
        "Group",
        secondary="courses_and_groups",
        backref=db.backref("groups", lazy="dynamic"),
        lazy="subquery"
    )

    def __repr__(self):
        return f"Course {self.name}"
