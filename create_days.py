from pathlib import Path
from datetime import date
import aoc_helper

def template() -> str:
    with open('template.py') as template:
        return template.read()

def all_inputs():
    for i in range(2015, 2021):
        Path(f'{i}').mkdir(parents=True, exist_ok=True)
        for j in range(1, 26):
            with open(f'{i}/day{j}.py', mode='a+') as py:
                if Path(f'{i}/day{j}.py').stat().st_size == 0:
                    py.write(template().replace('{day}', str(j)))
            with open(f'{i}/day{j}_input.txt', mode='a+') as txt:
                if Path(f'{i}/day{j}_input.txt').stat().st_size == 0:
                    txt.write(aoc_helper.fetch(j, i))


def get_today():
    # needs to be fixed for other timezones
    today = date.today()
    d, m, y = today.day, today.month, today.year
    if m == 12:
        with open(f'{y}/day{d}.py', mode='a+') as py:
            if Path(f'{y}/day{d}.py').stat().st_size == 0:
                py.write(template().replace('{day}', str(d)))
        with open(f'{y}/day{d}_input.txt', mode='w') as txt:
            txt.write(aoc_helper.fetch(d, y))
        return
    print('no AOC for today')

if __name__ == '__main__':
    get_today()
