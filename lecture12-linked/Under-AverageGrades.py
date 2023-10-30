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


c = LinkedList()
while True:
    line = float(input())
    if line == -1:
        break

    c.add_last(line)

current = c.head
while True:
    if current.value < 5:
        print(current.value)

    if current.next is None:
        break

    current = current.next
