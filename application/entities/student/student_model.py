from application import db
from application.entities.user.user_model import User
from application.entities.education_information import EducationDegree, EducationForm, EducationBasis


class Student(User):
    """ Student Model for storing information about students """
    __tablename__ = "student"

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    entrance_year = db.Column(db.Integer, nullable=True, default=None)
    education_degree = db.Column(db.Enum(EducationDegree), nullable=False, default=EducationDegree.nan)
    education_form = db.Column(db.Enum(EducationForm), nullable=False, default=EducationForm.nan)
    education_basis = db.Column(db.Enum(EducationBasis), nullable=False, default=EducationBasis.nan)

    def __repr__(self):
        return "Student " + super.__repr__()