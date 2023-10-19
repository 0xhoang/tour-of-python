n = int(input())
arr = input().split()

is_liked = True

for i in range(n):
    if int(arr[i]) == 0:
        is_liked = False
        break

if is_liked:
    print("YES")
else:
    print("NO")
