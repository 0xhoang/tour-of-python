min = 10
max = 0

while 1 == 1:
    score = int(input())
    if score == -1:
        break

    if score > max:
        max = score

    if score < min:
        min = score

print("{0} {1}".format(max, min))
