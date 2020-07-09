from common_imports import file_in_resource_dir

import ggsipu_result


class TestDataProcess:
    subject_data_file = file_in_resource_dir("CSE_Result", "1.txt")
    result_data_file = file_in_resource_dir("CSE_Result", "58.txt")

    subject_file = file_in_resource_dir("subjects.json")
    result_file = file_in_resource_dir("results.json")

    def test_has_page_subjects(self):
        # Load data file
        with open(self.subject_data_file, "r") as inputfile:
            assert ggsipu_result.has_page_subjects(inputfile.read()) is True

    def test_has_page_results(self):
        # Load data file
        with open(self.result_data_file, "r") as inputfile:
            assert ggsipu_result.has_page_results(inputfile.read()) is True

    def test_iter_subjects(self):
        with open(self.subject_data_file, "r") as inputfile, open(
            self.subject_file, "r"
        ) as dump_f:
            subjects = list(ggsipu_result.iter_subjects(inputfile.read()))
            json_dump = ggsipu_result.toJSON(subjects)
            assert json_dump == dump_f.read()

    def test_iter_results(self):
        with open(self.result_data_file, "r") as inputfile, open(
            self.result_file, "r"
        ) as dump_f:
            results = list(ggsipu_result.iter_results(inputfile.read()))
            json_dump = ggsipu_result.toJSON(results)
            assert json_dump == dump_f.read()
