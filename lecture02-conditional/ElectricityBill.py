old, new = map(int, input().split())

# 120 323
kw = new - old
total = 0

# first 50 kwh
if kw >= 50:
    total = total + (50 * 1484)
    kw = kw - 50
elif kw < 50:
    total = total + (kw * 1484)
    kw = kw - kw

# next 50 kwh
if kw > 0 and kw >= 50:
    total = total + (50 * 1533)
    kw = kw - 50
elif kw > 0 and kw < 50:
    total = total + (kw * 1533)
    kw = kw - kw

# next 100 kwh
if kw > 0 and kw >= 100:
    total = total + (100 * 1786)
    kw = kw - 100
elif kw > 0 and kw < 100:
    total = total + (kw * 1786)
    kw = kw - kw

# next 100 kwh
if kw > 0 and kw >= 100:
    total = total + (100 * 2242)
    kw = kw - 100
elif kw > 0 and kw < 100:
    total = total + (kw * 2242)
    kw = kw - kw

# next 100 kwh
if kw > 0 and kw >= 100:
    total = total + (100 * 2503)
    kw = kw - 100
elif kw > 0 and kw < 100:
    total = total + (kw * 2503)
    kw = kw - kw

#  over kwh
if kw > 0:
    total = total + (kw * 2587)

total = total + (total * 0.1)
print(int(total))
