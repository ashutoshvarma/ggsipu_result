import itertools
import json


class JSONSerializable:
    def toJSON(self, indent=4):
        return toJSON(self, indent)


def toJSON(self, indent=4):
    """Convert to json, for custom classes it jsonize their attribute dict(__dict__)."""
    return json.dumps(
        self,
        default=lambda o: o.__dict__
        if hasattr(o, "__dict__")
        else "<not serializable>",
        sort_keys=True,
        indent=indent,
    )


def toDict(obj):
    return json.loads(toJSON(obj))


def rm_extra_whitespace(string):
    """
    Remove Extra white space from 'string'.
    EXAMPLE:- "  aa    bb  cc" -> ""aa bb cc"
    """
    string = string.strip()
    while "  " in string:
        string = string.replace("  ", " ")
    return string


def group_iter(it, n, fillvalue):
    """
    group_iter([0,3,4,10,2,3], 2, None) => iterator

    Group an iterable into an n-tuples iterable and pad the final
    group with a fill value
    """
    return itertools.zip_longest(*[iter(it)] * n, fillvalue=fillvalue)
