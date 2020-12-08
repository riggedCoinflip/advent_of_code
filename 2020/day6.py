with open(f'day6_input.txt') as f:
    entries = f.read().split('\n\n')

def part1(entries):
    return sum(len(set(''.join(entry.split()))) for entry in entries)

def part2(entries):
    count = 0
    for entry in entries:
        passenger = [set(passenger) for passenger in entry.split()]
        count += len(passenger[0].intersection(*passenger[1:]))
    return count

if __name__ == '__main__':
    print(part2(entries))
