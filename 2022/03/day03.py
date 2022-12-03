lines = list(map(str.strip, open("input.txt").readlines()))

common = [next(iter(set([char for char in x[:len(x)//2] if char in x[len(x)//2:]]))) for x in lines]

# Part 1
print(sum([ord(x)-96 if x.islower() else ord(x)-38 for x in common]))

# Part 2
common = [next(iter(set.intersection(*map(set,[lines[i],lines[i+1],lines[i+2]])))) for i in range(0, len(lines), 3)]

print(sum([ord(x)-96 if x.islower() else ord(x)-38 for x in common]))
