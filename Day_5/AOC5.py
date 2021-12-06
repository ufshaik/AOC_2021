from collections import defaultdict

ventLines = defaultdict(int)
ventLines2 = defaultdict(int)

f = open("AOCI5", "r")
lines = f.readlines()


def sumVents(option):
    count = 0
    local_vent = ventLines
    if option == 1:
        local_vent = ventLines2
    for x in local_vent.values():
        if x >= 2:
            count += 1
    return count


for line in lines:
    L, R = line.split("-")
    a, b = [int(x) for x in L.split(",")]
    c, d = [int(x) for x in R.split(",")]
    if a == c:
        for y in range(min(b, d), max(b, d) + 1):
            ventLines[a, y] += 1
    elif b == d:
        for y in range(min(a, c), max(a, c) + 1):
            ventLines[y, b] += 1

print(sumVents(0))


def diagonal_generator(d1, d2):
    if d1 >= d2:
        return range(d1, d2 - 1, -1)
    else:
        return range(d1, d2 + 1, 1)


for line in lines:
    L, R = line.split("-")
    a, b = [int(x) for x in L.split(",")]
    c, d = [int(x) for x in R.split(",")]
    if a == c:
        for y in range(min(b, d), max(b, d) + 1):
            ventLines2[a, y] += 1
    elif b == d:
        for y in range(min(a, c), max(a, c) + 1):
            ventLines2[y, b] += 1
    else:
        for x, y in zip(diagonal_generator(a, c), diagonal_generator(b, d)):
            ventLines2[x, y] += 1

print(sumVents(1))

