#!/usr/bin/env python

from distutils.core import setup
import re

long_description = """
A python module for extraction of results from
GGSIPU results pdf. It is capable of:-

- Extraction of Results, Subjects details from pdfs.
- Dumping the extracted data in JSON format.
"""

VERSIONFILE="ggsipu_result/_version.py"
verstrline = open(VERSIONFILE, "r").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

setup(
        name="ggsipu_result",
        version=verstr,
        description="GGSIPU Result Extraction",
        long_description=long_description,
        author="Ashutosh Varma",
        author_email="ashutoshvarma11@live.com",
        maintainer="Ashutosh Varma",
        maintainer_email="ashutoshvarma11@live.com",
        url="https://github.com/ashutoshvarma/ggsipu_result",
        classifiers = [
            "Development Status :: 0 - InActive Development",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Operating System :: Windows OR UNIX",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        packages=["ggsipu_result"],
    )
