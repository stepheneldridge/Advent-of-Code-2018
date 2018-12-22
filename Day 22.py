# Day 22
from collections import defaultdict
from heapq import heappush, heappop
depth = 4845
target = (6, 770, 1)
grid = [[0 for _ in range(target[1] * 3)] for _ in range(target[0] * 10)]


def get_geoindex(x, y, grid):
    if x == target[0] and y == target[1]:
        return 0
    if x == 0:
        return y * 48271
    if y == 0:
        return x * 16807
    return grid[x - 1][y] * grid[x][y - 1]


for x in range(len(grid)):
    for y in range(len(grid[x])):
        grid[x][y] = ((get_geoindex(x, y, grid) + depth) % 20183)

total = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        grid[x][y] %= 3
        if x <= target[0] and y <= target[1]:
            total += grid[x][y]
print("part_1:", total)


def dijkstra(start, goal, data):
    neighbors = []
    for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        for j in range(3):
            neighbors.append(i + [j])

    def cost_to(p1, p2):
        return 1 if p1[2] == p2[2] else 8

    def is_valid(p):
        if p[0] < 0 or p[1] < 0:
            return False
        if p[0] >= len(data) or p[1] >= len(data[p[0]]):
            return False
        if data[p[0]][p[1]] == p[2]:
            return False
        return True
    explore = [(0, start)]
    score = defaultdict(lambda: 1e9)
    score[start] = 0
    while len(explore) > 0:
        c, current = heappop(explore)
        if current == goal:
            return c
        if c > score[current]:
            continue
        for i in neighbors:
            neighbor = (current[0] + i[0], current[1] + i[1], i[2])
            if not is_valid(neighbor) or data[current[0]][current[1]] == i[2]:
                continue
            cost = c + cost_to(current, neighbor)
            if cost < score[neighbor]:
                heappush(explore, (cost, neighbor))
                score[neighbor] = cost


print("part_2:", dijkstra((0, 0, 1), target, grid))
