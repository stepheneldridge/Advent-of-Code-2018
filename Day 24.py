# Day 24
import re


def parse(boost=0):
    INPUT = open("Day 24.txt", 'r')
    immune = []
    infection = []
    which = None
    for line in INPUT:
        if line == '\n':
            continue
        if line.startswith('Immune'):
            which = 0
            continue
        elif line.startswith('Infection'):
            which = 1
            continue
        nums = re.findall(r'\d+', line)
        nums = list(map(int, nums))
        weak = re.search(r'(?<=weak to )(?:(\w+)(?:, )?)+(?=\)|\;)', line)
        if weak:
            weak = tuple(weak.group(0).split(', '))
        else:
            weak = tuple()
        immune_to = re.search(r'(?<=immune to )(?:(\w+)(?:, )?)+(?=\)|\;)', line)
        if immune_to:
            immune_to = tuple(immune_to.group(0).split(', '))
        else:
            immune_to = tuple()
        atktype = re.search(r'\w+(?= damage)', line)
        cell = {
            'type': which,
            'units': nums[0],
            'hp': nums[1],
            'attack': nums[2],
            'init': nums[3],
            'immune': immune_to,
            'weak': weak,
            'atktype': atktype.group(0)
        }
        if which == 0:
            cell['attack'] += boost
            immune.append(cell)
        elif which == 1:
            infection.append(cell)
    return immune, infection


def power(cell):
    return cell['units'] * cell['attack']


def better_target(a, b):
    if a is None:
            return b
    else:
        if power(a) < power(b):
            return b
        elif power(a) == power(b):
            if a['init'] < b['init']:
                return b
    return a


def find_target(cell, targets, used):
    target = None
    damage = 0
    p = power(cell)
    for i in targets:
        if i in used:
            continue
        if cell['atktype'] in i['immune']:
            continue
        elif cell['atktype'] in i['weak']:
            if p * 2 > damage:
                target = i
                damage = p * 2
            elif p * 2 == damage:
                target = better_target(target, i)
        else:
            if p > damage:
                target = i
                damage = p
            elif p == damage:
                target = better_target(target, i)
    return target


boost = 0
lower, upper = 0, 2048
unit_count = 0
while True:
    immune, infection = parse(boost)
    while len(immune) > 0 and len(infection) > 0:
        # target selection
        everything = immune + infection
        attacked = []
        attacks = []
        everything.sort(key=lambda cell: power(cell) * 100 + cell['init'], reverse=True)
        for cell in everything:
            if cell['type'] == 0:
                target = find_target(cell, infection, attacked)
                if target:
                    attacked.append(target)
                    attacks.append((cell, target))
            elif cell['type'] == 1:
                target = find_target(cell, immune, attacked)
                if target:
                    attacked.append(target)
                    attacks.append((cell, target))
        # attack
        attacks.sort(key=lambda pair: pair[0]['init'], reverse=True)
        for cell, target in attacks:
            if cell['units'] <= 0 or target['units'] <= 0:
                continue
            p = power(cell)
            if cell['atktype'] in target['immune']:
                p = 0
            elif cell['atktype'] in target['weak']:
                p *= 2
            target['units'] -= p // target['hp']
            if target['units'] <= 0:
                if target['type'] == 0:
                    immune.remove(target)
                elif target['type'] == 1:
                    infection.remove(target)
        new_count = sum(i['units'] for i in everything)
        if new_count == unit_count:
            break
        unit_count = new_count
    if boost == 0:
        print("part_1:", sum(i['units'] for i in infection))
        boost = (upper + lower) // 2
    else:
        if len(immune) > 0 and len(infection) == 0:
            if boost == lower:
                break
            upper = boost
        elif len(infection) > 0:
            if lower == boost:
                boost += 1
            lower = boost
        boost = (upper + lower) // 2
print("part_2:", sum(i['units'] for i in immune))
