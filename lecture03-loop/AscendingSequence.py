pre_post = 0
rule_valid = 0

while 1 == 1:
    pots = int(input())
    if pots == 0:
        break

    if pots < pre_post:
        rule_valid += 1

    pre_post = pots

if rule_valid == 0:
    print("YES")
else:
    print("NO")
