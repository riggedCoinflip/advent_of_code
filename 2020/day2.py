from collections import Counter

with open(f'day2_input.txt') as f:
    entries = frozenset(f.readlines())

def part_1(entries):
    count = 0;
    for entry in entries:
        entry = entry.split(':')

        password = entry[1].strip()
        c = Counter(password)

        rules = entry[0].split()
        char = rules[1]

        range_ = rules[0].split('-')
        min = int(range_[0])
        max = int(range_[1])

        if c[char]:
            if min <= c[char] <= max:
                print(entry)
                count += 1

    return count

def part_2(entries):
    count = 0;
    for entry in entries:
        entry = entry.split(':')

        password = entry[1].strip()

        rules = entry[0].split()
        char = rules[1]

        positions = rules[0].split('-')
        pos1 = int(positions[0]) - 1
        pos2 = int(positions[1]) - 1

        if (char == password[pos1]) ^ (char == password[pos2]):
            print(entry)
            count += 1

    return count



if __name__ == '__main__':
    a = [10, 20, 30]
    b = [10, 20, 30]
    print(*a)
    print(*b)
    #print(part_2(entries))