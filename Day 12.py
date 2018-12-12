# Day 12
import re
INPUT = open('Day 12.txt', 'r')
data = []
start = None
for line in INPUT:
    m = re.findall(r"[\.#]+", line.strip())
    if start is None:
        start = [True if x == '#' else False for x in m[0]]
    elif len(m) > 0:
        data.append(m)
rules = [False for _ in range(2 ** 5)]
for i in data:
    key = 0
    for j in i[0]:
        key = key << 1
        if j == '#':
            key += 1
    rules[key] = True if i[1] == '#' else False
zero = 0
key = 0
gen = 0
total = 0
diff = 0
while True:
    gen += 1
    key = 0
    first = False
    offset = 0
    empty = True
    total_t = 0
    for i in range(len(start)):
        key = ((key << 1) + start[i]) & 0b011111
        if empty and zero - 2 + offset + i >= 0 and zero - 2 + offset + i <= 100:
            empty = not rules[key]
        if not first and not rules[key]:
            offset += 1
        else:
            first = True
            if rules[key]:
                total_t += i + zero - 2
            start[i - offset] = rules[key]
    zero += offset - 2
    for i in range(4):
        key = (key << 1) & 0b011111
        if rules[key]:
            total_t += i + zero + len(start)
        if offset > i:
            start[i - offset] = rules[key]
        else:
            start.append(rules[key])
    diff = total_t - total
    total = total_t
    if gen == 20:
        print("part_1:", total)
    if empty is True:
        break
print("part_2:", (int(5e10) - gen) * diff + total)
INPUT.close()
