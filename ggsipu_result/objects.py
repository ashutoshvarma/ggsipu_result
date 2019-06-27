"""Module having classes for data storing.
"""

import json
from .util import JSONSerializable


class Subject(JSONSerializable):
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
        # TODO: Temprariliy using hardcoded value, update it to scrap from pdf
        return 40

    @staticmethod
    def max_marks():
        # TODO: Temprariliy using hardcoded value, update it to scrap from pdf
        return 100

    def __str__(self):
        return "{self.paper_id}-{self.name}[{self.paper_code}]".format(self=self)

    def __eq__(self, other):
        return self.paper_id == other


class Marks(JSONSerializable):
    def __init__(self, paper_id, minor, major, total, grade=None):
        self.paper_id = paper_id
        self.minor = minor
        self.major = major
        self.total = total
        self.grade = grade

    def __str__(self):
        return "[{self.paper_id}] Minor-{self.minor}, Major-{self.major}, Total-{self.total}".format(self=self)


class Result(JSONSerializable):

    def __init__(self, roll_num, semester, student_name=None, batch=None, marks=None):
        self.semester = semester
        self.roll_num = roll_num
        self.student_name = student_name
        self.batch = batch
        self.marks = marks if marks else {}

    def get_mark_drops(self):
        # for paper_id, mark in self.marks.items():
        #     if mark.total < Subject.pass_marks():
        #         yeild mark
        return [item[1] for item in self.marks.items() if item[1].total and item[1].total < Subject.pass_marks()]

    def get_num_drops(self):
        return len(self.get_mark_drops())

    def get_marks_by_paper(self, paper_id):
        return self.marks[paper_id]

    def get_marks(self, min_marks=0, max_marks=Subject.max_marks()):
        """Return the marks whose total is more than 'min_marks' and more than 'max_marks'
        """
        return [item[1] for item in self.marks.items() if min_marks <= item[1].total <= max_marks]

    def add_mark(self, paper_id, mark):
        if isinstance(paper_id, int):
            self.marks[paper_id] = mark
        else:
            raise TypeError("paper_id should be of int type")

    def __str__(self):
        return "Result: [{self.roll_num}]{self.student_name}({self.batch}) Semester: {self.semester}".format(self=self)


class Student(JSONSerializable):
    def __init__(self, roll_num, full_name=None, batch_year=None, programme_code=None,
                 programme_name=None, institution_code=None, institution_name=None):
        self.name = full_name
        self.id = roll_num
        self.batch = batch_year
        self.results = {}
        self.programme_code = programme_code
        self.programme_name = programme_name
        self.institution_code = institution_code
        self.institution_name = institution_name

    def iter_results(self):
        """Return generator object of all results.
        """
        for sem in self.results:
            yield self.results[sem]

    def get_result_by_sem(self, sem):
        return self.results[sem]

    def add_result(self, res, semester):
        """Add the result to results dict.

        If result for semester is already present then it ignores current.
        """
        if not semester in self.results:
            self.update_result(res, semester)
        # else:
        #     raise Exception("Result for semester {} is already present.".format(semester))

    def update_result(self, res, semester):
        """Update the result for given semester.
        """
        if isinstance(semester, int):
            self.results[semester] = res
        else:
            raise TypeError("semester should be of int type")

    def __str__(self):
        return "{self.name} - {self.id} [{self.batch}]".format(self=self)
