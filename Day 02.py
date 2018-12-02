# Day 2
INPUT = open('Day 02.txt', 'r')
ids = []
two = 0
three = 0
for line in INPUT:
    x = line.strip()
    ids.append(x)
    s2 = False
    s3 = False
    for i in set(x):
        if x.count(i) == 2 and not s2:
            two += 1
            s2 = True
        elif x.count(i) == 3 and not s3:
            three += 1
            s3 = True
print("part_1:", two * three)


def comp(v, i, j):
    diff = None
    for k in range(len(v)):
        if v[k] != ids[i + j][k]:
            if diff is None:
                diff = k
            else:
                return None
    return diff


match = None
for i, v in enumerate(ids):
    for j in range(len(ids) - i - 1):
        diff = comp(v, i, j)
        if diff is not None:
            match = v[0:diff] + v[diff + 1:]
            break
    if match is not None:
        break

print("part_2:", match)
INPUT.close()
