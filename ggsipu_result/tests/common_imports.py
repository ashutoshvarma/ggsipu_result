import os

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
SOURCE_ROOT = os.path.dirname(TESTS_ROOT)
PROJECT_ROOT = os.path.dirname(SOURCE_ROOT)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, "Resources")


def file_in_resource_dir(*args):
    return os.path.join(RESOURCE_ROOT, *args)
