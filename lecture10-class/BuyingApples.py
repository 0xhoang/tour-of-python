class Apple:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight


class BuyApple:
    def __init__(self, apple):
        self.apple = apple

    def choice_apple(self):

        index = 0

        for i in range(len(self.apple)):
            if self.apple[index].weight < self.apple[i].weight:
                index = i
                continue
            elif self.apple[index].weight == self.apple[i].weight:
                if self.apple[index].price < self.apple[i].price:
                    index = i
                    continue

        return index


n = int(input())
apple = []
for i in range(n):
    weight, price = map(int, input().split())
    apple.append(Apple(int(price), int(weight)))

buy_apple = BuyApple(apple)
buy_apple_index = buy_apple.choice_apple()

print(buy_apple_index)
