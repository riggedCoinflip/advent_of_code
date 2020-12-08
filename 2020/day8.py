with open(f'day8_input.txt') as f:
    entries = [line.strip() for line in f]

def part1(instructions):
    acc = 0
    path = set()
    i = 0
    while i not in path:
        path.add(i)
        print(instructions[i])
        instruction, value = instructions[i].split()
        value = int(value)
        print(f'{i=}, {instruction=}, {value=}')

        if instruction == 'jmp':
            i += value
            continue
        else:
            i += 1
            if instruction == 'acc':
                acc += value
            elif instruction == 'nop':
                pass
            else:
                raise ValueError(f'{instruction=} not recognized')
    return acc

def part1_rec(instructions):
    def step(acc=0, path = [], i=0):
        if i not in path:
            path.append(i)
            instruction, value = instructions[i].split()
            value = int(value)
            print(f'{i=}, {instruction=}, {value=}')

            if instruction == 'jmp':
                return step(acc, [*path, i], i + value)
            elif instruction == 'acc':
                return step(acc + value, [*path, i], i + 1)
            elif instruction == 'nop':
                return step(acc, [*path, i], i + 1)
            else:
                raise ValueError(f'{instruction=} not recognized')
        else:
            return acc
    return step()

def part2(instructions):
    def step(acc=[0], path = [0], mode='forward'):
        i = path[-1]
        curr_acc = acc[-1]
        if i >= len(instructions):
            return curr_acc
        elif i not in path[:-1]:
            instruction, value = instructions[i].split()
            value = int(value)
            print(f'{i=}, {instruction=}, {value=}')

            if mode == 'backward': #inverse
                mode = 'forward_debug' # we only want to inverse this instruction
                if instruction == 'acc':
                    #wont change anything so wont solve the problem
                    return
                elif instruction == 'jmp':
                    instruction = 'nop'
                elif instruction == 'nop':
                    instruction = 'jmp'

            if instruction == 'jmp':
                return step([*acc, curr_acc], [*path, i + value], mode)
            elif instruction == 'acc':
                return step([*acc, curr_acc + value], [*path, i + 1], mode)
            elif instruction == 'nop':
                return step([*acc, curr_acc], [*path, i + 1], mode)
            else:
                raise ValueError(f'{instruction=} not recognized')
        elif mode == 'forward':
            for j in range(len(path), 0, -1):
                debug = step(acc[:j], path[:j], 'backward')
                if debug:
                    return debug
            else:
                return "Couldn't debug"
        else:
            print("debug didn't work")
            return
    return step()

if __name__ == '__main__':
    print(part2(entries))