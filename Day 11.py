# Day 11
INPUT = 2187
batteries = [[0 for _ in range(300)] for _ in range(300)]


def get(x, y, sid):
    rid = x + 10
    p = (rid * y + sid) * rid
    p = (p % 1000) // 100
    return p - 5


for x in range(300):
    for y in range(300):
        batteries[x][y] = get(x, y, INPUT)

sums = [[0 for _ in range(301)] for _ in range(301)]
for x in range(1, 301):
    for y in range(1, 301):
        sums[x][y] = batteries[x - 1][y - 1] + sums[x][y - 1] + sums[x - 1][y] - sums[x - 1][y - 1]


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


def max_for_coord_sums(x, y):
    sizes = min(300 - x, 300 - y)
    size = 0
    value = 0
    best_value = 0
    for s in range(1, sizes + 1):
        value = sums[x + s][y + s] - sums[x][y + s] - sums[x + s][y] + sums[x][y]
        if value > best_value:
            best_value = value
            size = s
    return "%s,%s,%s" % (x, y, size), best_value


print("part_1:", max_for_size(3)[0][:-2])
value = 0
key = ""
for x in range(300):
    for y in range(300):
        r = max_for_coord_sums(x, y)
        if r[1] > value:
            value = r[1]
            key = r[0]
print("part_2:", key)
