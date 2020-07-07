from pyxpdf import xpdf

from .data_process import (
    iter_results, iter_subjects, has_page_results, has_page_subejcts,
    parse_result_pdf, DataNotFoundError, DataNotSufficientError,
    DataProcessingError
)

from .objects import Subject, Result, Marks
from .util import toJSON

__version__ = "0.3"


def iter_pages(pdf, start=0, end=0):
    doc = xpdf.Document(pdf)

    if start < 0 or start >= len(doc):
        start = 0
    if end <= 0 or end >= len(doc):
        end = len(doc) - 1

    for p in doc[start:end]:
        yield p.text(control=xpdf.TextControl(mode="simple"))
