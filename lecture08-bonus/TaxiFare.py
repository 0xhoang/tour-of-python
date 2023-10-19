k = int(input())


def taxi_fee(kilometer):
    if kilometer <= 1:
        return 15000
    elif kilometer <= 5:
        return 15000 + (kilometer - 1) * 13500
    elif 6 <= kilometer < 12:
        return 15000 + (4 * 13500) + (kilometer - 5) * 11000
    else:
        total = 15000 + (4 * 13500) + ((kilometer - 5) * 11000)
        return total - total * 0.1


print("{:.0f}".format(taxi_fee(k)))
