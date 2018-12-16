# Day 15
INPUT = open('Day 15.txt', 'r')
data = []


class Entity():
    def __init__(self, x, y, hp, atk, species):
        self.x = x
        self.y = y
        self.hp = hp
        self.atk = atk
        self.species = species


goblins = []
elves = []
for line in INPUT:
    data.append(list(line.strip()))
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'E':
            elves.append(Entity(x, y, 200, 3, 'E'))
            data[y][x] = elves[-1]
        elif data[y][x] == 'G':
            goblins.append(Entity(x, y, 200, 3, 'G'))
            data[y][x] = goblins[-1]
print(data)
print("part_1:")
print("part_2:")
INPUT.close()
