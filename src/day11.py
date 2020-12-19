def solve_part1(entries):
    entries = [list(e.rstrip()) for e in entries]
    
    entries = [['.'] + row + ['.'] for row in entries]
    n_seats = len(entries[0])

    empty_row = ['.' for _ in range(n_seats)]
    entries = [empty_row] + entries + [empty_row]
    n_rows = len(entries)
    
    while True:
        changed = False
        prev_entries = [row[:] for row in entries[:]]

        for row_i in range(1, len(prev_entries) - 1):
            row = prev_entries[row_i]
            for seat_i in range(1, len(row) - 1):
                seat = row[seat_i]

                adj_seats = prev_entries[row_i - 1][seat_i - 1:seat_i + 2] + \
                    [row[seat_i - 1]] + [row[seat_i + 1]] + \
                    prev_entries[row_i + 1][seat_i - 1:seat_i + 2]

                adj_occupied = adj_seats.count('#')
                if seat == 'L' and adj_occupied == 0:
                    entries[row_i][seat_i] = '#'
                    changed = True
                elif seat == '#' and adj_occupied >= 4:
                    entries[row_i][seat_i] = 'L'
                    changed = True

        if not changed:
            break

    total_occupied = sum([row.count('#') for row in entries])

    return total_occupied

def solve_part2(entries):
    entries = [list(e.rstrip()) for e in entries]

    n_seats = len(entries[0])
    n_rows = len(entries)

    while True:
        changed = False
        changes_list = []

        for row_i, row in enumerate(entries):
            for seat_i, seat in enumerate(row):
                adj_seats = []

                nav_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),
                    (0, -1), (-1, -1)]
                for (row_nav, seat_nav) in nav_list:
                    point_row_i = row_i + row_nav
                    point_seat_i = seat_i + seat_nav

                    while point_row_i >= 0 and point_row_i <= (n_rows - 1) and \
                        point_seat_i >= 0 and point_seat_i <= (n_seats - 1):

                        point_seat = entries[point_row_i][point_seat_i]

                        if point_seat != '.':
                            adj_seats.append(point_seat)
                            break

                        point_row_i += row_nav
                        point_seat_i += seat_nav

                adj_occupied = adj_seats.count('#')
                if seat == 'L' and adj_occupied == 0:
                    changes_list.append((row_i, seat_i, '#'))
                    changed = True
                elif seat == '#' and adj_occupied >= 5:
                    changes_list.append((row_i, seat_i, 'L'))
                    changed = True

        for row_i, seat_i, value in changes_list:
            entries[row_i][seat_i] = value

        if not changed:
            break

    total_occupied = sum([row.count('#') for row in entries])

    return total_occupied

if __name__ == '__main__':
    entries = open('inputs/day11.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
