# Day 21
seen = set()
answer = 0
r3 = 7041048
r4 = 65536
answer = 0
while True:
    r3 += r4 & 255
    r3 &= 16777215
    r3 = (r3 * 65899) & 16777215
    if 256 > r4:
        if len(seen) == 0:
            print("part_1:", r3)
        if r3 in seen:
            break
        answer = r3
        seen.add(r3)
        r4 = r3 | 65536
        r3 = 7041048
    else:
        r4 //= 256
print("part_2:", answer)
