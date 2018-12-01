# Day 1
INPUT = open('Day 01.txt', 'r')
freq = 0
v = []
for line in INPUT:
    freq += int(line)
    v.append(int(line))
print("part_1:", freq)
freq = 0
a = {0}
i = 0
while True:
    freq += v[i]
    if freq in a:
        break
    a.add(freq)
    i += 1
    i %= len(v)
print("part_2:", freq)
INPUT.close()
