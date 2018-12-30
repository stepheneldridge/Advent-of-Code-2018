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
    m = list(map(int, re.findall(r"\-?\d+", line)))
    if line.startswith('x'):
        xd.append(m)
        if m[0] > maxx:
            maxx = m[0]
        if m[0] < minx:
            minx = m[0]
        if max(m[1:]) > maxy:
            maxy = min(m[1:])
        if min(m[1:]) < miny:
            miny = min(m[1:])
    elif line.startswith('y'):
        yd.append(m)
        if m[0] > maxy:
            maxy = m[0]
        if m[0] < miny:
            miny = m[0]
        if max(m[1:]) > maxx:
            maxx = min(m[1:])
        if min(m[1:]) < minx:
            minx = min(m[1:])
minx -= 1
maxx += 1
miny -= 1
grid = [['.' for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
for i in xd:
    for j in range(i[1], i[2] + 1):
        grid[j - miny][i[0] - minx] = '#'
for i in yd:
    for j in range(i[1], i[2] + 1):
        grid[i[0] - miny][j - minx] = '#'


def print_grid(g):
    for y in g:
        for x in y:
            print(x, end='')
        print()


def get(p):
    if p[1] >= len(grid) or p[1] < 0:
        return None
    return grid[p[1]][p[0]]


def setc(p, v):
    grid[p[1]][p[0]] = v


current = [500 - minx, 0]
state = None
while state != 'finished':
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
        if get(current) == '|' or get(current) == '<':
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
            setc(current, '<')
            current[1] += 1
            state = 'down'
        elif get(current) == '>':
            current[0] += 1
            state = 'right'
        elif get(current) == '*':
            current[0] += 1
            state = 'rightsurface'
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
        elif get(current) == '.' or get(current) == '#':
            current[1] += 1
            state = 'leftreverse'
        elif get(current) is None:
            state = 'finished'
        elif get(current) == '<':
            setc(current, '|')
            current[0] += 1
            state = 'leftreverse'
    elif state == 'rightreverse':
        if get(current) == '>' or get(current) == '*':
            setc(current, '|')
            current[0] -= 1
        elif get(current) == '~':
            setc(current, '^')
            current[0] -= 1
            state = 'leftsurface'
        elif get(current) == '|':
            current[1] -= 1
            state = 'up'
    elif state == 'leftreverse':
        if get(current) == '<' or get(current) == '|':
            setc(current, '|')
            current[0] += 1
        elif get(current) == '.':
            setc(current, '*')
            current[1] += 1
            state = 'down'
        elif get(current) == '~':
            state = 'finished'
        elif get(current) == '#':
            current[0] -= 1
            state = 'up'
    elif state == 'rightsurface':
        if get(current) == '.':
            setc(current, '*')
            current[1] += 1
            state = 'down'
        elif get(current) == '#':
            current[0] -= 1
            state = 'rightbacktrack'
    elif state == 'leftsurface':
        if get(current) == '~':
            setc(current, '|')
            current[0] -= 1
        elif get(current) == '#':
            current[0] += 1
            state = 'returntocenter'
    elif state == 'returntocenter':
        if get(current) == '|':
            current[0] += 1
        elif get(current) == '^':
            setc(current, '|')
            current[1] -= 1
            state = 'up'
count_stable = 0
count_unstable = 0
for y in grid[1:]:
    count_stable += y.count('~')
    count_unstable += y.count('|')
print("part_1:", count_stable + count_unstable)
print("part_2:", count_stable)
INPUT.close()
