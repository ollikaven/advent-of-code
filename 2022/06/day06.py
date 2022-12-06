datastream = list(map(str.strip, open("input.txt").readlines()))[0]

def all_unique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def calculate(marker):
    buffer = []
    i = 0
    for x in datastream:
        if len(buffer) < marker:
            buffer.append(x)
        else:
            buffer.pop(0)
            buffer.append(x)
            if all_unique(buffer):
                break
        i += 1
    return i+1

# Part 1
print(calculate(4))

# Part 2
print(calculate(14))
