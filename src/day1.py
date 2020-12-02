def solve_part1(entries):
    '''
    Given a list of integer values, what is the product of the two values whose
        sum is equal to 2020?
    '''
    entries = [int(e) for e in entries]

    n = 2020
    
    d = {}
    for e in entries:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    for e_i in entries:
        e_j = n - e_i
        if e_j in d:
            if (e_i != e_j) or d[e_i] > 1:
                prod = e_i * e_j

                return prod

def solve_part2(entries):
    '''
    Given a list of integer values, what is the product of the three values 
        whose sum is equal to 2020?
    '''
    entries = [int(e) for e in entries]

    n = 2020

    d = {}
    for e in entries:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    for i in range(len(entries)):
        e_i = entries[i]
        for j in range(i+1, len(entries)):
            e_j = entries[j]
            e_k = n - e_i - e_j
            if e_k in d:
                all_diff = (e_i != e_j) and (e_i != e_k) and (e_j != e_k)
                ij_eq = (e_i == e_j) and (d[e_i] > 1)
                ik_eq = (e_i == e_k) and (d[e_i] > 1)
                jk_eq = (e_j == e_k) and (d[e_j] > 1)

                # for "n" not divisible by 3, this case will never happen
                all_eq = (e_i == e_j) and (e_i == e_k) and (d[e_i] > 2)

                if all_diff or ij_eq or ik_eq or jk_eq or all_eq:
                    prod = e_i * e_j * e_k

                    return prod

if __name__ == '__main__':
    entries = open('inputs/day1.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
