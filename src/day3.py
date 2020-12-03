def solve_part1(entries):
    w = len(entries[0])
    h = len(entries)

    n_trees = [entries[y][(3 * y) % w] for y in range(1, h)].count('#')

    return n_trees

def solve_part2(entries):
    w = len(entries[0])
    h = len(entries)

    rd_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    prod = 1
    for r, d in rd_list:
        enc = [entries[d * y][(r * y) % w] for y in range(1, h) if d * y < h]
        prod *= enc.count('#')

    return prod

if __name__ == '__main__':
    entries = open('inputs/day3.txt').readlines()
    entries = [e.rstrip() for e in entries]

    print('part1: %s' % solve_part1(entries))
    print('part2: %s' % solve_part2(entries))
