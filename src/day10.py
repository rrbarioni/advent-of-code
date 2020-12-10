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

    graph = {}
    for a in s:
        graph[a] = []
        for n in range(1,4):
            if a + n in s:
                graph[a].append(a + n)

    d_split = [len(x) for x in graph.values()][:-1]
    d_split = ''.join([str(l) for l in d_split]).split('1')
    d_split = [[int(v) for v in l] for l in d_split if len(l) > 0]

    mults = [sum(d) - 1 if len(d) > 1 else d[0] for d in d_split]

    mult = 1
    for m in mults:
        mult *= m

    return mult

if __name__ == '__main__':
    entries = open('inputs/day10.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
