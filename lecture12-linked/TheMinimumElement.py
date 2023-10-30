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

    def add_after(self, x, y):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            if current.value == x:
                new_node = Node(y)
                new_node.next = current.next
                current.next = new_node
                return

            current = current.next

    def remove(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = None
        self.tail = current

    def remove_after(self, x, y):
        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            if current.value == x and current.next.value == y:
                current.next = current.next.next
                return

            current = current.next


linked = LinkedList()
while True:
    n = int(input())
    if n == 0:
        break
    linked.add_last(n)

current = linked.head
min = current.value

while True:
    if current.value < min:
        min = current.value

    if current.next is None:
        break

    current = current.next

print(min)
