# Day 8
import re
INPUT = open('Day 08.txt', 'r')
values = []
for line in INPUT:
    m = re.findall(r"\d+", line)
    values = list(map(int, m))


def get(index, data):
    cn = data[index]
    mdn = data[index + 1]
    meta = 0
    index += 2
    for i in range(cn):
        a, b = get(index, data)
        index = a
        meta += b
    for i in range(mdn):
        meta += data[index]
        index += 1
    return index, meta


print("part_1:", get(0, values)[1])


def get(index, data):
    cn = data[index]
    mdn = data[index + 1]
    meta = 0
    index += 2
    children_meta = []
    for i in range(cn):
        a, b = get(index, data)
        index = a
        children_meta.append(b)
    for i in range(mdn):
        if cn == 0:
            meta += data[index]
        else:
            if data[index] - 1 in range(len(children_meta)):
                meta += children_meta[data[index] - 1]
        index += 1
    return index, meta


print("part_2:", get(0, values)[1])
INPUT.close()
