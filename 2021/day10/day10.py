lines = list(map(str.strip, open("2021/day10/input.txt").readlines()))

mapping = dict(zip("({[<", ")}]>"))
error_codes = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
ac_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def is_matched(line):
    for letter in line:
        if letter in mapping:
            queue.append(letter)
        elif letter == mapping[queue[-1]]:
            queue.pop()
        else:
            return letter

error_score = 0
ac_scores = []
for line in lines:
    queue = []
    ac_score = 0
    error = is_matched(line)
    if error:
        error_score = error_score + error_codes[error] 
    else:
        while queue:
            a = mapping[queue.pop()]
            ac_score = ac_score * 5 + ac_points[a]
        ac_scores.append(ac_score)

print(f"Part 1: {error_score}")

ac_scores.sort()
middle_score = ac_scores[int(len(ac_scores)/2)]
print(f"Part 2: {middle_score}")
