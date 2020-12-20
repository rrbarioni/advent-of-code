def solve_part1(entries):
    entries = [e.rstrip() for e in entries]

    commands = [(e[0], int(e[1:])) for e in entries]

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
    entries = [e.rstrip() for e in entries]

    commands = [(e[0], int(e[1:])) for e in entries]

    w_x, w_y = [10, 1]
    s_x, s_y = [0, 0]

    for action, value in commands:
        if action == 'N':
            w_y += value
        elif action == 'S':
            w_y -= value
        elif action == 'E':
            w_x += value
        elif action == 'W':
            w_x -= value
        elif action == 'L':
            turns = round(value / 90)
            for _ in range(turns):
                w_aux = w_x
                w_x = -w_y
                w_y = w_aux
        elif action == 'R':
            turns = round(value / 90)
            for _ in range(turns):
                w_aux = w_x
                w_x = w_y
                w_y = -w_aux
        elif action == 'F':
            s_x += (w_x * value)
            s_y += (w_y * value)

    result = abs(s_x) + abs(s_y)

    return result

if __name__ == '__main__':
    entries = open('inputs/day12.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
