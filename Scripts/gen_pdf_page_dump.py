from ggsipu_result import iter_pages
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, "Resources")

FILE = os.path.join(RESOURCE_ROOT, "CSE_Result.pdf")


for i, page in enumerate(iter_pages(FILE)):
    with open(os.path.join(RESOURCE_ROOT, "CSE_Result" ,str(i+1) + ".txt"), 'w+') as f:
        f.write(page)
