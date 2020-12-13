import math
from sympy.ntheory.modular import crt

with open(f'day13_input.txt') as f:
    entries = [line.rstrip() for line in f]
    #timestamp = int(entries[0])
    busses = entries[1].split(',')

def part1(timestamp, busses):
    till_arrival = {}
    for bus in busses:
        if bus != 'x':
            bus = int(bus)
            till_arrival[bus] = bus - (timestamp % bus)
    earliest_bus = (min(till_arrival.items(), key=lambda x: x[1]))
    return math.prod(earliest_bus)

def part2(busses):
    coprimes = []
    modulos = []
    for i, bus in enumerate(busses):
        if bus != 'x':
            coprimes.append(int(bus))
            modulos.append(i)
    a, b = crt(coprimes, modulos)
    return b - a

if __name__ == '__main__':
    print(part2(busses))

