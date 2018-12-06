# Day 6
import re
INPUT = open('Day 06.txt', 'r')
r = re.compile("(\d+), (\d+)")
points = []
bbox = [2 ** 10, 2 ** 10, 0, 0]
for line in INPUT:
    m = r.match(line)
    points.append([int(m.group(1)), int(m.group(2))])
    bbox[0] = min(points[-1][0], bbox[0])
    bbox[1] = min(points[-1][1], bbox[1])
    bbox[2] = max(points[-1][0], bbox[2])
    bbox[3] = max(points[-1][1], bbox[3])


def get_closest(x, y, points):
    dis = [abs(p[0] - x) + abs(p[1] - y) for p in points]
    if dis.count(min(dis)) > 1:
        return -1
    return dis.index(min(dis))


def get_total(x, y, points):
    return sum([abs(p[0] - x) + abs(p[1] - y) for p in points])


dists = [0 for _ in points]
dists.append(0)
edges = set()
for i in range(bbox[2] - bbox[0] + 1):
    for j in range(bbox[3] - bbox[1] + 1):
        p = get_closest(i + bbox[0], j + bbox[1], points)
        dists[p] += 1

for i in range(bbox[2] - bbox[0]):
    edges.add(get_closest(i + bbox[0], bbox[1], points))

for i in range(bbox[3] - bbox[1]):
    edges.add(get_closest(bbox[0], i + bbox[1], points))

for i in range(bbox[2] - bbox[0]):
    edges.add(get_closest(i + bbox[0], bbox[3], points))

for i in range(bbox[3] - bbox[1]):
    edges.add(get_closest(bbox[2], i + bbox[1], points))

area = 0
for i in range(bbox[2] - bbox[0] + 1):
    for j in range(bbox[3] - bbox[1] + 1):
        t = get_total(i + bbox[0], j + bbox[1], points)
        if t < 10000:
            area += 1
dists[-1] = 0
for i in edges:
    dists[i] = 0
print("part_1:", max(dists))
print("part_2:", area)
INPUT.close()
