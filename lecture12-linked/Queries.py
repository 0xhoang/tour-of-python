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

    def remove(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next

    def print(self):
        current = self.head
        while True:
            print(current.value, end=' ')
            if current.next is None:
                break

            current = current.next


c = LinkedList()
n = int(input())
for i in range(n):
    item = list(map(int, input().split()))
    if item[0] == 0:
        c.remove()
    elif item[0] == 1:
        c.add_last(item[1])

c.print()
