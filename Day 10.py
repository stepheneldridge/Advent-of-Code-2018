# Day 10
# Tyler add discord: Areus#8910
import re
INPUT = open('Day 10.txt', 'r')
data = []
for line in INPUT:
    m = re.findall(r"\d+", line)
    data.append(list(map(int, m)))

print("part_1:")
print("part_2:")
INPUT.close()
