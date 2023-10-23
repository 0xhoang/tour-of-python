n = int(input())


class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class OldestEmployee:
    def __init__(self):
        self.oldest = None

    def add(self, employee):
        if self.oldest is None:
            self.oldest = employee
        elif self.oldest.age > employee.age:
            self.oldest = employee
        elif self.oldest.age == employee.age and self.oldest.id > employee.id:
            self.oldest = employee

    def get(self):
        return self.oldest


oldest = OldestEmployee()
for i in range(n):
    id, name, age = input().split()
    employee = Employee(id, name, int(age))
    oldest.add(employee)

print(oldest.get().id, oldest.get().name, oldest.get().age)
