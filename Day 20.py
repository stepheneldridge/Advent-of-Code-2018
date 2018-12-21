# Day 20
from collections import defaultdict
INPUT = open('Day 20.txt', 'r').read().split('\n')[0].strip()
key = ""
data = []
for i in INPUT:
    if i == '^' or i == '$':
        pass
    elif i in "NEWS":
        key += i
    else:
        if key != '' or data[-1] == '|':
            data.append(key)
        data.append(i)
        key = ""


def get(index, data):
    tree = []
    split = None
    i = index
    while i < len(data):
        if data[i] == '(':
            x, y = get(i + 1, data)
            tree.append(y)
            i = x
        elif data[i] == ')':
            break
        elif data[i] == '|':
            split = len(tree)
        else:
            tree.append(data[i])
        i += 1
    if split:
        return i, (tree[:split], tree[split:])
    else:
        return i, tree


tree = get(0, data)[1]


def get_path(subtree):
    path = ""
    for i in subtree:
        if isinstance(i, str):
            path += i
        elif isinstance(i, tuple):
            a = get_path(i[0])
            b = get_path(i[1])
            if b == '':
                continue
            else:
                path += max(a, b, key=lambda a: len(a))
    return path


path = get_path(tree)
print("part_1:", len(path))

vectors = {"N": -1j, "E": 1, "S": 1j, "W": -1}
stack = []
paths = defaultdict(lambda: 1 << 10)
prev = 0
x = 0
paths[0] = 0
for c in INPUT[1:-2]:
    if c == "(":
        stack += [x]
    elif c == ")":
        x = stack.pop()
    elif c == "|":
        x = stack[-1]
    else:
        x += vectors[c]
        paths[x] = min(paths[x], paths[prev] + 1)
    prev = x
v = paths.values()
print("part_2:", sum(x >= 1000 for x in v))
