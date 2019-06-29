
# GGSIPU_result
[![Build Status](https://travis-ci.org/ashutoshvarma/ggsipu_result.svg?branch=master)](https://travis-ci.org/ashutoshvarma/ggsipu_result)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

  

**ggsipu_result** is a A python module for extraction of results from GGSIPU results pdf. It is capable of:-

- Extraction of Results, Subjects details from pdfs.
- Dumping the extracted data in JSON format.


## Examples

```
import ggsipu_result

# If first page have subjects details
page_txt = ggsipu_result.get_page(FILE, 1)

for subject in ggsipu_result.iter_subjects(page_txt):
	print(subject)

  

## PROBABLE OUTPUT
# >> 98101-COMMUNICATION SKILLS - I[HS101]
# >> 99103-CHEMISTRY I[BA103]
# >> 15105-INTRODUCTION TO COMPUTERS[IT105]
# >> 15107-ELECTRICAL SCIENCE[IT107]
```
For more examples please see `Sample_Code` folder


## Tests

`ggsipu_result` includes a test suite built on the unittest framework. All tests are located in the "Tests" folder.
Tests can be run from the command line by:

  
```bash
python -m unittest Tests.tests
```

## License

All files under the repo are licensed under GNU [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)

#### Note:-
I am bit confused. I want to release it under MIT but [xpdf-tools](https://www.xpdfreader.com/opensource.html)  which I use for extracting pdf's text is licensed under GPLv3 or 2. Till I find a replacement for xpdf it will be GPL.

