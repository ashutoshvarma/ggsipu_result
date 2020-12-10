from ggsipu_result import iter_pages, has_page_results, iter_results

FILE = "document1.pdf"


for page in iter_pages(FILE):
    if has_page_results(page):
        for result in iter_results(page):
            # All the results where batch is 2018 and atleast one back(fail).
            if result.batch == 2018 and result.num_drops > 0:
                print(result)
                for m in result.get_mark_drops(ignore_None=True):
                    print("\t" + str(m))

## Probable Output
# Result(Sem 1): [01016403218]ANSHIKA(2018) [CGPA: 5.69]
#         [99109](4) Minor-11, Major-14, Total-25
# Result(Sem 1): [01216403218]ASHISH KUMAR SINGH(2018) [CGPA: 3.64]
#         [15107](4) Minor-10, Major-7, Total-17
#         [99109](4) Minor-3, Major-8, Total-11
#         [99111](3) Minor-6, Major-19, Total-25
#         [98119](1) Minor-None, Major-0, Total-0
# Result(Sem 1): [01416403218]AVINASH SHARMA(2018) [CGPA: 5.12]
#         [99109](4) Minor-5, Major-10, Total-15
# Result(Sem 1): [02716403218]MANENDER(2018) [CGPA: 6.65]
#         [99109](4) Minor-13, Major-18, Total-31
#         [99111](3) Minor-17, Major-None, Total-None
# Result(Sem 1): [03116403218]PRAGATI SHARMA(2018) [CGPA: 6.08]
#         [99109](4) Minor-10, Major-8, Total-18
# Result(Sem 1): [03416403218]RAJNIS KUMAR(2018) [CGPA: 4.92]
#         [99109](4) Minor-6, Major-2, Total-8
#         [99111](3) Minor-13, Major-10, Total-23
# Result(Sem 1): [04316403218]SUSHANT MAWAR(2018) [CGPA: 6.69]
#         [99109](4) Minor-13, Major-20, Total-33
# Result(Sem 1): [40816403218]SAKSHAM ROHILLA(2018) [CGPA: 6.12]
#         [99109](4) Minor-7, Major-26, Total-33
# Result(Sem 1): [70116403218]SAURAV SHRIWASTAV(2018) [CGPA: 5.58]
#         [99109](4) Minor-8, Major-3, Total-11
# Result(Sem 1): [70216403218]SURAJ SAH(2018) [CGPA: 6.08]
#         [99109](4) Minor-6, Major-5, Total-11
# Result(Sem 1): [70316403218]KUNAL GOENKA(2018) [CGPA: 4.58]
#         [15107](4) Minor-9, Major-22, Total-31
#         [99109](4) Minor-7, Major-6, Total-13
#         [15157](1) Minor-12, Major-20, Total-32
# Result(Sem 1): [70416403218]AKSHAT TYAGI(2018) [CGPA: 5.27]
#         [99109](4) Minor-11, Major-22, Total-33
# Result(Sem 1): [70616403218]TENZIN TSECHOK(2018) [CGPA: 4.52]
#         [15107](4) Minor-10, Major-19, Total-29
#         [99109](4) Minor-5, Major-2, Total-7
#         [98119](1) Minor-None, Major-0, Total-0
# Result(Sem 1): [70716403218]RASHINDRA YADAV(2018) [CGPA: 5.81]
#         [99109](4) Minor-11, Major-18, Total-29
# Result(Sem 1): [70816403218]SRISHTI JHA(2018) [CGPA: 4.96]
#         [15105](3) Minor-8, Major-23, Total-31
#         [99109](4) Minor-5, Major-6, Total-11
