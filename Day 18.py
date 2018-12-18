# Day 18
INPUT = open("Day 18.txt", "r")
data = []
data2 = []
for line in INPUT:
    data.append(list(line.strip()))
    data2.append(list(line.strip()))

v = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0]]


def get(x, y):
    if y < 0 or x < 0 or y >= len(data) or x >= len(data[0]):
        return None
    else:
        return data[y][x]


def hash_map(g):
    h = ""
    for y in g:
        for x in y:
            h += x
    return h


scores = []
prev = []
for i in range(1000000000):
    for y in range(len(data)):
        for x in range(len(data[y])):
            a = []
            for d in v:
                if get(x + d[0], y + d[1]):
                    a.append(get(x + d[0], y + d[1]))
            if get(x, y) == '.':
                if a.count('|') >= 3:
                    data2[y][x] = '|'
                else:
                    data2[y][x] = '.'
            elif get(x, y) == '|':
                if a.count('#') >= 3:
                    data2[y][x] = '#'
                else:
                    data2[y][x] = '|'
            elif get(x, y) == '#':
                if a.count('#') >= 1 and a.count('|') >= 1:
                    data2[y][x] = '#'
                else:
                    data2[y][x] = '.'
    data, data2 = data2, data
    h = hash_map(data)
    if h in prev:
        freq = len(prev) - prev.index(h)
        min_left = int(1e9 - prev.index(h) - 1)
        print("part_1:", scores[9])
        print("part_2:", scores[(min_left % freq) + prev.index(h)])
        break
    prev.append(h)
    lum = 0
    yard = 0
    for y in data:
        lum += y.count('|')
        yard += y.count('#')
    scores.append(lum * yard)
