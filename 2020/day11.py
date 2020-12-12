from itertools import product, count
from collections import Counter
import numpy as np
import abc
import time
import click  # used for system

with open(f'day11_input.txt') as f:
    entries = [list(line.rstrip()) for line in f]
    entries = np.array([x for x in entries])


class LikeGameOfLife:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        return '\n'.join([''.join(column) for column in self.grid])

    def __repr__(self):
        return str(self.grid)

    def __eq__(self, other):
        if isinstance(other, LikeGameOfLife):
            return np.array_equal(self.grid, other.grid)
        else:
            return NotImplemented

    def __iter__(self):
        current = self
        while True:
            yield current
            current = next(current)

    def __next__(self):
        next_grid = np.empty_like(self.grid)
        d1, d2 = np.shape(self.grid)
        for x, y in product(range(d1), range(d2)):
            next_grid[x][y] = self.elem_next(x, y)
        return self.__class__(grid=next_grid)

    def start(self):
        current = self
        try:
            while True:
                print(current)
                next_ = next(current)
                if current == next_:
                    print('found stabilized')
                    print(current)
                    return current
                else:
                    current = next_
                    time.sleep(0.2)
                    click.clear()
        except KeyboardInterrupt:
            return current

    def neighbors_relative_index(self, x, y):
        indices = set()
        for a, b in product([-1, 0, 1], [-1, 0, 1]):
            if a == b == 0:
                continue
            else:
                indices.add((a, b))
        return indices

    def neighbors(self, x, y, looping=False):
        (max_x, max_y) = np.shape(self.grid)
        neighbors_ = []
        for (a, b) in self.neighbors_relative_index(x, y):
            if not looping:
                if 0 <= x + a < max_x and 0 <= y + b < max_y:
                    neighbors_.append(self.grid[x + a][y + b])
                else:
                    continue
            else:
                neighbors_.append(self.grid[x + a % max_x][y + b % max_y])
        return neighbors_

    def counter_neighbors(self, x, y, looping=False):
        return Counter(self.neighbors(x, y, looping))

    def stabilizes(self, maxiter=1000):
        current = None
        for i, next_ in enumerate(self):
            if i >= maxiter:
                return None, -1
            elif current == next_:
                return current, i
            else:
                current = next_

    @abc.abstractmethod
    def elem_next(self, x, y):
        return


class GameOfLife(LikeGameOfLife):
    def __str__(self):
        columns = np.where(self.grid == True, '▉', ' ')
        return '\n'.join([''.join(column) for column in columns])

    def elem_next(self, x, y):
        alive = self.grid[x][y]
        counter_ = self.counter_neighbors(x, y)
        if alive:
            return True if 2 <= counter_[True] <= 3 else False
        else:
            return True if counter_[True] == 3 else False


class BeachKing(LikeGameOfLife):
    def elem_next(self, x, y):
        seat = self.grid[x][y]
        counter_ = self.counter_neighbors(x, y)

        if seat == 'L':
            return '#' if counter_['#'] == 0 else 'L'
        elif seat == '#':
            return '#' if counter_['#'] < 4 else 'L'
        else:  # seat == '.'
            return seat

    def count_occupied(self):
        return np.count_nonzero(self.grid == '#')


class BeachQueen(BeachKing):
    def neighbors(self, x, y, looping=False):
        (max_x, max_y) = np.shape(self.grid)
        neighbors_ = []
        for (a, b) in self.neighbors_relative_index(x, y):
            for mult in count(1):
                x2, y2 = x + a * mult, y + b * mult
                if not looping:
                    if 0 <= x2 < max_x and 0 <= y2 < max_y:
                        seat = self.grid[x2][y2]
                    else:
                        break
                else:
                    seat = self.grid[x2 % max_x][y2 % max_y]

                if seat == '.':
                    continue
                else:
                    neighbors_.append(seat)
                    break
        return neighbors_

    def elem_next(self, x, y):
        seat = self.grid[x][y]
        counter_ = self.counter_neighbors(x, y)

        if seat == 'L':
            return '#' if counter_['#'] == 0 else 'L'
        elif seat == '#':
            return '#' if counter_['#'] < 5 else 'L'
        else:  # seat == '.'
            return seat


if __name__ == '__main__':
    b = BeachQueen(entries)
    end, i = b.stabilizes()

    print(end.count_occupied())

# TODO visualization with curses