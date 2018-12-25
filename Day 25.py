# Day 25
import re
INPUT = open('Day 25.txt', 'r')
data = []
for line in INPUT:
    data.append(list(map(int, re.findall(r'-?\d+', line))))


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3])


consts = []
for i in range(len(data)):
    s = set()
    s.add(i)
    for j in range(i + 1, len(data)):
        if dist(data[i], data[j]) <= 3:
            s.add(j)
    consts.append(s)
index = 0
index2 = 1
while index < len(consts) - 1:
    if len(consts[index].intersection(consts[index2])) > 0:
        consts[index].update(consts[index2])
        consts.pop(index2)
        index2 = index + 1
    else:
        index2 += 1
    if index2 >= len(consts):
        index += 1
        index2 = index + 1
print("part_1:", len(consts))
print("part_2: finished")
