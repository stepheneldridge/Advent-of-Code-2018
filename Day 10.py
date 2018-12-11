# Day 10
import re
INPUT = open('Day 10.txt', 'r')
p = []
v = []
for line in INPUT:
    m = re.findall(r"-?\d+", line.strip())
    d = list(map(int, m))
    p.append(d[0:2])
    v.append(d[2:])


def move_points(points, speed, time):
    j = 0
    for i in points:
        i[0] += speed[j][0] * time
        i[1] += speed[j][1] * time
        j += 1


time = 0
move_points(p, v, time)
while True:
    move_points(p, v, 1)
    time += 1
    if (max(p, key=lambda a: a[1])[1] - min(p, key=lambda a: a[1])[1]) == 9:
        bbox = [min(p, key=lambda a: a[0])[0], min(p, key=lambda a: a[1])[1], max(p, key=lambda a: a[0])[0], max(p, key=lambda a: a[1])[1]]
        print("part_1:")
        for i in range(bbox[3] - bbox[1] + 1):
            print("".join(['#' if [j + bbox[0], i + bbox[1]] in p else " " for j in range(bbox[2] - bbox[0] + 1)]))
        print("part_2:", time)
        break
INPUT.close()
