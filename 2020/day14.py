import re
from itertools import combinations

with open('day14_input.txt') as f:
    entries = [line.rstrip() for line in f]


def part1(entries):
    mem = {}
    mask = 'X' * 36
    for entry in entries:
        instruction, value = entry.split(' = ')
        if instruction.startswith('mask'):
            mask = value
        else:
            m = re.search('\[([^]]*)', instruction)
            memcell = int(m.group(1))
            value = f'{int(value):b}'
            value = value.zfill(36)
            output = ''.join(membit if maskbit == 'X' else maskbit for maskbit, membit in zip(mask, value))
            mem[memcell] = output

    return sum(int(v, 2) for _, v in mem.items())

def part2(entries):
    mem = {}
    mask = '0' * 36
    for entry in entries:
        instruction, value = entry.split(' = ')
        if instruction.startswith('mask'):
            mask = value
        else:
            value = f'{int(value):b}'
            value = value.zfill(36)

            m = re.search('\[([^]]*)', instruction)
            memcell = int(m.group(1))
            memcell = f'{int(memcell):b}'
            memcell = memcell.zfill(36)

            output = ''
            x_es = [2 ** int(i) for i, c in enumerate(mask[::-1]) if c == 'X']
            for i, (maskbit, membit) in enumerate(zip(mask, memcell)):
                if maskbit == '1':
                    output += '1'
                elif maskbit == 'X':
                    output += '0'
                else:
                    output += membit
            output = int(output, 2)
            for r in range(0, len(x_es) + 1):
                for item in combinations(x_es, r):
                    x_sum = sum(item)
                    mem[output + x_sum] = value

    return sum(int(v, 2) for _, v in mem.items())

if __name__ == '__main__':
    print(part2(entries))