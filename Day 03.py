# Day 3
import re
p = re.compile(r"\#(\d+) \@ (\d+),(\d+)\: (\d+)x(\d+)")
INPUT = open('Day 03.txt', 'r')
data = {}
grid = []
for i in range(1000):
    grid.append([0 for _ in range(1000)])
over = 0


def fill(x, y, w, h, grid):
    ov = 0
    for i in range(w):
        for j in range(h):
            if grid[x + i][y + j] == 1:
                ov += 1
            grid[x + i][y + j] += 1
    return ov


for line in INPUT:
    m = p.match(line)
    data[m.group(1)] = list(map(int, m.groups()[1:]))
    over += fill(*data[m.group(1)], grid)
print("part_1:", over)


def check_fill(x, y, w, h, grid):
    for i in range(w):
        for j in range(h):
            if grid[x + i][y + j] != 1:
                return False
    return True


best = 0
for i, v in data.items():
    if check_fill(*v, grid):
        best = i
        break
print("part_2:", best)
INPUT.close()
