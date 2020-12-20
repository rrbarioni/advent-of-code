def solve_part1(entries):
    earliest = int(entries[0])
    buses = [int(bus) for bus in entries[1].split(',') if bus.isdigit()]

    buses_departs = [(bus, bus * -(-earliest // bus) - earliest)
        for bus in buses]

    bus, depart = min(buses_departs, key=lambda bd: bd[1])

    result = bus * depart

    return result

def solve_part2(entries):
    def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
        # Source: https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset

        def extended_gcd(a, b):
            old_r, r = a, b
            old_s, s = 1, 0
            old_t, t = 0, 1
            while r:
                quotient, remainder = divmod(old_r, r)
                old_r, r = r, remainder
                old_s, s = s, old_s - quotient * s
                old_t, t = t, old_t - quotient * t

            return old_r, old_s, old_t

        gcd, s, t = extended_gcd(a_period, b_period)
        phase_difference = a_phase - b_phase
        pd_mult, pd_remainder = divmod(phase_difference, gcd)
        if pd_remainder:
            raise ValueError("Rotation reference points never synchronize.")

        combined_period = a_period // gcd * b_period
        combined_phase = (a_phase - s * pd_mult * a_period) % combined_period

        return combined_period, combined_phase

    buses = [(int(bus), bus_i) for bus_i, bus
        in enumerate(entries[1].split(',')) if bus.isdigit()]

    total_period, total_phase = (1, 0)
    for period, phase in buses:
        total_period, total_phase = combine_phased_rotations(total_period,
            total_phase, period, phase)

    earliest = total_period - total_phase

    return earliest

if __name__ == '__main__':
    entries = open('inputs/day13.txt').readlines()

    print('part 1: %s' % solve_part1(entries))
    print('part 2: %s' % solve_part2(entries))
