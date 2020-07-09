import ggsipu_result

FILE = "document1.pdf"

with open("subj_dump.json", "a") as fs, open("res_dump.json", "a") as fr:
    for page in ggsipu_result.iter_pages(FILE):
        if ggsipu_result.has_page_results(page):
            results = list(ggsipu_result.iter_results(page))
            fr.write(ggsipu_result.toJSON(results))
        elif ggsipu_result.has_page_subjects(page):
            subjects = list(ggsipu_result.iter_subjects(page))
            fs.write(ggsipu_result.toJSON(subjects))
