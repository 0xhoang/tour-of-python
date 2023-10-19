n = int(input())


def choice_packet(n):
    max_apple = 0
    max_orange = 0
    index = 0

    for i in range(n):
        arr = list(map(int, input().split()))
        if max_apple < arr[0]:
            max_apple = arr[0]
            max_orange = arr[1]
            index = i + 1

        elif max_apple == arr[0]:
            if max_orange < arr[1]:
                max_orange = arr[1]
                index = i + 1

    return index


print(choice_packet(n))
