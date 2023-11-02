import sys

sys.setrecursionlimit(1000000)


class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score


class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def addToRoot(self, new_node):
        if new_node.val.score < self.val.score:
            if self.left is None:
                self.left = new_node
            else:
                self.left.addToRoot(new_node)
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right.addToRoot(new_node)

    def maxScore(self):
        if self.right is None:
            return self.val

        return self.right.maxScore()


class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        self.root.addToRoot(new_node)

    def maxScore(self):
        if self.root is None:
            return 0

        return self.root.maxScore()


n = int(input())

bst = BST()
for i in range(n):
    id, name, score = input().split()
    student = Student(id, name, float(score))
    bst.addToBST(student)

found = bst.maxScore()
print(found.id, found.name, found.score)
