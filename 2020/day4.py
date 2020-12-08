with open(f'day4_input.txt') as f:
    entries = f.read().split('\n\n')

def part1(entries):
    return sum((part1_helper(entry) for entry in entries))

def part1_helper(entry):
    passport = dict(x.split(':') for x in entry.split())
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= passport.keys()

def part1_1line(entries):
    return sum({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= dict(x.split(':') for x in entry.split()).keys() for entry in entries)


def part2(entries):
    count = 0
    entry = ''
    for line in entries:
        if line and line != ' ':
            entry += line
        else:
            if part2_helper(entry):
                count += 1
            entry = ''
    if part2_helper(entry):
        count += 1
    return count


def part2_helper(entry):
    entry = entry.split()
    passport = dict((key, value) for key, value in (x.split(':') for x in entry))

    # print(passport)
    if {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= passport.keys():
        if not 1920 <= int(passport['byr']) <= 2002:
            return False

        if not 2010 <= int(passport['iyr']) <= 2020:
            return False

        if not 2020 <= int(passport['eyr']) <= 2030:
            return False

        hgt, unit = passport['hgt'][:-2], passport['hgt'][-2:]
        try:
            hgt = int(hgt)
        except ValueError:
            return False
        if unit == 'cm':
            if not 150 <= hgt <= 193:
                return False
        elif unit == 'in':
            if not 59 <= hgt <= 76:
                return False
        else:
            return False

        if not passport['hcl'][0] == '#':
            return False
        if not len(passport['hcl']) == 7:
            return False
        if not all(c in '0123456789abcdef' for c in (passport['hcl'][1:])):
            return False

        if not passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            return False

        if not len(passport['pid']) == 9:
            return False
        if not passport['pid'].isnumeric():
            return False
        print(f'valid: {passport}')
        return True
    else:
        print(f'invalid: {passport}')
        return False


if __name__ == '__main__':
    print(len(entries))
    print(part1_1line(entries))
