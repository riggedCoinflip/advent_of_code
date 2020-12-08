with open(f'day5_input.txt') as f:
    entries = [line.strip() for line in f]

def get_seatid(entry):
    return int(''.join('0' if x in 'FL' else '1' for x in entry), 2)

def part1(entries):
    return max(get_seatid(entry) for entry in entries)

def part2(entries):
    seats = set(get_seatid(entry) for entry in entries)
    sum_occupied = sum(seats)
    min_ = min(seats)
    max_ = max(seats)
    checksum = (max_ * (max_ + 1) - (min_ - 1) * min_) / 2
    return checksum - sum_occupied

p1_lambda = lambda entries: max(get_seatid(entry) for entry in entries)


if __name__ == '__main__':
    print(part2(entries))