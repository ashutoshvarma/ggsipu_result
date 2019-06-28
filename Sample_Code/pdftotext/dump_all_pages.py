from ggsipu_result import iter_pages


FILE = 'document1.pdf'

for i, page in enumerate(iter_pages(FILE)):
    with open(str(i+1) + ".txt") as f:
        f.write(page)
