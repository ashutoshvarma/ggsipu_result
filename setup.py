#!/usr/bin/env python

#long_description = """
#A python module for extraction of results from
#GGSIPU results pdf. It is capable of:-
#
#- Extraction of Results, Subjects details from pdfs.
#- Dumping the extracted data in JSON format.
#"""


from setuptools import setup
from os import path

# bump ggsipu_result/__init__.py version as well.
VERSION = "0.1.1"

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding="utf8") as f:
    readme = f.read()

setup(
    name='ggsipu_result',
    version=VERSION,
    packages=['ggsipu_result'],
    install_requires=[
        'pyxpdf==0.1.1',
    ],
    description='GGSIPU Results PDF parser and analyzer',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Ashutosh Varma',
    author_email='ashutoshvarma11@live.com',
    url='https://github.com/ashutoshvarma/ggsipu_result',
    #scripts=[
    #    'tools/dumppdf.py',
    #],
    keywords=[
        'ggsipu result',
        'ipu result converter',
        'cgpa calculator',
    ],
    python_requires='>=3.4',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Text Processing',
    ],
)
