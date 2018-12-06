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
        return -1, sum(dis)
    return dis.index(min(dis)), sum(dis)


dists = [0 for _ in points]
dists.append(0)
edges = set()
area = 0
for i in range(bbox[2] - bbox[0] + 1):
    for j in range(bbox[3] - bbox[1] + 1):
        p, s = get_closest(i + bbox[0], j + bbox[1], points)
        if i == 0 or j == 0 or i == bbox[2] or j == bbox[3]:
            edges.add(p)
        if s < 10000:
            area += 1
        dists[p] += 1
dists[-1] = 0
for i in edges:
    dists[i] = 0
print("part_1:", max(dists))
print("part_2:", area)
INPUT.close()
