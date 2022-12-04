lines = [x.split(',') for x in map(str.strip, open("input.txt").readlines())]

fully_contains = 0
overlap_at_all = 0
for x,y in lines:
    first = x.split('-')
    first_range = set(list(range(int(first[0]), int(first[1])+1)))
    second = y.split('-')
    second_range = set(list(range(int(second[0]), int(second[1])+1)))
    if first_range <= second_range or second_range <= first_range:
        fully_contains += 1
    if first_range & second_range:
        overlap_at_all += 1

print(f"Part 1: {fully_contains}")
print(f"Part 2: {overlap_at_all}")

