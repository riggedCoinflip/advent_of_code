import itertools
from more_itertools import windowed, peekable


with open(f'day10_input.txt') as f:
    raw_entries = [0, *[int(line.rstrip()) for line in f]]
    entries = sorted(raw_entries)

def part1(entries):
    print(entries)
    jolt_differences = [0, 0, 0]
    for current, next_ in windowed(entries, 2):
        difference = next_ - current
        if difference <= 3:
            jolt_differences[difference-1] += 1
        else:
            break
    return jolt_differences[0] * jolt_differences[2]

def part2(entries):
    entries = [[x, 0] for x in entries]
    entries[0][1] = 1
    for i, entry in enumerate(entries):
        jolt, paths = entry
        for next_i, next_ in enumerate(entries[i+1:(i+1) + 3 + 1]):
            jolt2, paths2 = next_
            if jolt + 3 >= jolt2:
                entries[(i+1)+next_i][1] += paths
            else:
                break
    print(entries)
    return entries[-1][1]


def part2_bigbrain(numbers: set, allowed_step_size: int = 3):
    '''
    doesnt use sort, doesnt use max. space complexity of O(n), n=allowed_step_size.
    :param numbers:
    :param allowed_step_size:
    :return:
    '''
    cache = [1] + [0] * allowed_step_size

    for i in itertools.count(0):
        if cache[i % len(cache)] is 0:  # number doesnt exist, skip it
            continue
        break_flag = True
        for step in range(1,4):
            if i + step in numbers:
                break_flag = False
                cache[(i + step) % len(cache)] += cache[i % len(cache)]

        if break_flag: #return the cache
            return cache[i % 4]
        else: #clear the cache
            cache[i % 4] = 0


def yield_all_possible_paths(entries):
    #might take a very long time
    def rec(i=0, jolt=0, path=[0]):
        #print(f'{i=}, {jolt=}, {path=}')
        possible_paths = peekable(entries[i+1:])

        empty_generator = True
        for j, possible_path in enumerate(possible_paths):
            empty_generator = False
            #print(f'{j=}, {possible_path=}')
            if possible_path <= jolt + 3:
                #print('works')
                yield from rec(i + j + 1, possible_path, [*path, possible_path])
            else:
                #print('doesnt')
                break
        if empty_generator:
            yield path
    yield from rec()


if __name__ == '__main__':
    part2_bigbrain(set(raw_entries))
    #print(part2(entries))
