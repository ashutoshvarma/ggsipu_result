# GGSIPU_result
[![Build Status](https://travis-ci.com/ashutoshvarma/ggsipu_result.svg?branch=master)](https://travis-ci.com/ashutoshvarma/ggsipu_result)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


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


## Tests

`ggsipu_result` includes a test suite built on the unittest framework. All tests are located in the "Tests" folder.
Tests can be run from the command line by:

  
```bash
python -m unittest Tests.tests
```

## License

All files under the repo are licensed under GNU [GPLv3](https://github.com/ashutoshvarma/ggsipu_result/blob/master/LICENSE)


