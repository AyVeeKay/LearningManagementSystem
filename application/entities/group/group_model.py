from application import db


class Group(db.Model):
    """ Group Model for storing information about groups of students """
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), nullable=False, unique=True)

    n_course = db.Column(db.Integer, nullable=False, default=1)
    group_name = db.Column(db.String(100), nullable=False, unique=True)
    faculty_name = db.Column(db.String(100), nullable=False)

    students = db.relationship("student", backref="group", lazy="dynamic")
    courses = db.relationship(
        "course",
        secondary="courses_x_groups",
        backref=db.backref("course", lazy="dynamic"), lazy="subquery"
    )

    def __repr__(self):
        return f"Group {self.group_name}"
