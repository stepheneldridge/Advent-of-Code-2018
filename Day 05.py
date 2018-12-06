# Day 5
INPUT = open('Day 05.txt', 'r')
text = INPUT.read().strip()
data = list(map(ord, text))


def get_len(data):
    i = 0
    popped = False
    while True:
        if data[i] ^ data[i + 1] == 32:
            data.pop(i + 1)
            data.pop(i)
            popped = True
        else:
            i += 1
        if i == len(data) - 1:
            if popped:
                i = 0
                popped = False
            else:
                break
    return len(data)


def remove_letter(data, letter):
    while letter in data:
        data.remove(letter)
    while (letter + 32) in data:
        data.remove(letter + 32)
    return data


print("part_1:", get_len(data.copy()))

letters = set(map(ord, text.upper()))
lengths = []
for i in letters:
    lengths.append(get_len(remove_letter(data.copy(), i)))
print("part_2:", min(lengths))
INPUT.close()
