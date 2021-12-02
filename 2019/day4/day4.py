def is_six_digit(password):
    str_pass = str(password)
    if len(str_pass) == 6:
        return True
    else:
        return False


def is_in_range(password):
    if 168630 <= password <= 718098:
        return True
    else:
        return False


def has_adjacent(password):
    str_pass = str(password)
    for x, y in zip(str_pass, str_pass[1:]):
        if x == y:
            return True
    return False


def has_unique_adjacent(password):
    str_pass = str(password)
    pairs = [(str_pass[i], str_pass[i + 1]) for i in range(len(str_pass) - 1)]
    for x, y in zip(str_pass, str_pass[1:]):
        if x == y:
            cnt = pairs.count((x, y))
            if cnt == 1:
                return True
    return False


def never_decreases(password):
    str_pass = str(password)
    for x, y in zip(str_pass, str_pass[1:]):
        if int(x) > int(y):
            return False
    return True


def possible_passwords():
    possible_passwords = 0
    for i in range(168630, 718098):
        if (is_six_digit(i) and is_in_range(i) and has_adjacent(i) and
            never_decreases(i) and has_unique_adjacent(i)):
            possible_passwords += 1
    return possible_passwords

