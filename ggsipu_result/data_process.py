# -*- coding: utf-8 -*
"""Data Processing module

This module provide classes to extract required data from
string data formatted in a known manner. Extracted data will
be returned in a suitable objects. For each type of string format
there are specialised classes.

TODO:
    None
"""


from .objects import Student, Marks, Result, Subject
from .util import rm_extra_whitespace, group_iter
import re


class DataProcessingError(Exception):
    pass


class DataNotSufficientError(DataProcessingError):
    pass


class DataNotFoundError(DataProcessingError):
    pass



def _get_scheme_dates(data):
    """Get first occurance of date in 'dd/mm/yyy' format."""
    # Capture Date of format dd/mm/yyy
    RE_DATE = re.compile(r"\d{2}/\d{2}/\d{4}")
    match = RE_DATE.search(data)
    return match.group() if match else None


def _get_semester(data):
    """
    Extract the semester number in given data

    Match one or more digits prefix by 'Sem' + any
    other than digit + ':' + zero or more '0's

    Args:
        data: single line of string having semeter details

    Return:
        int type if semeter number found else None
    """
    RE_SEMESTER = re.compile(r'(?:Sem\D*:\s*0*)(\d+)')
    match = RE_SEMESTER.search(data)
    return int(match.group(1)) if match else None


def _get_batch(data):
    """
    Returns the batch year in given data

    Match one or more numbers prefix by 'Batch' + any
    other than digit + ':' + zero or more '0's

    Args:
        data: single line of string having batch details

    Return:
        int type if batch year found else None
    """
    RE_BATCH = re.compile(r'(?:Batch\D*:\s*0*)(\d+)')
    match = RE_BATCH.search(data)
    return int(match.group(1)) if match else None


def _iter_paper_id_credits(data):
    """
    Iterate the paper ids in given data

    Match 5 digit number followed by '(' with atleast one digit
    and completed by ')' from begininig of each words in given
    'data' as paper ids are followed by their credit number.
    Example:- 98768(3) 98767(2)

    Args:
        data: Single line of string having paper ids.

    Return:
        Generator object of (paper_id, paper_credit)
    """
    RE_PAPER_ID = re.compile(r'^(?P<paper_id>\d{5,6})\((?P<paper_credit>\d+)\)')
    for word in data.split():
        match = RE_PAPER_ID.search(word)
        paper_id = match.group('paper_id') if match else None
        paper_credit = match.group('paper_credit') if match else None
        if paper_id:
            yield int(paper_id), int(paper_credit)


def _iter_marks(data):
    """
    Iterate the pair of minor and major marks in given 'data'.

    It extract and group the items in 'data.split()' ignoring 2 items from start.

    Args:
        data: single line of string having minor and major marks detail.

    Return:
        iterable object having pair of minor and major marks.
        NOTE: interger conversion is not performed here hence returned values are
                of type string.
    """

    # Number of items to ignore in data.split() as they contain
    # 'SID:' and sid number
    NUM_WORDS_IGNORE = 2
    DEFAULT_MARKS = None
    data = data.split()[NUM_WORDS_IGNORE:]
    return group_iter(data, 2, DEFAULT_MARKS)


def _iter_total_marks(data):
    """
    Return (total, grade) iterable

    Args:
        data: single line of string having total marks and grade

    Return:
        genrator object of type (total, grade).
    """

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
        # If first element is number then it is marks,
        # if not then it should be grade.
        marks = int(ex_data[0]) if ex_data[0].isdigit() else None
        grade = ex_data[0] if marks == None else (
            ex_data[1] if len(ex_data) > 1 else None)
        if marks or grade:
            yield marks, grade


def _get_subject(data):
    """
    Extract the subject details from given 'data'.

    Args:
        data: single line of string having subject details.

    Return:
        dict having extracted data.
        Example:-
        {'paper_id': 99887, 'paper_code': 'BA109', 'name': 'Maths',
        'credit': 2, 'minor_max': 40, 'major_max': 100,
        'type': sub_type, 'department': exam, 'mode': mode, 'kind': kind}
    """
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
        sub_id = subj_match.group('id')
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
        minor_max = int(minor_max) if minor_max.isdigit() else None
        major_max = int(major_max) if major_max.isdigit() else None

        return {'paper_id': sub_id, 'paper_code': paper_code, 'name': name,
                'credit': credit, 'minor_max': minor_max, 'major_max': major_max,
                'type': sub_type, 'department': exam, 'mode': mode, 'kind': kind}


def has_page_subejcts(pg_data):
    """Check if page contains subjects data.
    """

    RE_IS_SUBJECT_PAGE = re.compile(r"\(.*SCHEME.+OF.+EXAMINATIONS*\)")
    match = RE_IS_SUBJECT_PAGE.search(pg_data)

    return True if match else False


def has_page_results(pg_data):
    """Check if page contains results data.
    """

    RE_IS_RESULTS_PAGE = re.compile(r"RESULT.+TABULATION.+SHEET")
    match = RE_IS_RESULTS_PAGE.search(pg_data)

    return True if match else False


def iter_subjects(raw_data, force=False):
    """Iterate through subjects extracted from page data.

    Retieves the subject data from given page data assuming the
    data to be from pdftotext with -simple flag. If force param is False
    it wont't check for data format.

    Args:
        raw_data: Raw data of a single page.
        force: Whether to raise exception when data does not contain
                subject details.

    Returns:
        A generator object of Subject type.

    Raise:
        DataNotFoundError: When 'force' is True and data does not contain any
                            subject details.
        DataNotSufficientError: When given data does not have minimum requried
                                lines for processing.
    """
    if force and not has_page_subejcts(raw_data):
        raise DataNotFoundError

    raw_data = raw_data.splitlines()

    LINE_SEMESTER = 7  # Semester , Programme Code, Scheme ID
    LINE_SUBJ_START = 11  # Subject Details
    SUBJ_GAP = 1    # Gap btw two consecutive subject lines

    # Check for data length
    if max((LINE_SEMESTER, LINE_SUBJ_START)) + 1 > len(raw_data):
        raise DataNotSufficientError

    semester = _get_semester(raw_data[LINE_SEMESTER])

    for raw in raw_data[LINE_SUBJ_START::SUBJ_GAP+1]:
        subj_details_dict = _get_subject(raw)
        if subj_details_dict:
            subj_details_dict['semester'] = semester
            yield Subject(**subj_details_dict)


def iter_results(raw_data, force=False):
    """Iterate through results extracted from page data.

    Retieves the results data from given page data assuming the
    data to be from pdftotext with -simple flag. If force param is False
    it wont't check for data format.

    Args:
        raw_data: Raw data of a single page.
        force: Whether to raise exception when data does not contain
                result details.

    Returns:
        A generator object of Result type.

    Raise:
        DataNotFoundError: When 'force' is True and data does not contain any
                            result details.
        DataNotSufficientError: When given data does not have minimum requried
                                lines for processing.
    """
    if force and not has_page_results(raw_data):
        raise DataNotFoundError

    raw_data = raw_data.splitlines()

    LINE_SEMESTER_BATCH = 17
    GAP_TOTAL_MARKS = 4
    GAP_MARKS = 2
    GAP_NAME = 1

    # Check for data length
    if LINE_SEMESTER_BATCH + 1 > len(raw_data):
        raise DataNotSufficientError

    # Match whole 11 digits number
    RE_ROLL_NUM = re.compile(r'\b\d{11}\b')

    semester = _get_semester(raw_data[LINE_SEMESTER_BATCH])
    batch = _get_batch(raw_data[LINE_SEMESTER_BATCH])

    for i, line in enumerate(raw_data):
        roll_match = RE_ROLL_NUM.search(line)
        if roll_match:
            # list with subject_ids
            paper_id_credits = list(_iter_paper_id_credits(line))
            # list of (minor, major) marks
            raw_marks = list(_iter_marks(raw_data[i + GAP_MARKS]))
            # list of (total, grade)
            total_and_grades = list(
                _iter_total_marks(raw_data[i + GAP_TOTAL_MARKS]))
            # Name of student
            name = rm_extra_whitespace(raw_data[i + GAP_NAME])

            # Remove line till total marks, to avoid processing them again
            del raw_data[i: GAP_TOTAL_MARKS]

            new_result = Result(roll_match.group(), semester, name, batch)
            for paper_id_credit, mark, total_grade in zip(paper_id_credits, raw_marks, total_and_grades):

                minor = int(mark[0]) if mark[0].isdigit() else None
                major = int(mark[1]) if mark[1].isdigit() else None

                temp_mark = Marks(
                    paper_id_credit[0], minor, major, total_grade[0], total_grade[1], paper_id_credit[1])
                new_result.add_mark(paper_id_credit[0], temp_mark)
            yield new_result
