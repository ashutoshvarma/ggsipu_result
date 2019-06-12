from enum import Enum

class Grade(Enum):
    A_Plus = 1
    A = 2
    B_Plus = 3
    B = 4
    C = 5
    D = 6
    E = 7
    P = 8
    F = 9


class Subject:
    def __init__(self, paper_id, paper_code=None, name=None, credit=None, minor_max=None,
                 major_max=None, type=None, department=None, mode=None, kind=None, semester=None):
        self.paper_id = paper_id
        self.paper_code = paper_code
        self.name = name
        self.credit = credit
        self.minor_max = minor_max
        self.major_max = major_max
        self.type = type
        self.department = department
        self.mode = mode
        self.kind = kind
        self.semester = semester

    @staticmethod
    def pass_marks():
        #TODO: Temprariliy using hardcoded value, update it to scrap from pdf
        return 40

    def __str__(self):
        return "{self.paper_id}-{self.name}[{self.paper_code}]".format(self=self)

    def __eq__(self, other):
        return self.paper_id == other



class Marks:
    def __init__(self, paper_id, minor, major, total, grade=None):
        self.paper_id = paper_id
        self.minor = minor
        self.major = major
        self.total = total
        self.grade = grade

    def get_subject(self):
        pass

    def __str__(self):
        return "[{self.paper_id}] Minor-{self.minor}, Major-{self.major}, Total-{self.total}".format(self=self)


class Result:

    def __init__(self, semester, marks):
        self.semester = semester
        self.marks = marks

    def get_num_drops(self):
        pass


class Student:
    def __init__(self, roll_num, full_name=None, batch_year=None):
        self.name = full_name
        self.id = roll_num
        self.batch = batch_year
        self.results = []

    def __str__(self):
        return "{self.name} - {self.id} [{self.batch}]".format(self=self)
