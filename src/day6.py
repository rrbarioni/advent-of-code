def solve_part1(entries):
    entries = [e.rstrip() if e != '\n' else ' ' for e in entries]
    entries = ''.join(entries).split(' ')

    sum_n_q = 0
    for e in entries:
        qs = {}
        for q in e:
            if q not in qs:
                qs[q] = None
        n_q = len(qs)

        sum_n_q += n_q

    return sum_n_q

def solve_part2(entries):
    entries = [e.rstrip() if e != '\n' else ' ' for e in entries]

    sep_entries = []
    curr_entry = []
    for e in entries:
        if e[0] != ' ':
            curr_entry.append(e)
        else:
            sep_entries.append(curr_entry)
            curr_entry = []
    sep_entries.append(curr_entry)

    total_all = 0
    for e in sep_entries:
        qs = {}
        for s in e:
            for c in s:
                if c not in qs:
                    qs[c] = 1
                else:
                    qs[c] += 1

        n_all = len([x for x in qs.values() if x == len(e)])
        total_all += n_all

    return total_all

if __name__ == '__main__':
    entries = open('inputs/day6.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
