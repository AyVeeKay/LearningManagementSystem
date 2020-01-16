import enum


class EducationDegree(enum.Enum):
    nan = 1
    bachelor = 2
    specialist = 3
    master = 4


class EducationBasis(enum.Enum):
    nan = 1
    budget = 2
    contract = 3


class EducationForm(enum.Enum):
    nan = 1
    full_time = 2
    distance = 3
    evening = 4
