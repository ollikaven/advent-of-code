from math import *


def location(move, s):
    direction = move[0]
    steps = int(move[1:])
    if direction == 'U':
        return [s[0], s[1]+steps]
    elif direction == 'D':
        return [s[0], s[1]-steps]
    elif direction == 'L':
        return [s[0]-steps, s[1]]
    elif direction == 'R':
        return [s[0]+steps, s[1]]


def move_left(s):
    return [s[0]-1, s[1]]


def move_right(s):
    return [s[0]+1, s[1]]


def move_up(s):
    return [s[0], s[1]+1]


def move_down(s):
    return [s[0], s[1]-1]


def handle_move(instruction, current_pos):
    direction = instruction[0]
    steps = int(instruction[1:])
    j = 0
    locations = []
    while j < steps:
        if direction == 'U':
            new_loc = move_up(current_pos)
        elif direction == 'D':
            new_loc = move_down(current_pos)
        elif direction == 'L':
            new_loc = move_left(current_pos)
        elif direction == 'R':
            new_loc = move_right(current_pos)

        current_pos = new_loc
        locations.append(new_loc)
        j += 1
    return locations


def calc_route(wire):
    route = []
    for i, obj in enumerate(wire):
        if i == 0:
            s = [0, 0]
        else:
            s = route[-1]
        locations = handle_move(obj, s)
        route.extend(locations)

    return route


def intersection(lst1, lst2):
    tup1 = map(tuple, lst1)
    tup2 = map(tuple, lst2)
    return list(map(list, set(tup1).intersection(tup2)))


def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def main():
    routes = []
    with open('input.txt', 'r') as data:
        datalines = (line.rstrip('\r\n') for line in data)
        for line in datalines:
            wire = line.split(',')
            print(f'Calculating route')
            route = calc_route(wire)
            routes.append(route)
        common = intersection(routes[0], routes[1])
        print(f'Common: {common}')
        distances = [manhattan_distance(
            [0, 0, 0], [pair[0], pair[1], 0]) for pair in common]
        shortest = min(distances)
        print(f'Shortest distance: {shortest}')
        steps = [[routes[0].index(intersect)+1, routes[1].index(intersect)+1]for intersect in common]
        print('Steps for each wire to reach intersections')
        print(steps)
        total_steps = [pair[0] + pair[1] for pair in steps]
        print('Total steps')
        print(total_steps)
        min_steps = min(total_steps)
        print(f'Min steps: {min_steps}')

if __name__ == '__main__':
    main()



