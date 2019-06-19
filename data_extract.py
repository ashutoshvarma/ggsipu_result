# -*- coding: utf-8 -*
"""Data Extraction module

This module provide classes to extract required data from
string data formatted in a known manner. Extracted data will
be returned in a suitable objects. For each type of string format
there are specialised classes.

TODO:
    None
"""


from objects import Student, Marks, Result, Subject
from util import rm_extra_whitespace, group_iter
import re


class pdftotext_dump_extract:

    @staticmethod
    def _get_scheme_dates(data):
        # Capture Date of format dd/mm/yyy
        RE_DATE = re.compile(r"\d{2}/\d{2}/\d{4}")
        match = RE_DATE.search(data)
        return match.group() if match else None

    @staticmethod
    def _get_semester(data):
        # Match one or more numbers prefix by 'Sem' + any
        # other than digit + ':' + zero or more '0's
        RE_SEMESTER = re.compile(r'(?:Sem\D*:\s*0*)(\d+)')
        match = RE_SEMESTER.search(data)
        return int(match.group(1)) if match else None

    @staticmethod
    def _get_batch(data):
        # Match one or more numbers prefix by 'Batch' + any
        # other than digit + ':' + zero or more '0's
        RE_BATCH = re.compile(r'(?:Batch\D*:\s*0*)(\d+)')
        match = RE_BATCH.search(data)
        return int(match.group(1)) if match else None

    @staticmethod
    def _iter_paper_ids(data):
        # Match 5 digit number followed by '(' from begininig
        RE_PAPER_ID = re.compile(r'^\d{5}(?=\()')
        for word in data.split():
            match = RE_PAPER_ID.search(word)
            paper_id = match.group() if match else None
            if paper_id:
                yield int(paper_id)

    @staticmethod
    def _iter_marks(data):
        # Number of items to ignore in data.split() as they contain
        # 'SID:' and sid number
        NUM_WORDS_IGNORE = 2
        DEFAULT_MARKS = None
        data = data.split()[NUM_WORDS_IGNORE:]
        return group_iter(data, 2, DEFAULT_MARKS)

    @staticmethod
    def _iter_total_marks(data):
        """
        Return (total, grade) iterable
        """
        # RE_TOTAL_MARKS = re.compile(r"""
        #                             (?P<total>\b\d{2}\b)(?=\()  # whole 2 digits number followed by '('
        #                             \(                          # Match '('
        #                             (?P<grade>[^)]+)            # Match any other than ')'
        #                             """, re.VERBOSE)

        # To ignore the first number in data.split() as they contain
        # serial num
        NUM_WORDS_IGNORE = 1
        RE_BTW_PARANTHESES = re.compile(r"""
                            \(          #Match Opening Parantheses
                            ([^)]+)     #Match characters except ')' one or more (Capturing Group)
                            \)          #Match Closing Parantheses
                            """, re.VERBOSE)
        data_split = data.split()[NUM_WORDS_IGNORE:]
        for line in data_split:
            ex_data = RE_BTW_PARANTHESES.split(line)
            if len(ex_data) == 1:
                yield ex_data[0], None
            else:
                yield ex_data[:2]

    @staticmethod
    def _get_subject(data, semester=None):
        RE_SUBJ_DETAILS = re.compile(r"""
                            (?P<index>\d{,2})\s*
                            (?P<id>\d{5})\s*
                            (?P<paper_code>\w{5})\s*
                            (?P<name>(\D)+)
                            (?P<credit>\d)\s*
                            (?P<type>\w+)\s*
                            (?P<exam>\w+)\s*
                            (?P<mode>\w+)\s*
                            (?P<kind>\w+)\s*
                            (?:(?P<minor_max>\d*)(?:--)?)\s*
                            (?P<major_max>\d+)
                            """, re.VERBOSE)

        subj_match = RE_SUBJ_DETAILS.search(data)
        if subj_match:
            minor_max = subj_match.group('minor_max')
            major_max = subj_match.group('major_max')
            credit = subj_match.group("credit")
            sub_type = subj_match.group('type')
            exam = subj_match.group('exam')
            kind = subj_match.group('kind')
            mode = subj_match.group('mode')
            paper_code = subj_match.group('paper_code')
            name = rm_extra_whitespace(subj_match.group('name'))

            # Validation
            minor_max = minor_max if minor_max.isdigit() else None
            major_max = major_max if major_max.isdigit() else None

            return Subject(subj_match.group('id'), paper_code, name, credit,
                           minor_max, major_max, sub_type, exam, mode, kind, semester)

    @staticmethod
    def has_page_subejcts(pg_data):
        """Check if page contains subjects data.
        """

        RE_IS_SUBJECT_PAGE = re.compile(r"\(.*SCHEME.+OF.+EXAMINATIONS*\)")
        match = RE_IS_SUBJECT_PAGE.search(pg_data)
        if match:
            return True
        else:
            return False

    @staticmethod
    def has_page_results(pg_data):
        """Check if page contains results data.
        """

        RE_IS_RESULTS_PAGE = re.compile(r"RESULT.+TABULATION.+SHEET")
        match = RE_IS_RESULTS_PAGE.search(pg_data)
        if match:
            return True
        else:
            return False

    @classmethod
    def iter_subjects(cls, raw_data, force=False):
        """Iterate through subjects extracted from page data.

        Retieves the subject data from given page data assuming the 
        data to be from pdftotext with -simple flag. If force param is False
        it wont't check for data format.

        Args:
            raw_data: Raw data of a single page.
            force: If True, check whether data contains subjects or not.

        Returns:
            A generator object of Subject type.
        """
        if force and not cls.has_page_subejcts(raw_data):
            return None

        raw_data = raw_data.splitlines()

        LINE_SEMESTER = 7  # Semester , Programme Code, Scheme ID
        LINE_SUBJ_START = 11  # Subject Details
        SUBJ_GAP = 1    # Gap btw two consecutive subject lines

        semester = cls._get_semester(raw_data[LINE_SEMESTER])

        for raw in raw_data[LINE_SUBJ_START::SUBJ_GAP+1]:
            yield cls._get_subject(raw, semester)

    @classmethod
    def iter_results(cls, raw_data, force=False):
        """Iterate through results extracted from page data.

        Retieves the results data from given page data assuming the 
        data to be from pdftotext with -simple flag. If force param is False
        it wont't check for data format.

        Args:
            raw_data: Raw data of a single page.
            force: If True, check whether data contains subjects or not.

        Returns:
            A generator object of Result type.
        """
        if force and not cls.has_page_results(raw_data):
            return None

        raw_data = raw_data.splitlines()

        LINE_SEMESTER_BATCH = 17
        GAP_TOTAL_MARKS = 4
        GAP_MARKS = 2
        GAP_NAME = 1

        # Match whole 11 digits number
        RE_ROLL_NUM = re.compile(r'\b\d{11}\b')

        semester = cls._get_semester(raw_data[LINE_SEMESTER_BATCH])
        batch = cls._get_batch(raw_data[LINE_SEMESTER_BATCH])

        for i, line in enumerate(raw_data):
            roll_match = RE_ROLL_NUM.search(line)
            if roll_match:
                # list with subject_ids
                paper_ids = list(cls._iter_paper_ids(line))
                # list of (minor, major) marks
                raw_marks = list(cls._iter_marks(raw_data[i + GAP_MARKS]))
                # list of (total, grade)
                total_and_grades = list(
                    cls._iter_total_marks(raw_data[i + GAP_TOTAL_MARKS]))
                # Name of student
                name = rm_extra_whitespace(raw_data[i + GAP_NAME])

                # Remove line till total marks, to avoid processing them again
                del raw_data[i: GAP_TOTAL_MARKS]

                new_result = Result(roll_match.group(), semester, name, batch)
                for paper_id, mark, total_grade in zip(paper_ids, raw_marks, total_and_grades):
                    
                    minor = int(mark[0]) if mark[0].isdigit() else None
                    major = int(mark[1]) if mark[1].isdigit() else None

                    temp_mark = Marks(
                        paper_id, minor, major, total_grade[0], total_grade[1])
                    new_result.add_mark(paper_id, temp_mark)
                yield new_result
