import ggsipu_result

FILE = 'document1.pdf'


for page in ggsipu_result.iter_pages(FILE):
    if ggsipu_result.has_page_results(page):
        for result in ggsipu_result.iter_results(page):
            # All the results where batch is 2018 and atleast one back(fail).
            if result.batch == 2018 and result.get_num_drops() > 0 :
                print(result)
                for m in result.get_mark_drops():
                    print("\t" + str(m))


## Probable Output
# Result: [01016403218]ANSHIKA(2018) Semester: 1
#         [99109] Minor-11, Major-14, Total-25
# Result: [01216403218]ASHISH KUMAR SINGH(2018) Semester: 1
#         [15107] Minor-10, Major-7, Total-17
#         [99109] Minor-3, Major-8, Total-11
#         [99111] Minor-6, Major-19, Total-25
# Result: [01416403218]AVINASH SHARMA(2018) Semester: 1
#         [99109] Minor-5, Major-10, Total-15
# Result: [02716403218]MANENDER(2018) Semester: 1
#         [99109] Minor-13, Major-18, Total-31
# Result: [03116403218]PRAGATI SHARMA(2018) Semester: 1
#         [99109] Minor-10, Major-8, Total-18
# Result: [03416403218]RAJNIS KUMAR(2018) Semester: 1
#         [99109] Minor-6, Major-2, Total-8
#         [99111] Minor-13, Major-10, Total-23
# Result: [04316403218]SUSHANT MAWAR(2018) Semester: 1
#         [99109] Minor-13, Major-20, Total-33
# Result: [40816403218]SAKSHAM ROHILLA(2018) Semester: 1
#         [99109] Minor-7, Major-26, Total-33
# Result: [70116403218]SAURAV SHRIWASTAV(2018) Semester: 1
#         [99109] Minor-8, Major-3, Total-11
# Result: [70216403218]SURAJ SAH(2018) Semester: 1
#         [99109] Minor-6, Major-5, Total-11
# Result: [70316403218]KUNAL GOENKA(2018) Semester: 1
#         [15107] Minor-9, Major-22, Total-31
#         [99109] Minor-7, Major-6, Total-13
#         [15157] Minor-12, Major-20, Total-32
# Result: [70416403218]AKSHAT TYAGI(2018) Semester: 1
#         [99109] Minor-11, Major-22, Total-33
# Result: [70616403218]TENZIN TSECHOK(2018) Semester: 1
#         [15107] Minor-10, Major-19, Total-29
#         [99109] Minor-5, Major-2, Total-7
# Result: [70716403218]RASHINDRA YADAV(2018) Semester: 1
#         [99109] Minor-11, Major-18, Total-29
# Result: [70816403218]SRISHTI JHA(2018) Semester: 1
#         [15105] Minor-8, Major-23, Total-31
#         [99109] Minor-5, Major-6, Total-11