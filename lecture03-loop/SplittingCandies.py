bag = int(input())

bag_invalid = 0

for i in range(bag):
    number = int(input())

    if number % 2 != 0:
        bag_invalid += 1

if bag_invalid == 0:
    print("YES")
else:
    print("NO")
