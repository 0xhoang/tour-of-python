import string


class Student:
    def __init__(self, id, math, literature):
        self.id = id
        self.math = math
        self.literature = literature


class SearchStudent:
    def __init__(self, student_list):
        self.student_list = student_list

    def search(self, id):
        for index in range(len(self.student_list)):
            element = self.student_list[index]
            if element.id == id:
                return element

        return None


a, b = map(int, input().split())

student_list = []
list = []

for i in range(a):
    id, math, literature = input().split()
    student = Student(id, float(math), float(literature))
    student_list.append(student)

search_student = SearchStudent(student_list)

for i in range(b):
    item = input()
    rs = search_student.search(item)
    if rs != None:
        list.append(rs)

for i in range(len(list)):
    item = list[i]
    print(item.math, item.literature)
