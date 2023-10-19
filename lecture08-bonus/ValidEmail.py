email = input()


def email_valid(email):
    if '@' not in email:
        return False

    if email.count('@') > 1:
        return False

    name_subfix = email.split('@')[0]

    if name_subfix == '':
        return False

    valid = True
    for i in range(len(name_subfix)):
        if name_subfix[i] == '.' or name_subfix[i] == '_':
            continue

        if 'a' <= name_subfix[i].lower() <= 'z':
            continue

        if '0' <= name_subfix[i].lower() <= '9':
            continue

        valid = False
        break

    if not valid:
        return False

    sub_fix = email.split('@')[1]

    if '.' not in sub_fix:
        return False

    if sub_fix.count('.') > 2:
        return False

    part1 = sub_fix.split('.')[0]
    part2 = sub_fix.split('.')[1]

    if sub_fix.count('.') == 1:
        if part1 == '' or part2 == '':
            return False
    else:
        part3 = sub_fix.split('.')[2]
        if part1 == '' or part2 == '' or part3 == '':
            return False

    valid = True
    for i in range(len(sub_fix)):
        if sub_fix[i] == '.':
            continue

        if 'a' <= sub_fix[i].lower() <= 'z':
            continue

        valid = False

    if not valid:
        return False

    return True


if email_valid(email):
    print("VALID")
else:
    print("INVALID")
