lines = list(
    map(
        str.strip,
        open("input.txt").readlines(),
    )
)


def is_sorted_either_way(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)


def check_adjacent_difference(lst):
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if 1 <= diff <= 3:
            continue
        else:
            return False
    return True


def check_again(l):
    for i in range(len(l)):
        copy_list = l.copy()
        copy_list.pop(i)
        if not check_adjacent_difference(copy_list):
            continue
        elif not is_sorted_either_way(copy_list):
            continue
        else:
            return True
    return False


string_list = [line.split() for line in lines]
integer_list = [[int(num) for num in sublist] for sublist in string_list]

# Part 1
unsafe = 0
safe = 0
for level in integer_list:
    if not is_sorted_either_way(level):
        unsafe += 1
    elif not check_adjacent_difference(level):
        unsafe += 1
    else:
        safe += 1

print(f"Unsafe lists: {unsafe}")
print(f"Safe lists: {safe}")

# Part 2
unsafe = 0
safe = 0
for level in integer_list:
    if not is_sorted_either_way(level) and not check_again(level):
        unsafe += 1
    elif not check_adjacent_difference(level) and not check_again(level):
        unsafe += 1
    else:
        safe += 1

print(f"Unsafe lists: {unsafe}")
print(f"Safe lists: {safe}")
