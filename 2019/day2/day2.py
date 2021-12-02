def get_data(filename):
    with open(filename, 'r') as f:
        lst = [int(x) for x in f.read().split(',')]
        return lst


def run(data, noun=12, verb=2):
    i = 0
    a = data[:]  # create copy of the data
    a[1] = noun
    a[2] = verb
    while a[i] != 99:
        if a[i] == 1:
            a[a[i+3]] = a[a[i+1]] + a[a[i+2]]
        elif a[i] == 2:
            a[a[i+3]] = a[a[i+1]] * a[a[i+2]]
        i += 4
    return a[0]


def part2(data):
    for i in range(100):
        for j in range(100):
            if run(data, i, j) == 19690720:
                return 100 * i + j


def main():
    part_i = run(get_data('input.txt'))
    print(f'Part I: {part_i}')
    part_ii = part2(get_data('input.txt'))
    print(f'Part II: {part_ii}')


if __name__ == '__main__':
    main()
