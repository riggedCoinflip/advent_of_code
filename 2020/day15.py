with open('day15_input.txt') as f:
    entries = [int(number) for number in f.read().rstrip().split(',')]

def solution(entries, n=2020):
    spoken = entries[::-1]
    for i in range(len(spoken), n):
        if i % 100_000 == 0:
            print(i)
        try:
            spoken.insert(0, spoken[1:].index(spoken[0]) + 1)
        except ValueError:
            spoken.insert(0, 0)
    print(spoken[::-1])
    return spoken[0]

def solution2(entries, n=2020):
    spoken = {}
    for i, elem in enumerate(entries[:-1]):
        spoken[elem] = i
    to_add = entries[-1]
    for i in range(len(spoken), n - 1):
        if to_add in spoken:
            tmp = i - spoken[to_add]
            spoken[to_add] = i
            to_add = tmp
        else:
            spoken[to_add] = i
            to_add = 0
    return to_add

if __name__ == '__main__':
    print(solution2(entries, 30000000))
