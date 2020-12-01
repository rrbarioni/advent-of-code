def solve_part1(entries):
    '''
    Given a list of integer values, what is the product of the two values whose
        sum is equal to 2020?
    '''
    for i in range(len(entries)):
        e_i = entries[i]
        for j in range(i+1, len(entries)):
            e_j = entries[j]
            if (e_i + e_j == 2020):
                prod = e_i * e_j

                return prod

def solve_part2(entries):
    '''
    Given a list of integer values, what is the product of the three values 
        whose sum is equal to 2020?
    '''
    for i in range(len(entries)):
        e_i = entries[i]
        for j in range(i+1, len(entries)):
            e_j = entries[j]
            for k in range(j+1, len(entries)):
                e_k = entries[k]
                if (e_i + e_j + e_k == 2020):
                    prod = e_i * e_j * e_k

                    return prod

if __name__ == '__main__':
    entries = list(open('inputs/day1.txt'))
    entries = [int(e) for e in entries]

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
