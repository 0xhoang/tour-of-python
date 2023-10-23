n = int(input())

class Student:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def average(self):
        return (self.a + self.b) / 2


total = 0
for i in range(n):
    name = input()
    a, b = map(float, input().split())

    c = Student(name, a, b)
    gpa = c.average()

    if gpa >= 9:
        max = gpa
        total += 1

print(total)
