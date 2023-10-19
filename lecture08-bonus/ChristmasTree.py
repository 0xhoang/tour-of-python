k = int(input())


def print_tree(node):
    for i in range(node):
        print(" " * (node - i - 1) + "*" * (2 * i + 1))


print_tree(k)
