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

    def calculate_new_node(self, n, list):
        self.add_last(list[0])

        i = 1
        while i < n:
            new_node = list[i - 1] + list[i]
            self.add_last(new_node)
            i += 1

    def print(self):
        current = self.head
        while True:
            print(current.value, end=' ')

            if current.next is None:
                break

            current = current.next


n = int(input())
list = list(map(int, input().split()))

c = LinkedList()
c.calculate_new_node(n, list)
c.print()
