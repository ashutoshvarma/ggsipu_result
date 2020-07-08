import os
import sys

import ggsipu_result

# Configure path environment
TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
SOURCE_ROOT = os.path.dirname(TESTS_ROOT)
PROJECT_ROOT = os.path.dirname(SOURCE_ROOT)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, "Resources")

# Append project dir to PATH
sys.path.append(PROJECT_ROOT)


class TestDataProcess:
    subject_data_file = os.path.join(RESOURCE_ROOT, "CSE_Result", "1.txt")
    result_data_file = os.path.join(RESOURCE_ROOT, "CSE_Result", "58.txt")

    subject_file = os.path.join(RESOURCE_ROOT, "subjects.json")
    result_file = os.path.join(RESOURCE_ROOT, "results.json")

    def test_has_page_subjects(self):
        # Load data file
        with open(self.subject_data_file, "r") as inputfile:
            assert ggsipu_result.has_page_subejcts(inputfile.read()) is True

    def test_has_page_results(self):
        # Load data file
        with open(self.result_data_file, "r") as inputfile:
            assert ggsipu_result.has_page_results(inputfile.read()) is True

    def test_iter_subjects(self):
        with open(self.subject_data_file, "r") as inputfile, open(
            self.subject_file, "r"
        ) as dumpf:
            subjects = list(ggsipu_result.iter_subjects(inputfile.read()))
            json_dump = ggsipu_result.toJSON(subjects)
            assert json_dump == dumpf.read()

    def test_iter_results(self):
        with open(self.result_data_file, "r") as inputfile, open(
            self.result_file, "r"
        ) as dumpf:
            results = list(ggsipu_result.iter_results(inputfile.read()))
            json_dump = ggsipu_result.toJSON(results)
            assert json_dump == dumpf.read()
