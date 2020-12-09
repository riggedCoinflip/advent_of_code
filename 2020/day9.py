from itertools import combinations

with open(f'day9_input.txt') as f:
    entries = [int(line.strip()) for line in f]


def part1(entries, n= 25):
    last_n = lambda x, y: x[-y:]
    for i, entry in enumerate(entries[n:]):
        possible_tuples = combinations(last_n(entries[:n + i], n), 2)
        possible_sums = (sum(comb) for comb in possible_tuples)
        for possible_sum in possible_sums:
            if entry == possible_sum:
                break
        else:
            return entry

def part2(entries):
    invalid_number = part1(entries)
    for i, first in enumerate(entries):
        tempsum = first
        for j, inner in enumerate(entries[i+1:]):
            tempsum += inner
            # contiguous set has to have at least 2 numbers, so only check after adding 2nd elem
            if tempsum == invalid_number:
                contiguous_set = entries[i:i+1+j+1] #+1 to keep last element
                return min(contiguous_set) + max(contiguous_set)
            elif tempsum > invalid_number:
                break


if __name__ == '__main__':
    a = [1,1,2]
    print([c for c in combinations(a, 2)])
    print(part2(entries))

