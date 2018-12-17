# Day 17
import re
INPUT = open("Day 17.txt", "r")
xd = []
yd = []
minx = 2 << 10
miny = 2 << 10
maxx = 0
maxy = 0
for line in INPUT:
    if line.startswith('x'):
        xd.append(list(map(int, re.findall(r"\-?\d+", line))))
        if xd[-1][0] > maxx:
            maxx = xd[-1][0]
        if xd[-1][0] < minx:
            minx = xd[-1][0]
        if max(xd[-1][1:]) > maxy:
            maxy = min(xd[-1][1:])
        if min(xd[-1][1:]) < miny:
            miny = min(xd[-1][1:])
    elif line.startswith('y'):
        yd.append(list(map(int, re.findall(r"\-?\d+", line))))
        if yd[-1][0] > maxy:
            maxy = yd[-1][0]
        if yd[-1][0] < miny:
            miny = yd[-1][0]
        if max(yd[-1][1:]) > maxx:
            maxx = min(yd[-1][1:])
        if min(yd[-1][1:]) < minx:
            minx = min(yd[-1][1:])
minx -= 1
maxx += 1
miny -= 1


def print_grid(g):
    for y in g:
        for x in y:
            print(x, end='')
        print()


grid = [['.' for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
for i in xd:
    for j in range(i[1], i[2] + 1):
        grid[j - miny][i[0] - minx] = '#'
for i in yd:
    for j in range(i[1], i[2] + 1):
        grid[i[0] - miny][j - minx] = '#'


def count_water(x, y, grid):
    count = 0
    if y >= len(grid):
        return 0, True
    fall = False
    if grid[y][x] == '.':
        c, f = count_water(x, y + 1, grid)
        count += c
        fall = f
        if not f:
            c, f = count_water(x - 1, y, grid)
            count += c
            c, g = count_water(x + 1, y, grid)
            count += c
            fall = f or g
    return count, fall


def get(p):
    if p[1] >= len(grid) or p[1] < 0:
        return None
    return grid[p[1]][p[0]]


def setc(p, v):
    grid[p[1]][p[0]] = v


current = [500 - minx, 0]
state = None
while state != 'finished':
    # print(state, get(current))
    if state is None:
        if get(current) == '.':
            setc(current, '|')
            current[1] += 1
            state = 'down'
    elif state == 'down':
        if get(current) == '.':
            setc(current, '|')
            current[1] += 1
        elif get(current) == '#' or get(current) == '~':
            current[1] -= 1
            state = 'backup'
        elif get(current) is None:
            current[1] -= 1
            state = 'up'
        elif get(current) == '|':
            current[1] -= 1
            state = 'up'
    elif state == 'backup':
        if get(current) == '|':
            setc(current, '<')
            current[0] -= 1
            state = 'left'
        elif get(current) == '>':
            current[0] += 1
            state = 'right'
        elif get(current) == '*':
            current[0] += 1
            state = 'rightsurface'
    elif state == 'left':
        if get(current) == '.':
            setc(current, '|')
            current[1] += 1
            state = 'down'
        elif get(current) == '#':
            current[0] += 1
            state = 'right'
        elif get(current) == '|':
            current[1] += 1
            state = 'down'
        elif get(current) == '>':
            current[0] += 1
            state = 'right'
    elif state == 'right':
        if get(current) == '<':
            setc(current, '~')
            current[0] += 1
        elif get(current) == '.':
            setc(current, '>')
            current[1] += 1
            state = 'down'
        elif get(current) == '#':
            current[0] -= 1
            state = 'rightbacktrack'
    elif state == 'rightbacktrack':
        if get(current) == '>':
            setc(current, '~')
            current[0] -= 1
        elif get(current) == '~':
            current[1] -= 1
            state = 'left'
        elif get(current) == '|':
            current[1] -= 1
            state = 'up'
        elif get(current) == '*':
            setc(current, '|')
            current[0] -= 1
    elif state == 'up':
        if get(current) == '|':
            current[1] -= 1
        elif get(current) == '>' or get(current) == '*':
            setc(current, '|')
            current[0] -= 1
            state = 'rightreverse'
        elif get(current) == '.':
            current[1] += 1
            state = 'leftreverse'
        elif get(current) is None:
            state = 'finished'
    elif state == 'rightreverse':
        if get(current) == '>' or get(current) == '*':
            setc(current, '|')
            current[0] -= 1
        elif get(current) == '~' or get(current) == '|':
            current[1] -= 1
            state = 'up'
    elif state == 'leftreverse':
        if get(current) == '<' or get(current) == '|':
            setc(current, '|')
            current[0] += 1
        elif get(current) == '.':
            setc(current, '>')
            current[0] += 1
            state = 'rightsurface'
        elif get(current) == '~':
            state = 'finished'
    elif state == 'rightsurface':
        if get(current) == '.':
            setc(current, '*')
            current[1] += 1
            state = 'down'
        elif get(current) == '#':
            current[0] -= 1
            state = 'rightbacktrack'

count = 0
for y in grid[1:]:
    count += y.count('~')
    count += y.count('|')
print("part_1:", count)
for y in range(len(grid)):
    while True:
        change = False
        for x in range(len(grid[y])):
            if get([x, y]) == '~':
                if get([x + 1, y]) == '|' or get([x - 1, y]) == '|':
                    setc([x, y], '|')
                    change = True
        if not change:
            break

count = 0
for y in grid[1:]:
    count += y.count('~')
print("part_2:", count)
INPUT.close()
