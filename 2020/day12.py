import turtle

with open(f'day12_input.txt') as f:
    entries = [line.rstrip() for line in f]
    entries = [(entry[0], int(entry[1:])) for entry in entries]

def part_1(entries):
    x, y = 0, 0
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    current_dir = 0

    for instruction, value in entries:
        if instruction == 'R':
            value = int(value / 90)
            current_dir = (current_dir + value) % len(direction)
        elif instruction == 'L':
            value = int(value / 90)
            current_dir = (current_dir - value) % len(direction)
        elif instruction == 'F':
            x += value * direction[current_dir][0]
            y += value * direction[current_dir][1]
        elif instruction == 'E':
            x += value
        elif instruction == 'W':
            x -= value
        elif instruction == 'N':
            y += value
        elif instruction == 'S':
            y -= value
    print(x,y)
    return abs(x) + abs(y)

def part_2(entries):
    ship_x, ship_y = 0, 0
    wp_x, wp_y = 10, 1

    for instruction, value in entries:
        if instruction == 'R':
            rotations = int(value / 90)
            for _ in range(rotations):
                wp_x, wp_y = wp_y, -wp_x
        elif instruction == 'L':
            rotations = int(value / 90)
            for _ in range(rotations):
                wp_x, wp_y = -wp_y, wp_x
        elif instruction == 'F':
            ship_x += value * wp_x
            ship_y += value * wp_y
        elif instruction == 'E':
            wp_x += value
        elif instruction == 'W':
            wp_x -= value
        elif instruction == 'N':
            wp_y += value
        elif instruction == 'S':
            wp_y -= value
    print(ship_x, ship_y)
    return abs(ship_x) + abs(ship_y)

def part_1_turtle():
    turtle.speed(0)
    turtle.right(90)
    for instruction, value in entries:
        if instruction == 'L':
            turtle.left(value)
        if instruction == 'R':
            turtle.right(value)
        if instruction == 'F':
            turtle.forward(value)

        (x, y) = turtle.pos()
        if instruction == 'N':
            turtle.sety(y + value)
        if instruction == 'S':
            turtle.sety(y - value)
        if instruction == 'E':
            turtle.setx(x + value)
        if instruction == 'W':
            turtle.setx(x - value)
    x, y = turtle.pos()
    print(x, y)
    return abs(x) + abs(y)

if __name__ == '__main__':
    print(part_2(entries))
    #turtle.done()
