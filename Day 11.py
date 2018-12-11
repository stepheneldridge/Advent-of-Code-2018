# Day 11
INPUT = 2187
values = {}
batteries = [[0 for _ in range(300)] for _ in range(300)]


def get(x, y, sid):
    rid = x + 10
    p = (rid * y + sid) * rid
    p = (p % 1000) // 100
    return p - 5


for x in range(300):
    for y in range(300):
        batteries[x][y] = get(x, y, INPUT)


def max_for_size(size):
    v = {}
    for x in range(0, 300 - size):
        for y in range(0, 300 - size):
            temp = 0
            for i in range(size):
                for j in range(size):
                    temp += batteries[x + i][y + j]
            v["%s,%s,%s" % (x, y, size)] = temp
    m = max(v, key=lambda a: v[a])
    return m, v[m]


def max_for_coord(x, y):
    sizes = min(300 - x, 300 - y)
    size = 0
    value = 0
    best_value = 0
    for s in range(sizes):
        for i in range(s):
            value += batteries[x + s][y + i]
        for i in range(s):
            value += batteries[x + i][y + s]
        value += batteries[x + s][y + s]
        if value > best_value:
            best_value = value
            size = s + 1
    return "%s,%s,%s" % (x, y, size), best_value


print("part_1:", max_for_size(3)[0][:-2])
value = 0
key = ""
for x in range(300):
    for y in range(300):
        r = max_for_coord(x, y)
        if r[1] > value:
            value = r[1]
            key = r[0]
print("part_2:", key)
