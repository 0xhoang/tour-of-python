a, b, c, d = map(int, input().split())

bigBag = a

if b > bigBag:
    bigBag = b

if c > bigBag:
    bigBag = c

if d > bigBag:
    bigBag = d

print(bigBag)
