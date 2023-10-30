class DateTime:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def isGreatestDate(self):
        current = self.head

        max_year = current.value.year
        max_month = current.value.month
        max_day = current.value.day

        while True:
            if max_year < current.value.year:
                max_year = current.value.year
                max_month = current.value.month
                max_day = current.value.day

            elif max_year == current.value.year:
                if max_month < current.value.month:
                    max_month = current.value.month
                    max_day = current.value.day
                elif max_month == current.value.month:
                    if max_day < current.value.day:
                        max_day = current.value.day

            if current.next is None:
                break

            current = current.next

        print(max_day, max_month, max_year)


c = LinkedList()

n = int(input())
for i in range(n):
    day, month, year = map(int, input().split())
    date = DateTime(day, month, year)
    c.add_last(date)

c.isGreatestDate()
