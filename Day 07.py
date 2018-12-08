# Day 7
import re
INPUT = open('Day 07.txt', 'r')
r = re.compile(r"Step (\w) must be finished before step (\w) can begin\.")
steps = {}
for line in INPUT:
    m = r.match(line)
    if m.group(2) in steps:
        steps[m.group(2)].append(m.group(1))
    else:
        steps[m.group(2)] = [m.group(1)]
first = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - set(steps.keys())

for i in first:
    steps[i] = ["#"]
ready = ["#"]
order = []
while len(ready) > 0:
    ready.sort()
    ready.reverse()
    order.append(ready.pop())
    ready = list(set([i for i in steps if set(steps[i]).issubset(set(order)) and i not in order]))
print("part_1:", "".join(order[1:]))

time = 0
active = {}
done = {"#"}
ready = list(set([i for i in steps if set(steps[i]).issubset(done) and i not in done and i not in active]))
while len(ready) > 0 or len(active) > 0:
    ready.sort()
    ready.reverse()
    for i in range(5):
        if len(active.keys()) == 5 or len(ready) == 0:
            break
        active[ready.pop()] = 0
    for i in active:
        active[i] += 1
        if active[i] >= 60 + ord(i) - 64:
            done.add(i)
    for i in done:
        if i in active:
            del active[i]
    time += 1
    ready = list(set([i for i in steps if set(steps[i]).issubset(done) and i not in done and i not in active]))
print("part_2:", time)
INPUT.close()
