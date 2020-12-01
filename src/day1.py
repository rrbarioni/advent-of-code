def solve_part1(entries):
    '''
    Given a list of integer values, what is the product of the two values whose
        sum is equal to 2020?
    '''
    d = { e: None for e in entries }

    for e in entries:
        if (2020 - e) in entries:
            prod = e * (2020 - e)

            return prod

def solve_part2(entries):
    '''
    Given a list of integer values, what is the product of the three values 
        whose sum is equal to 2020?
    '''
    d = { e: None for e in entries }

    for i in range(len(entries)):
        e_i = entries[i]
        for j in range(i+1, len(entries)):
            e_j = entries[j]
            if (2020 - e_i - e_j) in d:
                prod = e_i * e_j * (2020 - e_i - e_j)

                return prod

if __name__ == '__main__':
    entries = list(open('inputs/day1.txt'))
    entries = [int(e) for e in entries]

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
