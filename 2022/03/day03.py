lines = list(map(str.strip, open("input.txt").readlines()))

def result(common):
    return sum([ord(x)-96 if x.islower() else ord(x)-38 for x in common])

print(result([next(iter(set([char for char in x[:len(x)//2] if char in x[len(x)//2:]]))) for x in lines]))
print(result([next(iter(set.intersection(*map(set,[lines[i],lines[i+1],lines[i+2]])))) for i in range(0, len(lines), 3)]))

