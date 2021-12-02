import math


def fuel_simple(m):
    m_int = int(m)
    return math.floor(m_int / 3) - 2


def fuel_recursive(current_number, acc_sum=0):
    fuel = fuel_simple(current_number)
    if fuel < 0:
        return acc_sum
    else:
        return fuel_recursive(
            fuel,
            acc_sum + fuel
        )


def process_lines(filename, fn):
    total_fuel = 0
    with open(filename, 'r') as data:
        datalines = (line.rstrip('\r\n') for line in data)
        for module in datalines:
            fuel = fn(module)
            total_fuel += fuel
    return total_fuel


def main():
    part_i = process_lines('input.txt', fuel_simple)
    print(f'Part I: {part_i}')
    part_ii = process_lines('input.txt', fuel_recursive)
    print(f'Part II: {part_ii}')


if __name__ == '__main__':
    main()
