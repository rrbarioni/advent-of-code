def solve_part1(entries):
    '''
    Given a list of (string, char, interval), how many strings contains
        the amount of char within the interval?
    '''
    n_valid = 0

    for e in entries:
        # entry is in the format "2-6 c: fcpwjqhcgtffzlbj"
        expected_count, c, password = e.split(' ')
        min_count, max_count = expected_count.split('-')
        min_count = int(min_count)
        max_count = int(max_count)
        c = c[0]
        password = password.rstrip()

        count = password.count(c)
        if count >= min_count and count <= max_count:
            n_valid += 1

    return n_valid

def solve_part2(entries):
    '''
    Given a list of (string, char, index 1, index 2), how many string contain
        the char in only one of the indexes? (considering that the index starts
        at 1)?
    '''
    n_valid = 0

    for e in entries:
        # entry is in the format "2-6 c: fcpwjqhcgtffzlbj"
        expected_indexes, c, password = e.split(' ')
        index_i, index_j = expected_indexes.split('-')
        index_i = int(index_i) - 1
        index_j = int(index_j) - 1
        c = c[0]
        password = password.rstrip()

        p_index_i = password[index_i]
        p_index_j = password[index_j]

        i_c = p_index_i == c
        j_c = p_index_j == c

        if (i_c and not j_c) or (not i_c and j_c):
            n_valid += 1

    return n_valid

if __name__ == '__main__':
    entries = open('inputs/day2.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
