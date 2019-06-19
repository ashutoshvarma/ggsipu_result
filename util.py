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
    group_iter([0,3,4,10,2,3], 2) => iterator

    Group an iterable into an n-tuples iterable and pad the final
    group with a fill value

    >>> list(group(range(10), 3, x))
    [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, x, x)]
    """
    return itertools.zip_longest(*[iter(it)]*n, fillvalue=fillvalue)
