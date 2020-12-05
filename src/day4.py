def solve_part1(entries):
    fields = { 'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None,
        'ecl': None, 'pid': None }

    valid_passports = 0

    entries = list(entries)

    sep_entries = []
    curr_sep_entry = []
    for e in entries:
        if e != '\n':
            curr_sep_entry.append(e)
        else:
            sep_entries.append(curr_sep_entry)
            curr_sep_entry = []
    sep_entries.append(curr_sep_entry)

    sep_entries = [[l.rstrip() for l in se] for se in sep_entries]
    sep_entries = [' '.join(se).split(' ') for se in sep_entries]
    entries_fields = [[f.split(':')[0] for f in se] for se in sep_entries]
    entries_fields = [dict.fromkeys(ef, None) for ef in entries_fields]

    for ef in entries_fields:
        curr_valid = True
        for f in fields:
            if f not in ef:
                curr_valid = False
                break

        if curr_valid:
            valid_passports += 1

    return valid_passports

def solve_part2(entries):
    fields = { 'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None,
        'ecl': None, 'pid': None }

    valid_passports = 0

    entries = list(entries)

    sep_entries = []
    curr_sep_entry = []
    for e in entries:
        if e != '\n':
            curr_sep_entry.append(e)
        else:
            sep_entries.append(curr_sep_entry)
            curr_sep_entry = []
    sep_entries.append(curr_sep_entry)

    sep_entries = [[l.rstrip() for l in se] for se in sep_entries]
    sep_entries = [' '.join(se).split(' ') for se in sep_entries]
    entries_fields = [[f.split(':') for f in se] for se in sep_entries]
    entries_fields = [dict(ef) for ef in entries_fields]
    
    for ef in entries_fields:
        curr_valid = True

        for f in fields:
            if f not in ef:
                curr_valid = False
                break

        if not curr_valid:
            continue

        byr, iyr, eyr, hgt, hcl, ecl, pid = ef['byr'], ef['iyr'], ef['eyr'], \
            ef['hgt'], ef['hcl'], ef['ecl'], ef['pid']

        if not (len(byr) == 4 and (int(byr) >= 1920 and int(byr) <= 2002)):
            curr_valid = False
            continue

        if not (len(iyr) == 4 and (int(iyr) >= 2010 and int(iyr) <= 2020)):
            curr_valid = False
            continue

        if not (len(eyr) == 4 and (int(eyr) >= 2020 and int(eyr) <= 2030)):
            curr_valid = False
            continue

        if hgt.find('cm') != -1:
            if not(int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193):
                curr_valid = False
                continue
        elif hgt.find('in') != -1:
            if not(int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76):
                curr_valid = False
                continue
        else:
            curr_valid = False
            continue

        if not(hcl[0] == '#' and len(hcl) == 7):
            curr_valid = False
            continue

        if not (ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or \
            ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
            curr_valid = False
            continue
            
        if not(pid.isdigit() and len(pid) == 9):
            curr_valid = False
            continue

        if curr_valid:
            valid_passports += 1

    return valid_passports

if __name__ == '__main__':
    entries = open('inputs/day4.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
