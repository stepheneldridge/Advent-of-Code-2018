# Day 16
import re
INPUT = open('Day 16.txt', 'r')
data = []
index = 0
entry = 0


def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]
    return reg


def addi(reg, a, b, c):
    reg[c] = reg[a] + b
    return reg


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]
    return reg


def muli(reg, a, b, c):
    reg[c] = reg[a] * b
    return reg


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]
    return reg


def bani(reg, a, b, c):
    reg[c] = reg[a] & b
    return reg


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]
    return reg


def bori(reg, a, b, c):
    reg[c] = reg[a] | b
    return reg


def setr(reg, a, b, c):
    reg[c] = reg[a]
    return reg


def seti(reg, a, b, c):
    reg[c] = a
    return reg


def gtir(reg, a, b, c):
    reg[c] = 1 if a > reg[b] else 0
    return reg


def gtri(reg, a, b, c):
    reg[c] = 1 if reg[a] > b else 0
    return reg


def gtrr(reg, a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0
    return reg


def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0
    return reg


def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0
    return reg


def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0
    return reg


funcs = [addr, addi, mulr, muli, bani, banr, bori, borr, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
reg = [0, 0, 0, 0]
program = []
for line in INPUT:
    if index == 0 and line.startswith('Before'):
        data.append(list(map(int, re.findall(r'\d+', line))))
        index += 1
    elif index == 1 or index == 2:
        data[entry].extend(list(map(int, re.findall(r'\d+', line))))
        index += 1
    elif index == 3 and line == '\n':
        entry += 1
        index = 0
    elif index == 0 and line == '\n':
        index = 10
    elif index == 10 and line != '\n':
        program.append(list(map(int, re.findall(r'\d+', line))))

over = 0
op_codes = {}
for i in data:
    matches = 0
    ops = set()
    for j in funcs:
        if j(i[0:4], i[5], i[6], i[7]) == i[8:]:
            matches += 1
            ops.add(j)
    if matches >= 3:
        over += 1
    if i[4] in op_codes:
        op_codes[i[4]] = op_codes[i[4]].intersection(ops)
    else:
        op_codes[i[4]] = ops
used = set()
correct_ops = {}
while len(used) < 16:
    for i in op_codes:
        if len(op_codes[i] - used) == 1:
            correct_ops[i] = (op_codes[i] - used).pop()
            used.add(correct_ops[i])
for i in program:
    reg = correct_ops[i[0]](reg, i[1], i[2], i[3])
print("part_1:", over)
print("part_2:", reg[0])
INPUT.close()
