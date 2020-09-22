from pyxpdf import xpdf

from .data_process import (
    DataNotFoundError,
    DataNotSufficientError,
    DataProcessingError,
    has_page_results,
    has_page_subjects,
    iter_results,
    iter_subjects,
    parse_result_pdf,
)
from .objects import Marks, Result, Subject
from .util import toDict, toJSON

__version__ = "0.3.3"

__all__ = [
    "DataNotFoundError",
    "DataNotSufficientError",
    "DataProcessingError",
    "has_page_results",
    "has_page_subjects",
    "iter_results",
    "iter_subjects",
    "parse_result_pdf",
    # Objects
    "Marks",
    "Result",
    "Subject",
    # util functions
    "toDict",
    "toJSON",
]


def iter_pages(pdf, start=0, end=0):
    doc = xpdf.Document(pdf)

    if start < 0 or start >= len(doc):
        start = 0
    if end <= 0 or end >= len(doc):
        end = len(doc) - 1

    for p in doc[start:end]:
        yield p.text(control=xpdf.TextControl(mode="simple"))
