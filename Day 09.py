# Day 9
# Tyler add discord: Areus#8910
import re
INPUT = open('Day 09.txt', 'r')
data = []
for line in INPUT:
    m = re.findall(r"\d+", line)
    data.append(list(map(int, m)))
players = data[0][0]
marbles = data[0][1]
scores = [0 for _ in range(players)]
current_player = 0
current_index = 0
circle = [0]
for i in range(marbles):
    if (i + 1) % 23 != 0:
        circle.insert(current_index - 1, i + 1)
        current_index = circle.index(i + 1)
    else:
        scores[current_player] += (i + 1)
        current_index = (current_index + 7) % len(circle)
        c = circle.pop(current_index)
        scores[current_player] += c
        current_index = (current_index - 1) % len(circle)
    current_player = (current_player + 1) % players
print("part_1:", max(scores))
# The magic of linked lists. Both parts take equal time :|
marbles *= 100
scores = [0 for _ in range(players)]
current_player = 0
current = [0]
current.extend([current, current])
for i in range(marbles):
    if (i + 1) % 23 != 0:
        current = current[1]
        a = [i + 1, current[1], current]
        current[1] = a
        a[1][2] = a
        current = a
    else:
        for _ in range(7):
            current = current[2]
        scores[current_player] += i + 1 + current[0]
        current[1][2] = current[2]
        current[2][1] = current[1]
        current = current[1]
    current_player = (current_player + 1) % players
print("part_2:", max(scores))
INPUT.close()
