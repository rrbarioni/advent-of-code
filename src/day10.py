def solve_part1(entries):
    entries = [int(e.rstrip()) for e in entries]

    entries = sorted(entries)
    diff = [entries[i+1] - entries[i] for i in range(len(entries) - 1)]

    diffs = [0, diff.count(1), 0, diff.count(3) + 1]
    if entries[0] < 4:
        diffs[entries[0]] += 1

    result = diffs[1] * diffs[3]

    return result

def solve_part2(entries):
    entries = [int(e.rstrip()) for e in entries]

    s = set(entries)
    s.add(0)

    neigh = [len([n for n in [1,2,3] if a + n in s]) for a in s][:-1]
    neigh = ''.join([str(l) for l in neigh]).split('1')

    neigh = [[int(v) for v in l] for l in neigh if len(l) > 0]
    mults = [sum(n) - 1 if len(n) > 1 else n[0] for n in neigh]

    mult = 1
    for m in mults:
        mult *= m

    return mult

if __name__ == '__main__':
    entries = open('inputs/day10.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
