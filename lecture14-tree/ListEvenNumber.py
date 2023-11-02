import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def addToRoot(self, new_node):
        if new_node.val < self.val:
            if self.left is None:
                self.left = new_node
            else:
                self.left.addToRoot(new_node)
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right.addToRoot(new_node)

    # Postorder Traversal -> LRN
    def listEventNumber(self):
        result = []

        if self.left is not None:
            result += self.left.listEventNumber()

        if self.right is not None:
            result += self.right.listEventNumber()

        if self.val % 2 == 0:
            result.append(self.val)

        return result


class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        self.root.addToRoot(new_node)

    def listEventNumber(self):
        if self.root is None:
            return []

        return self.root.listEventNumber()


n = int(input())
list = list(map(int, input().split()))

bst = BST()
for i in range(n):
    bst.addToBST(list[i])

list_number = bst.listEventNumber()
for i in range(len(list_number)):
    print(list_number[i], end=' ')
