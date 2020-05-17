import os
import sys
import json
import unittest

import ggsipu_result

# Configure path environment
TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(TESTS_ROOT)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, 'Resources')

# Append project dir to PATH
sys.path.append(PROJECT_ROOT)


class data_process_TestCases(unittest.TestCase):

    subject_data_file = os.path.join(RESOURCE_ROOT, 'CSE_Result', '1.txt')
    result_data_file = os.path.join(RESOURCE_ROOT, 'CSE_Result', '58.txt')

    subject_file = os.path.join(RESOURCE_ROOT, 'subjects.json')
    result_file = os.path.join(RESOURCE_ROOT, 'results.json')

    def setUp(self):
        # To incorporate large asserEquals calls
        self.maxDiff = None

    def test_has_page_subjects(self):
        # Load data file
        with open(self.subject_data_file, 'r') as inputfile:
            self.assertTrue(ggsipu_result.has_page_subejcts(inputfile.read()))

    def test_has_page_results(self):
        # Load data file
        with open(self.result_data_file, 'r') as inputfile:
            self.assertTrue(ggsipu_result.has_page_results(inputfile.read()))

    def test_iter_subjects(self):
        with open(self.subject_data_file, 'r') as inputfile, open(self.subject_file, 'r') as dumpf:
            subjects = list(ggsipu_result.iter_subjects(inputfile.read()))
            json_dump = ggsipu_result.toJSON(subjects)
            self.assertEqual(json_dump, dumpf.read())

    def test_iter_results(self):
        with open(self.result_data_file, 'r') as inputfile, open(self.result_file, 'r') as dumpf:
            results = list(ggsipu_result.iter_results(inputfile.read()))
            json_dump = ggsipu_result.toJSON(results)
            self.assertEqual(json_dump, dumpf.read())


