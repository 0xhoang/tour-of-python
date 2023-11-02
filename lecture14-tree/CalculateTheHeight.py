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

    def height(self):
        heightLeft = 0
        heightRight = 0

        if self.left is not None:
            heightLeft = self.left.height()

        if self.right is not None:
            heightRight = self.right.height()

        # break point
        return 1 + max(heightLeft, heightRight)


class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        self.root.addToRoot(new_node)

    def height(self):
        if self.root is None:
            return 0

        return self.root.height()


n = int(input())
list = list(map(int, input().split()))

bst = BST()
for i in range(n):
    bst.addToBST(list[i])

print(bst.height())
