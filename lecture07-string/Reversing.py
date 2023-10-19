s = input()


def reversing(s):
    arr = s.split(" ")

    new_str = ''
    for i in range(-1, -len(arr) - 1, -1):
        new_str += arr[i] + " "

    return new_str

print(reversing(s))
