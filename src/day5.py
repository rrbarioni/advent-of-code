def solve_part1(entries):
    entries = [e.rstrip() for e in entries]

    max_id = 0

    for e in entries:
        r_s, c_s = e[:7], e[7:]

        r_s = r_s.replace('F', '0').replace('B', '1')
        c_s = c_s.replace('L', '0').replace('R', '1')

        r = int(r_s, 2)
        c = int(c_s, 2)

        curr_id = r * 8 + c

        max_id = max(max_id, curr_id)

    return max_id

def solve_part2(entries):    
    entries = [e.rstrip() for e in entries]

    ids = {}
    min_id = float('inf')
    max_id = 0

    for e in entries:
        r_s, c_s = e[:7], e[7:]

        r_s = r_s.replace('F', '0').replace('B', '1')
        c_s = c_s.replace('L', '0').replace('R', '1')

        r = int(r_s, 2)
        c = int(c_s, 2)

        curr_id = r * 8 + c

        ids[curr_id] = None

        min_id = min(min_id, curr_id)
        max_id = max(max_id, curr_id)

    for curr_id in range(min_id, max_id + 1):
        if curr_id not in ids:
            your_id = curr_id

            return your_id

if __name__ == '__main__':
    entries = open('inputs/day5.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
