lines = list(map(str.strip, open("input.txt").readlines()))

new_list = [line.split() for line in lines]

l1 = []
l2 = []
for x in new_list:
    l1.append(int(x[0]))
    l2.append(int(x[1]))

l1.sort()
l2.sort()

# part 1
total_dist = 0
for i in range(len(l1)):
    total_dist += abs(l1[i] - l2[i])
print(total_dist)

# part 2
total_dist = 0
for i in range(len(l1)):
    total_dist += l1[i] * l2.count(l1[i])
print(total_dist)
