from application import db


class GroupsXCourses(db.Model):
    """ GroupsXCourses Model for storing relations between groups and courses """
    __tablename__ = "groups_x_courses"

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), primary_key=True)
