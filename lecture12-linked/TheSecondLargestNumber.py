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

    def findSecondLagestNumber(self):
        if self.head is None:
            return -1

        if self.head == self.tail:
            return -1

        current = self.head
        largest = current.value
        largestSecond = current.value

        while True:
            if largest < current.value:
                largestSecond = largest
                largest = current.value
            elif largestSecond < current.value:
                largestSecond = current.value

            if current.next is None:
                break

            current = current.next

        if largest == largestSecond:
            return -1

        return largestSecond


c = LinkedList()

while True:
    n = float(input())
    if n == -1:
        break

    c.add_last(n)

print(c.findSecondLagestNumber())
