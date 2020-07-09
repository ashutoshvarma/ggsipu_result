#!/usr/bin/env python

# long_description = """
# A python module for extraction of results from
# GGSIPU results pdf. It is capable of:-
#
# - Extraction of Results, Subjects details from pdfs.
# - Dumping the extracted data in JSON format.
# """

import sys
from os import path

from setuptools import setup


def version():
    import re

    base_dir = path.abspath(path.dirname(sys.argv[0]))
    _VERSION = None
    with open(path.join(base_dir, "ggsipu_result", "__init__.py")) as f:
        _VERSION = re.search(r'__version__\s*=\s*"([^"]+)"', f.read()).group(1)
        assert _VERSION
    return _VERSION


with open(
    path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf8"
) as f:
    readme = f.read()

setup(
    name="ggsipu_result",
    version=version(),
    packages=["ggsipu_result",],
    install_requires=["pyxpdf>=0.2.1",],
    description="GGSIPU Results PDF parser and analyzer",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Ashutosh Varma",
    author_email="ashutoshvarma11@live.com",
    url="https://github.com/ashutoshvarma/ggsipu_result",
    # scripts=[
    #    'tools/dumppdf.py',
    # ],
    keywords=["ggsipu result", "ipu result converter", "cgpa calculator",],
    python_requires=">=3.4",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Text Processing",
    ],
)
