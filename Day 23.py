# Day 23
import re
INPUT = open('Day 23.txt', 'r').read().split('\n')
data = []
for line in INPUT:
    if line != "":
        m = re.findall(r"\-?\d+", line)
        data.append(list(map(int, m)))


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


best = data[data.index(max(data, key=lambda a: a[3]))]
count = 0
for i in data:
    if dist(best, i) <= best[3]:
        count += 1
print("part_1:", count)

xs = [i[0] for i in data]
ys = [i[1] for i in data]
zs = [i[2] for i in data]
size = 1
while size < max(xs) - min(xs):
    size *= 2
while size > 0:
    best_count = 0
    best = None
    answer = int(1e20)
    for i in range(min(xs), max(xs) + 1, size):
        for j in range(min(ys), max(ys) + 1, size):
            for k in range(min(zs), max(zs) + 1, size):
                count = 0
                for bot in data:
                    if (dist((i, j, k), bot) - bot[3]) // size <= 0:
                        count += 1
                if count > best_count:
                    best_count = count
                    best = (i, j, k)
                    answer = dist((0, 0, 0), best)
                elif count == best_count:
                    if dist((0, 0, 0), (i, j, k)) < answer:
                        best = (i, j, k)
                        answer = dist((0, 0, 0), best)
    if size == 1:
        print("part_2:", answer)
    xs = [best[0] - size, best[0] + size]
    ys = [best[1] - size, best[1] + size]
    zs = [best[2] - size, best[2] + size]
    size //= 2
