def solve_part1(entries):
    entries = [e.rstrip() for e in entries]

    commands = [(e[0], int(e[1:])) for e in entries]

    print(commands[0])

    x, y = [0, 0]

    orientations = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    orientation_i = 1

    for action, value in commands:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            turns = round(value / 90)
            orientation_i = (orientation_i - turns) % 4
        elif action == 'R':
            turns = round(value / 90)
            orientation_i = (orientation_i + turns) % 4
        elif action == 'F':
            x += (orientations[orientation_i][0] * value)
            y += (orientations[orientation_i][1] * value)

    result = abs(x) + abs(y)

    return result

def solve_part2(entries):
    return

if __name__ == '__main__':
    entries = open('inputs/day12.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    # print('part 2: %s' % solve_part2(entries))
