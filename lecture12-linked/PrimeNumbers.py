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

    def isPrime(self, value):
        if value < 2:
            return False

        for i in range(2, value):
            if value % i == 0:
                return False

        return True

    def countPrime(self):
        count = 0
        current = self.head

        while True:
            if self.isPrime(current.value):
                count += 1

            if current.next is None:
                break

            current = current.next

        return count


c = LinkedList()
while True:
    line = int(input())
    if line == -1:
        break
    c.add_last(line)

print(c.countPrime())
