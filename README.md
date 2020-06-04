# ggsipu_result
[![Travis (.com)](https://img.shields.io/travis/com/ashutoshvarma/ggsipu_result?style=for-the-badge)](https://travis-ci.com/github/ashutoshvarma/ggsipu_result/)
[![GitHub license](https://img.shields.io/github/license/ashutoshvarma/ggsipu_result?style=for-the-badge)](https://github.com/ashutoshvarma/ggsipu_result/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/ggsipu_result?color=blue&style=for-the-badge)](https://pypi.org/project/ggsipu-result/)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ggsipu_result?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ggsipu_result?style=for-the-badge)

**ggsipu_result** is a A python module for extraction of results from GGSIPU results pdf. It is capable of:-

- Extraction of Results, Subjects details from pdfs.
- Dumping the extracted data in JSON format.


## Examples
Given code prints top 5 students of 2018 batch:-
```python
from ggsipu_result import iter_pages, has_page_results, iter_results

FILE="Resources/CSE_Result.pdf"

results = []
for page in iter_pages(FILE):
    if has_page_results(page):
        results = results + [r for r in iter_results(page) if r.batch == 2018]

results.sort(key=lambda x: x.cgpa, reverse=True)

for i, result in enumerate(results[:5]):
    print("{i}. {r}".format(i=i+1, r= result))


## PROBABLE OUTPUT
# 1. Result(Sem 1): [41516403218]GAURAV JAIN(2018) [CGPA: 8.92]
# 2. Result(Sem 1): [41016403218]VARDAAN GROVER(2018) [CGPA: 8.77]
# 3. Result(Sem 1): [40316403218]UJJWAL NEGI(2018) [CGPA: 8.73]
# 4. Result(Sem 1): [40116403218]RIGVED ALANKAR(2018) [CGPA: 8.5]
# 5. Result(Sem 1): [01616403218]CHAITANYA GIRI(2018) [CGPA: 8.46]
```
For more examples please see `Sample_Code` folder

## Install
```
pip install ggsipu-result
```

## Tests

`ggsipu_result` includes a test suite built on the unittest framework. All tests are located in the "Tests" folder.
Tests can be run from the command line by:


```bash
python -m unittest Tests.tests
```

## Changelog
### v0.1.1 (05-06-2020)
- fix [#1](https://github.com/ashutoshvarma/ggsipu_result/issues/1): include support for 6 digit paper codes
### v0.1 (initial release)

## License

All files under the repo are licensed under GNU [GPLv3](https://github.com/ashutoshvarma/ggsipu_result/blob/master/LICENSE)


