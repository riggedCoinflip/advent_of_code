from itertools import combinations

with open(f'day1_input.txt') as f:
    entries = {int(line.strip()) for line in f}

def part_1(entries:list[int]) -> int:
    for x, y in combinations(entries, r=2):
        if x + y == 2020:
            return(x * y)

def part_2(entries:list[int]) -> int:
    for x, y, z in combinations(entries, r=3):
        if x + y + z == 2020:
            print(x, y, z)
            return(x * y * z)

if __name__ == '__main__':
    print(part_2(entries))
