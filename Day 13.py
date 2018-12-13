# Day 13
INPUT = open('Day 13.txt', 'r')
data = []
for line in INPUT:
    data.append(list(line))
carts = []
pos = []


def init():
    carts = []
    pos = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in ['^', '>', 'v', '<']:
                a = [x, y]
                pos.append(a)
                cart = [a, data[y][x], 0]
                carts.append(cart)
    return pos, carts


vectors = {'^': [0, -1], 'v': [0, 1], '<': [-1, 0], '>': [1, 0]}
dirs = ['^', '>', 'v', '<']


def move(c):
    v = vectors[c[1]]
    p = data[c[0][1] + v[1]][c[0][0] + v[0]]
    if (p == '|' and v[0] == 0) or (p == '-' and v[1] == 0):
        pass
    elif p == '/':
        if c[1] == '^':
            c[1] = '>'
        elif c[1] == '<':
            c[1] = 'v'
        elif c[1] == 'v':
            c[1] = '<'
        elif c[1] == '>':
            c[1] = '^'
    elif p == '\\':
        if c[1] == '^':
            c[1] = '<'
        elif c[1] == '<':
            c[1] = '^'
        elif c[1] == 'v':
            c[1] = '>'
        elif c[1] == '>':
            c[1] = 'v'
    elif p == '+':
        if c[2] == 0:
            c[1] = dirs[(dirs.index(c[1]) - 1) % 4]
        elif c[2] == 2:
            c[1] = dirs[(dirs.index(c[1]) + 1) % 4]
        c[2] = (c[2] + 1) % 3
    elif p in dirs:
        if (dirs.index(p) ^ dirs.index(c[1])) != 2:
            c[1] = p
    if [c[0][0] + v[0], c[0][1] + v[1]] in pos:
        return [c[0][0] + v[0], c[0][1] + v[1]]
    else:
        c[0][0] += v[0]
        c[0][1] += v[1]
        return


def print_map():
    for y in range(len(data)):
        for x in range(len(data[y])):
            if [x, y] in pos:
                c = [m for m in carts if m[0] == [x, y]]
                if len(c) == 0:
                    print('X', end='')
                else:
                    print(c[0][1], end='')
            else:
                print(data[y][x], end='')


pos, carts = init()
crash = False
while True:
    carts.sort(key=lambda a: [a[0][1], a[0][0]])
    for c in carts:
        crash = move(c)
        if crash:
            break
    if crash:
        break
print("part_1:", "%s,%s" % (crash[0], crash[1]))
pos, carts = init()
while len(carts) > 1:
    crash = False
    carts.sort(key=lambda a: [a[0][1], a[0][0]])
    remove = []
    for c in carts:
        crash = move(c)
        if crash:
            remove.append(carts.index(c))
            for i in carts:
                if i[0] == crash:
                    remove.append(carts.index(i))
    remove = list(set(remove))
    remove.sort()
    remove.reverse()
    for i in remove:
        c = carts.pop(i)
        pos.remove(c[0])
last = carts[0][0]
print("part_2:", "%s,%s" % (last[0], last[1]))
INPUT.close()
