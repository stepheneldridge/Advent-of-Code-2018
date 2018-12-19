# Day 15
INPUT = open('Day 15.txt', 'r').read().split('\n')
data = []


class Entity():
    def __init__(self, x, y, hp, atk, species):
        self.x = x
        self.y = y
        self.hp = hp
        self.atk = atk
        self.species = species
        self.moved = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.moved = True

    def attack(self, enemy):
        enemy.hp -= self.atk


directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]


def get_neighbors(x, y, explored):
    return [[x + i[0], y + i[1]] for i in directions if [x + i[0], y + i[1]] not in explored]


def print_map(map_data):
    for y in map_data:
        hps = []
        for x in y:
            if isinstance(x, Entity):
                hps.append("%s(%s)" % (x.species, x.hp))
                print(x.species, end='')
            else:
                print(x, end='')
        print(" ", " ".join(hps), end='')
        print()


goblins = []
elves = []


def reset(attack=3):
    for line in INPUT:
        data.append(list(line.strip()))
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'E':
                elves.append(Entity(x, y, 200, attack, 'E'))
                data[y][x] = elves[-1]
            elif data[y][x] == 'G':
                goblins.append(Entity(x, y, 200, 3, 'G'))
                data[y][x] = goblins[-1]


def func(keep_alive=False):
    rounds = 0
    while len(goblins) > 0 and len(elves) > 0:
        for y in range(len(data)):
            for x in range(len(data[y])):
                if isinstance(data[y][x], Entity):
                    current_entity = data[y][x]
                    if current_entity.hp <= 0:
                        continue
                    if current_entity.moved is False:
                        best_dist = 2 << 10
                        best_dir = -1
                        d = 0
                        target = None
                        for w in [[x + i[0], y + i[1]] for i in directions]:
                            dist = 0
                            if isinstance(data[w[1]][w[0]], Entity) and data[w[1]][w[0]].species != current_entity.species and data[w[1]][w[0]].hp > 0:
                                if dist < best_dist:
                                    target = data[w[1]][w[0]]
                                    best_dist = dist
                                    best_dir = d
                                d += 1
                                continue
                            elif data[w[1]][w[0]] != '.':
                                d += 1
                                continue
                            explored = [[x, y]]
                            explore = get_neighbors(*w, explored)
                            found = False
                            while len(explore) > 0 and not found:
                                dist += 1
                                new_set = []
                                for i in explore:
                                    if isinstance(data[i[1]][i[0]], Entity) and data[i[1]][i[0]].species != current_entity.species and data[i[1]][i[0]].hp > 0:
                                        if dist < best_dist:
                                            target = data[i[1]][i[0]]
                                            best_dist = dist
                                            best_dir = d
                                        elif dist == best_dist:
                                            if target is None or target.y > i[1] or (target.y == i[1] and target.x > i[0]):
                                                target = data[i[1]][i[0]]
                                                best_dist = dist
                                                best_dir = d
                                        found = True
                                    elif data[i[1]][i[0]] == '.':
                                        n = get_neighbors(*i, explored)
                                        explored.extend(n)
                                        new_set.extend(n)
                                    elif data[i[1]][i[0]] == '#':
                                        explored.extend(i)
                                explore = new_set
                            d += 1
                        if best_dir != -1 and data[y + directions[best_dir][1]][x + directions[best_dir][0]] == '.':
                            current_entity.move(*directions[best_dir])
                            data[y][x] = '.'
                            data[current_entity.y][current_entity.x] = current_entity
                        target = None
                        for d in directions:
                            next_to = data[current_entity.y + d[1]][current_entity.x + d[0]]
                            if isinstance(next_to, Entity) and next_to.species != current_entity.species and next_to.hp > 0:
                                if target is None:
                                    target = next_to
                                elif target.hp > next_to.hp:
                                    target = next_to
                        if target is not None:
                            current_entity.attack(target)
                            if target.hp <= 0:
                                data[target.y][target.x] = '.'
        remove = []
        for i in goblins:
            i.moved = False
            if i.hp <= 0:
                remove.append(i)
        for i in remove:
            goblins.remove(i)
        remove = []
        for i in elves:
            i.moved = False
            if i.hp <= 0:
                remove.append(i)
        if keep_alive and len(remove) > 0:
            return False
        for i in remove:
            elves.remove(i)
        rounds += 1
    return rounds - 1


reset()
r = func()
print("part_1:", r * sum([i.hp for i in goblins]))
base = 4
while True:
    goblins = []
    elves = []
    reset(attack=base)
    r = func(keep_alive=True)
    base += 1
    if r:
        break
print("part_2:", r * sum([i.hp for i in elves]))
