def solve_part1(entries):
    entries = [e.rstrip() for e in entries]

    instructions = [e.split(' ') for e in entries]
    instructions = [(c, int(v)) for (c, v) in instructions]

    visited = set()
    accumulator = 0
    p = 0
    while True:
        if p in visited:
            break
        visited.add(p)
        c, v = instructions[p]
        if c == 'nop':
            p += 1
        elif c == 'acc':
            accumulator += v
            p += 1
        elif c == 'jmp':
            p += v

    return accumulator

def solve_part2(entries):
    entries = [e.rstrip() for e in entries]

    ins = [e.split(' ') for e in entries]
    ins = [[c, int(v)] for (c, v) in ins]

    visited = set()
    p = 0
    while True:
        if p in visited:
            break
        visited.add(p)
        c, v = ins[p]

        if c == 'nop':
            p += 1
        elif c == 'acc':
            p += 1
        elif c == 'jmp':
            p += v

    possible_causes = visited

    for pc in possible_causes:
        c, _ = ins[pc]
        if c == 'nop':
            ins[pc][0] = 'jmp'
        elif c == 'jmp':
            ins[pc][0] = 'nop'
        else:
            continue

        curr_visited = set()
        accumulator = 0
        p = 0
        while p < len(ins):
            if p in curr_visited:
                break
            curr_visited.add(p)
            c, v = ins[p]

            if c == 'nop':
                p += 1
            elif c == 'acc':
                p += 1
                accumulator += v
            elif c == 'jmp':
                p += v

        if p >= len(ins):
            return accumulator

        else:
            c, _ = ins[pc]
            if c == 'nop':
                ins[pc][0] = 'jmp'
            elif c == 'jmp':
                ins[pc][0] = 'nop'

    return -1

if __name__ == '__main__':
    entries = open('inputs/day8.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
    