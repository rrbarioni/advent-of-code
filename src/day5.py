def solve_part1(entries):
    entries = [e.rstrip() for e in entries]

    max_id = 0

    for e in entries:
        e = e.translate(str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'}))
        curr_id = int(e, 2)

        max_id = max(max_id, curr_id)

    return max_id

def solve_part2(entries):    
    entries = [e.rstrip() for e in entries]

    ids = {}
    min_id = float('inf')
    max_id = 0

    for e in entries:
        e = e.translate(str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'}))
        curr_id = int(e, 2)

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
