from ggsipu_result import iter_pages, iter_results, has_page_results

FILE = "document1.pdf"

cgpa = []

for page in iter_pages(FILE):
    if has_page_results(page):
        for res in iter_results(page):
            # Filtered for specific batch
            if res.batch == 2018:
                cgpa.append(res.cgpa)

avg_cgpa = sum(i for i in cgpa) / len(cgpa)
print(avg_cgpa)
