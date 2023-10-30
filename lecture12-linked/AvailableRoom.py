class Room:
    def __init__(self, room_number, room_price, available):
        self.room_number = room_number
        self.room_price = room_price
        self.available = available


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

    def room_available(self):
        current = self.head

        while True:
            if current.value.available == 0:
                print(current.value.room_number, current.value.room_price)

            if current.next is None:
                break

            current = current.next


c = LinkedList()

n = int(input())
for i in range(n):
    room_number, room_price, available = input().split()
    c.add_last(Room(room_number, int(room_price), int(available)))

c.room_available()
