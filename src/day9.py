def solve_part1(entries):
    entries = [int(e.rstrip()) for e in entries]

    for i in range((len(entries) - 1) - 25):
        j = i + 25

        preamble = set(entries[i:j])
        curr = entries[j]

        valid = False
        for p in preamble:
            if (curr - p) in preamble:
                valid = True

        if not valid:
            return curr

    return -1

def solve_part2(entries):
    entries = [int(e.rstrip()) for e in entries]

    for i in range((len(entries) - 1) - 25):
        j = i + 25

        preamble = set(entries[i:j])
        curr = entries[j]

        valid = False
        for p in preamble:
            if (curr - p) in preamble:
                valid = True

        if not valid:
            preamble_l = entries[i:j]

            for w_s in range(2, j + 1):
                for k in range(j - w_s):
                    w = entries[k:k + w_s]
                    
                    if sum(w) == curr:
                        weak = min(w) + max(w)

                        return weak

    return -1

if __name__ == '__main__':
    entries = open('inputs/day9.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))