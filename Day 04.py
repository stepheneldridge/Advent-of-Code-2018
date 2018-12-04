# Day 4
import re
from datetime import datetime

INPUT = open('Day 04.txt', 'r')
r = re.compile(r"\[(\d+-\d+-\d+ \d\d:\d\d)\] (wakes up|falls asleep|Guard #(\d+) begins shift)")
data = []
for line in INPUT:
    m = r.match(line)
    d = datetime.fromisoformat(m.group(1))
    data.append([d, *m.groups()[1:]])
data.sort(key=lambda a: a[0])
schedule = {}
last = -1


def fill(s, id, m, a):
    for i in range(60 - m):
        s[id][i + m] += a


for i in data:
    if i[2] is not None:
        last = int(i[2])
        if last not in schedule:
            schedule[last] = [0 for _ in range(60)]
    elif i[1] == 'wakes up':
        fill(schedule, last, i[0].minute, -1)
    elif i[1] == 'falls asleep':
        fill(schedule, last, i[0].minute, 1)

best_id = max(schedule, key=lambda a: sum(schedule[a]))
best_minute = schedule[best_id].index(max(schedule[best_id]))
print("part_1:", best_id * best_minute)

best_id = max(schedule, key=lambda a: max(schedule[a]))
best_minute = schedule[best_id].index(max(schedule[best_id]))
print("part_2:", best_id * best_minute)
INPUT.close()
