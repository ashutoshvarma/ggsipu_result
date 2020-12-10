"""
Cumulative GPA for Two Semester

Calculate combine cgpa for Two Semester and
print the pretty formated output and also dumps
data in csv format.
"""
from ggsipu_result import parse_result_pdf
import random
import csv

BATCH = 2018
RESULT_FILES = {
    1: "/mnt/e/av136/Downloads/results/SEM1.pdf",
    2: "/mnt/e/av136/Downloads/results/SEM2.pdf",
    3: "/mnt/e/av136/Downloads/results/SEM3.pdf",
    4: "/mnt/e/av136/Downloads/results/SEM4.pdf",
}

all_results = {
    sem: {
        i.roll_num: i
        for i in [
            r for r in parse_result_pdf(pdf)[1] if r.semester == sem and r.batch == 2018
        ]
    }
    for sem, pdf in RESULT_FILES.items()
}

for sem, res in all_results.items():
    print(f"Sem {sem} students - {len(res)}")
print()


def _sem_credits(sem_results):
    sample = random.sample(sem_results, 2)
    cred1 = sum(m.paper_credit for m in sample[0].get_marks(include_none=True))
    cred2 = sum(m.paper_credit for m in sample[1].get_marks(include_none=True))
    # for sanity check
    assert cred1 == cred2
    return cred1


compiled_list = []
for roll_num, res in list(all_results.values())[0].items():
    cum_cgpa = None
    sem_credits = {
        sem: _sem_credits(list(res.values())) for sem, res in all_results.items()
    }
    total_grade = 0.0
    # make sure student has appeared in all semesters
    missing = False
    for sem, results in all_results.items():
        if not results.get(roll_num):
            missing = True
            print(
                f"Student {res.student_name} [{res.roll_num}] not found in Semester {sem} PDF."
            )
            continue
        total_grade += results[roll_num].cgpa * sem_credits[sem]

    if not missing:
        res.combine_gpa = round(total_grade / sum(sem_credits.values()), 2)
        compiled_list.append(res)

print()

compiled_list.sort(key=lambda x: x.combine_gpa, reverse=True)
with open("compile.csv", "w") as csv_file:
    filednames = [
        "S.No.",
        "Roll Number",
        "Name",
        "Batch",
        f"CGPA (Sem {'+'.join(str(k) for k in all_results.keys())})",
    ]
    csv_writer = csv.writer(
        csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    csv_writer.writerow(filednames)

    for i, r in enumerate(compiled_list):
        out_str = f"{i+1:2}. [{r.roll_num}] {r.student_name}({r.batch}) [CGPA (Sem {'+'.join(str(k) for k in all_results.keys())}): {r.combine_gpa}]"
        print(out_str)
        csv_writer.writerow([i + 1, r.roll_num, r.student_name, r.batch, r.combine_gpa])
