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

    def sum(self, value):
        total = 0

        if self.left is not None:
            total += self.left.sum(value)

        if self.right is not None:
            total += self.right.sum(value)

        if self.val < value:
            return total + self.val

        return total


class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        self.root.addToRoot(new_node)

    def sum(self, value):
        if self.root is None:
            return 0

        return self.root.sum(value)


n, x = map(int, input().split())
list = list(map(int, input().split()))

bst = BST()
for i in range(n):
    bst.addToBST(list[i])

print(bst.sum(x))
