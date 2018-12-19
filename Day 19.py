# Day 19
from math import sqrt
INPUT = open('Day 19.txt', 'r').read().split('\n')


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
func_names = ['addr', 'addi', 'mulr', 'muli', 'bani', 'banr', 'bori', 'borr', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']
reg = [0, 0, 0, 0, 0, 0]
program = []
pointer = None
for line in INPUT:
    if line == '':
        continue
    elif line.startswith('#ip'):
        pointer = int(line.split(' ')[1])
    else:
        data = line.split(' ')
        f = funcs[func_names.index(data[0])]
        program.append([f] + list(map(int, data[1:])))

while reg[pointer] < len(program):
    p = program[reg[pointer]]
    reg = p[0](reg, *p[1:])
    reg[pointer] += 1
print("part_1:", reg[0])
reg = [1, 0, 0, 0, 0, 0]
for _ in range(100):
    p = program[reg[pointer]]
    reg = p[0](reg, *p[1:])
    reg[pointer] += 1
value = 0
x = reg.index(max(reg))
for i in range(1, int(sqrt(reg[x]))):
    if reg[x] % i == 0:
        value += i + reg[x] // i
print("part_2:", value)
