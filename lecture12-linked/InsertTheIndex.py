class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def add_after(self):
        current = self.head
        i = 2

        while current.next is not None:
            p = Node(i)
            p.next = current.next
            current.next = p
            current = p.next
            i = i + 1

    def print(self):
        current = self.head
        while True:
            print(current.value, end=' ')

            if current.next is None:
                break

            current = current.next


c = LinkedList()
list = []
while True:
    line = int(input())
    if line == 0:
        break

    c.add_last(line)
    list.append(line)

current = c.head
if current.next is None:
    c.add(1)
else:
    c.add_after()
    c.add(1)

c.print()
