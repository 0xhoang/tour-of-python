class Student:
    def __init__(self, code, score):
        self.code = code
        self.score = score


def insert_sort_desc(list_student, n):
    j = n
    while j > 0 and list_student[j - 1].score <= list_student[j].score:
        if list_student[j - 1].score == list_student[j].score:
            if list_student[j - 1].code > list_student[j].code:
                list_student[j], list_student[j - 1] = list_student[j - 1], list_student[j]
        else:
            list_student[j], list_student[j - 1] = list_student[j - 1], list_student[j]

        j -= 1

    return list_student


def sort(list_student):
    # insert sort
    for i in range(len(list_student)):
        insert_sort_desc(list_student, i)

    return list_student


n, y = map(int, input().split())

list_student = []
for i in range(n):
    code, score = input().split()
    list_student.append(Student(int(code), float(score)))

list_student_sort = sort(list_student)

for i in range(y):
    print(list_student_sort[i].code)
