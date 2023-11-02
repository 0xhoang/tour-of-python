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

    def create_note(self, x, y, n):
        total = n - 2
        self.add_last(x)
        self.add_last(y)

        while total > 0:
            new_node = y + x

            new_node = new_node % 1000007

            self.add_last(new_node)

            x = y
            y = new_node

            total -= 1

    def print(self):
        current = self.head
        while True:
            print(current.value, end=' ')

            if current.next is None:
                break

            current = current.next


c = LinkedList()

x, y, n = map(int, input().split())

c.create_note(
    x,
    y,
    n
)

c.print()
