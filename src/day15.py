def solve_part1(entries):
    entries = [int(e.rstrip()) for e in entries[0].split(',')]

    spoken_list = { v: [k+1] for k, v in enumerate(entries) }
    print(spoken_list)

    last_spoken = entries[-1]
    turn = spoken_list[last_spoken][0]

    while turn < 2020:
        turn += 1
        if len(spoken_list[last_spoken]) == 1:
            last_spoken = 0
        else:
            last_spoken = \
                spoken_list[last_spoken][-1] - spoken_list[last_spoken][-2]
        
        if last_spoken not in spoken_list:
            spoken_list[last_spoken] = []

        spoken_list[last_spoken].append(turn)

    result = last_spoken

    return result

def solve_part2(entries):
    entries = [int(e.rstrip()) for e in entries[0].split(',')]

    spoken_list = { v: [k+1] for k, v in enumerate(entries) }
    print(spoken_list)

    last_spoken = entries[-1]
    turn = spoken_list[last_spoken][0]

    while turn < 30000000:
        turn += 1
        if len(spoken_list[last_spoken]) == 1:
            last_spoken = 0
        else:
            last_spoken = \
                spoken_list[last_spoken][-1] - spoken_list[last_spoken][-2]
        
        if last_spoken not in spoken_list:
            spoken_list[last_spoken] = []

        spoken_list[last_spoken].append(turn)

    result = last_spoken

    return result

if __name__ == '__main__':
    entries = open('inputs/day15.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
