def solve_part1(entries):
    entries = [e.rstrip() if e != '\n' else ' ' for e in entries]
    
    adj_list = {}
    for e in entries:
        holder, inside_l = e.split(' bags contain ')
        if holder not in adj_list:
            adj_list[holder] = set()

        inside_l = inside_l.split(', ')
        for i in inside_l:
            i = i.split(' ')[1:3]
            i = ' '.join(i)

            if i != 'other bags.':
                if i not in adj_list:
                    adj_list[i] = set()
                adj_list[i].add(holder)

    n_holders = 0
    start = 'shiny gold'
    visited = set()
    stack = [start]
    while len(stack) > 0:
        h = stack.pop()
        if h not in visited:
            visited.add(h)
            stack.extend(adj_list[h] - visited)

            if h != start:
                n_holders += 1

    return n_holders

def solve_part2(entries):
    entries = [e.rstrip() if e != '\n' else ' ' for e in entries]
    
    adj_list = {}
    for e in entries:
        holder, inside_l = e.split(' bags contain ')
        if holder not in adj_list:
            adj_list[holder] = set()

        inside_l = inside_l.split(', ')
        for i in inside_l:
            if i != 'no other bags.':
                i = i.split(' ')

                n_i = int(i[0])
                t_i = ' '.join(i[1:3])

                adj_list[holder].add((n_i, t_i))            

    n_bags = 0
    start = 'shiny gold'
    stack = [(1, 1, start)]
    while len(stack) > 0:
        mult, nest_count, bag = stack.pop()

        n_bags += nest_count
        
        adj = [(mult_adj, mult_adj * nest_count, name_adj)
            for (mult_adj, name_adj) in adj_list[bag]]

        stack.extend(adj)

    n_bags -= 1

    return n_bags

if __name__ == '__main__':
    entries = open('inputs/day7.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
