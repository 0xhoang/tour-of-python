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

    def isPalindromeNumber(self, value):
        list = []
        n = value

        while n > 0:
            temp = n % 10
            list.append(temp)
            n = n // 10

        length = len(list)
        part = length // 2

        for i in range(part):
            if list[i] != list[length - 1 - i]:
                return False

        return True

    def printIndex(self):
        current = self.head

        i = 0
        while True:
            if self.isPalindromeNumber(current.value):
                print(i, end=' ')

            i += 1
            if current.next is None:
                break

            current = current.next


c = LinkedList()

while True:
    n = float(input())
    if n == -1:
        break

    c.add_last(n)

c.printIndex()
