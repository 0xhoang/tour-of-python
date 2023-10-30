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

    def ending5(self, value):
        ending = value % 10
        if ending == 5:
            return True

        return False

    def print(self):
        current = self.head
        while True:
            if self.ending5(current.value) is not True:
                print(current.value, end=' ')

            if current.next is None:
                break

            current = current.next


c = LinkedList()

n = int(input())
for i in range(n):
    line = int(input())
    c.add_last(line)

c.print()
