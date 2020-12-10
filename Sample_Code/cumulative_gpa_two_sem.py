"""
Cumulative GPA for Two Semester

Calculate combine cgpa for Two Semester and
print the pretty formated output and also dumps
data in csv format.
"""
import csv
from ggsipu_result import iter_pages, has_page_results, iter_results

# Sem1 result file
SEM1_PDF = "Resources/CSE_Result.pdf"
# Total Credits in Sem1, you can calculate it using
# ggsipu_result but for sake of simpliness hardcoding
# it here.
SEM1_CRE = 26

SEM2_PDF = "/home/varma/Downloads/SEM2.pdf"
SEM2_CRE = 28


def get_2018_result(pdf):
    results = {}
    for page in iter_pages(pdf):
        if has_page_results(page):
            results.update(
                {r.roll_num: r for r in iter_results(page) if r.batch == 2018}
            )
    return results


sem1_res = get_2018_result(SEM1_PDF)
sem2_res = get_2018_result(SEM2_PDF)

print(f"Semester 1, Students - {len(sem1_res)}")
print(f"Semester 2, Students - {len(sem2_res)}")
print()

compile_list = []
for roll, sem1 in sem1_res.items():
    sem2 = sem2_res.get(roll)
    if not sem2:
        print(
            f"Student {sem1.student_name} [{sem1.roll_num}] not found in Semester 2 records."
        )
        continue
    total_grade = sem1.cgpa * SEM1_CRE + sem2.cgpa * SEM2_CRE
    total_credit = SEM1_CRE + SEM2_CRE
    cgpa = round(total_grade / total_credit, 2)
    sem1.combine_gpa = cgpa

    compile_list.append(sem1)

print()

compile_list.sort(key=lambda x: x.combine_gpa, reverse=True)
with open("compile.csv", "w") as csv_file:
    filednames = ["S.No.", "Roll Number", "Name", "Batch", "CGPA (Sem 1+2)"]
    csv_writer = csv.writer(
        csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    csv_writer.writerow(filednames)

    for i, r in enumerate(compile_list):
        out_str = f"{i+1:2}. Result(Sem 1+2): [{r.roll_num}] {r.student_name}({r.batch}) [CGPA: {r.combine_gpa}]"
        print(out_str)
        csv_writer.writerow([i + 1, r.roll_num, r.student_name, r.batch, r.combine_gpa])
