# Day 12
import re
INPUT = open('Day 12.txt', 'r')
data = []
start = None
for line in INPUT:
    m = re.findall(r"[\.#]+", line.strip())
    if start is None:
        j = 0
        start = {}
        for i in m[0]:
            start[j] = i
            j += 1
    elif len(m) > 0:
        data.append(m)
rules = {}
for i in data:
    rules[i[0]] = i[1]

totals = []
while len(totals) < 200:
    k = start.keys()
    start[max(k) + 1] = '.'
    start[max(k) + 1] = '.'
    start[min(k) - 1] = '.'
    start[min(k) - 1] = '.'
    new_start = {}
    for i in start:
        key = ""
        if (i - 2) in start:
            key += start[i - 2]
        else:
            key += '.'
        if (i - 1) in start:
            key += start[i - 1]
        else:
            key += '.'
        key += start[i]
        if (i + 1) in start:
            key += start[i + 1]
        else:
            key += '.'
        if (i + 2) in start:
            key += start[i + 2]
        else:
            key += '.'
        new_start[i] = rules[key]
    start = new_start
    total = 0
    for i in start:
        if start[i] == '#':
            total += i
    totals.append(total)
print("part_1:", totals[19])
p2 = (50000000000 - len(totals)) * (totals[-1] - totals[-2]) + totals[-1]
print("part_2:", p2)
INPUT.close()
