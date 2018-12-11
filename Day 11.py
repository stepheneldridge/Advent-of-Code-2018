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


print("part_1:", max_for_size(3)[0][:-2])
values = []
for s in range(300):
    values.append(max_for_size(s + 1))
print("part_2:", max(values, key=lambda a: values[a]))
