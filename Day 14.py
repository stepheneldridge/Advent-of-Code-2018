# Day 14
INPUT = 637061
key = [6, 3, 7, 0, 6, 1]
scores = [3, 7]
elves = [0, 1]
state = 0


def change(k, state):
    if k == 6:
        if state == 4:
            state += 1
        else:
            state = 1
    elif k in key:
        if state == key.index(k):
            state += 1
        else:
            state = 0
    else:
        state = 0
    return state


x = len(scores)
while state < 6:
    if x == INPUT + 10:
        print("part_1:", "".join(map(str, scores[-10:])))
    new_score = 0
    for i in elves:
        new_score += scores[i]
    if new_score >= 10:
        x += 1
        scores.append(1)
        if state == 5:
            break
        else:
            state = 0
        scores.append(new_score - 10)
    else:
        scores.append(new_score)
    state = change(scores[-1], state)
    for i in range(len(elves)):
        elves[i] = (elves[i] + scores[elves[i]] + 1) % len(scores)
    x += 1
print("part_2:", len(scores) - len(key))
