# Day 5
INPUT = open('Day 05.txt', 'r')
text = INPUT.read().strip()
data = list(text)


def get_len(data):
    while True:
        remove = []
        for i in range(len(data) - 1):
            if i in remove:
                continue
            if data[i].upper() == data[i + 1].upper() and data[i] != data[i + 1]:
                remove.append(i)
                remove.append(i + 1)
        remove.reverse()
        for i in remove:
            data.pop(i)
        if len(remove) == 0:
            break
    return len(data)


def remove_letter(data, letter):
    while letter in data:
        data.remove(letter)
    while letter.upper() in data:
        data.remove(letter.upper())
    return data


print("part_1:", get_len(data.copy()))
letters = set(text.lower())
lengths = []
for i in letters:
    lengths.append(get_len(remove_letter(data.copy(), i)))
print("part_2:", min(lengths))
INPUT.close()
