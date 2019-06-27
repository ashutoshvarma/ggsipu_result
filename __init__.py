from .data_process import (
    iter_results, iter_subjects, has_page_results,
    has_page_subejcts, DataNotFoundError, DataNotSufficientError,
    DataProcessingError
)

from .objects import Subject, Result, Student, Marks

from .util import toJSON

from .pdftotext import convert, iter_pages, get_page

from ._version import __version__
