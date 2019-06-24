import itertools


def rm_extra_whitespace(string):
    """
    Remove Extra white space from 'string'.
    EXAMPLE:- "  aa    bb  cc" -> ""aa bb cc"
    """
    string = string.strip()
    while '  ' in string:
        string = string.replace('  ', ' ')
    return string


def group_iter(it, n, fillvalue):
    """
    group_iter([0,3,4,10,2,3], 2, None) => iterator

    Group an iterable into an n-tuples iterable and pad the final
    group with a fill value
    """
    return itertools.zip_longest(*[iter(it)]*n, fillvalue=fillvalue)


def count_pdf_pages(file):
    """
    Returns total pages in pdf file.
    NOTE: Not reliable as implementaion is very basic
    """
    #TODO: Cover other cases and tests
    with open(file, 'r', encoding="latin-1") as fr:
        dump = fr.read()
        return dump.count("/Contents")
