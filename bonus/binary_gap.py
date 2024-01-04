def solution(N):
    count = 0
    remain = 0
    start_count = False
    while N >= 1:
        bin = N % 2

        if bin == 0:
            count = count + 1
        else:
            if start_count == False:
                count = 0
                start_count = True

            if remain < count:
                remain = count

            count = 0

        N = N // 2

    return remain


rs = solution(1041)
print(rs)
