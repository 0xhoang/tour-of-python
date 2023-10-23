class Color:
    def __init__(self, code, length):
        self.code = code
        self.length = length


class GroupColor:
    def __init__(self, color):
        self.code = color.code
        self.length = color.length
        self.total = 1

    def add(self, other):
        self.length = self.length + other.length
        self.total = self.total + 1


class Ribbon:
    def __init__(self, list_color):
        self.list_color = list_color

    def groupColor(self):
        list = []

        for i in range(len(self.list_color)):
            if len(list) == 0:
                group = GroupColor(self.list_color[i])
                list.append(group)
                continue

            for j in range(len(list)):
                if list[j].code == self.list_color[i].code:
                    list[j].add(self.list_color[i])
                    break
                elif j == len(list) - 1:
                    group = GroupColor(self.list_color[i])
                    list.append(group)
                    break

        # sort
        for i in range(len(list)):
            for j in range(len(list) - 1):
                if list[j].code > list[j + 1].code:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp

        return list


n = int(input())
list = []
for i in range(n):
    list_color = []
    c, l = map(int, input().split())
    color = Color(c, l)
    list.append(color)

ribbon = Ribbon(list)
rs = ribbon.groupColor()

print(len(rs))
for i in range(len(rs)):
    print(rs[i].code, rs[i].length, rs[i].total)
