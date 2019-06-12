from objects import Student, Marks, Result, Subject
import re

def rm_extra_whitespace(string):
    """
    Remove Extra white space from 'string'.
    EXAMPLE:- "  aa    bb  cc" -> ""aa bb cc"
    """
    string = string.strip()
    while '  ' in string:
        string = string.replace('  ', ' ')
    return string


def extract_subjects(raw_data):
    raw_data = raw_data.splitlines()

    # Compiled Regex
    # Capture Date of format dd/mm/yyy
    RE_DATE = re.compile(r"\d{2}/\d{2}/\d{4}")

    RE_COLON_NUM = re.compile(r"""
                        (?::\s*0*)  #Match : followed by spaces and 0s (Non-Matching Group)
                        (\d+)       # Match digits 
                        """, re.VERBOSE)

    # RE_BTW_PARANTHESES = re.compile(r"""
    #                     \(          #Match Opening Parantheses
    #                     ([^)]+)     #Match characters except ')' one or more (Capturing Group)
    #                     \)          #Match Closing Parantheses
    #                     """, re.VERBOSE)

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

    # CONSTANTS
    LINE_PRE_DATE = 2  # Prepared Date
    LINE_DEC_DATE = 4  # Declared Date
    LINE_SEMESTER = 10  # Semester , Programme Code, Scheme ID

    LINE_SUBJ_START = 16  # Subject Details
    SUBJ_GAP = 1    # Gap btw two consecutive subject lines

    # Prepared Date
    prepared_date = RE_DATE.search(raw_data[LINE_PRE_DATE]).group()

    # Declared Date
    declared_date = RE_DATE.search(raw_data[LINE_DEC_DATE]).group()

    # Semester, Programme Code, Scheme ID
    programme_code, scheme_id, semester = RE_COLON_NUM.findall(
        raw_data[LINE_SEMESTER])

    for raw in raw_data[LINE_SUBJ_START::SUBJ_GAP+1]:
        subj_match = RE_SUBJ_DETAILS.search(raw)
        if subj_match:
            new_subj = Subject(subj_match.group('id'), subj_match.group('paper_code'),
                               rm_extra_whitespace(subj_match.group(
                                   'name')), subj_match.group('credit'),
                               subj_match.group(
                                   'minor_max'), subj_match.group('major_max'),
                               subj_match.group(
                                   'type'), subj_match.group('exam'),
                               subj_match.group(
                                   'mode'), subj_match.group('kind'),
                               semester=semester)
            yield new_subj


def extract_student_marks(raw_data):
    raw_data = raw_data.splitlines()

    LINE_SEMESTER_BATCH = 24
    GAP_TOTAL_MARKS = 8

    RE_ROLL_NUM = re.compile(r'\b\d{11}\b')
    RE_PAPER_ID = re.compile(r'^\d{5}(?=\()')
    RE_SEMESTER = re.compile(r'(?:Sem\D*:\s*0*)(\d+)')
    RE_BATCH = re.compile(r'(?:Batch\D*:\s*0*)(\d+)')
    RE_TOTAL_MARKS = re.compile(r"""
                                (?P<total>\b\d{2}\b)(?=\()
                                \(
                                (?P<grade>[^)]+)
                                """, re.VERBOSE)

    # Get the semester
    semester = None
    sem_match = RE_SEMESTER.search(raw_data[LINE_SEMESTER_BATCH])
    if sem_match:
        semester = sem_match.group(1)

    batch = None
    sem_match = RE_BATCH.search(raw_data[LINE_SEMESTER_BATCH])
    if sem_match:
        batch = sem_match.group(1)

    buffer_data = []

    for i, line in enumerate(raw_data):
        roll_match = RE_ROLL_NUM.search(line)
        if roll_match:
            paper_ids = []
            for words in line.split():
                paper_id = RE_PAPER_ID.match(words).group() \
                    if RE_PAPER_ID.match(words) else None
                if paper_id:
                    paper_ids.append(paper_id)

            buffer_data.append(
                (i, Student(roll_match.group(), batch_year=batch), paper_ids))

    for line_no, student, subject_ids in buffer_data:

        new_result = Result(semester, [])

        student.name = rm_extra_whitespace(raw_data[line_no + 2])
        raw_marks = raw_data[line_no + 4].split()[2:]

        iterate = iter(raw_marks)
        for i, minor in enumerate(iterate):
            minor = minor if minor.isdigit() else None

            major = next(iterate)
            major = major if major.isdigit() else None

            new_marks = Marks(subject_ids[i], minor, major, None)
            new_result.marks.append(new_marks)

        match_iter = RE_TOTAL_MARKS.finditer(
            raw_data[line_no + GAP_TOTAL_MARKS])
        for mrks, mtch in zip(new_result.marks, match_iter):
            total = mtch.group('total')
            grade = mtch.group('grade')
            mrks.total = total
            mrks.grade = grade

        student.results.append(new_result)
        yield student
