from statistics import median, mean

with open("2021/day7/input.txt", "r") as file:
    _input = [x.strip() for x in file.readlines()]

line = list(map(int,_input[0].split(",")))

# Part 1
m = int(median(line))

total_fuel = 0
for x in line:
    fuel = abs(m-x)
    total_fuel = total_fuel + fuel

print(f"Part 1: {total_fuel}")

# Part 2
avg = int(mean(line))

total_fuel = 0
for x in line:
    dist = abs(avg-x)
    fuel = sum(list(range(1,dist+1)))
    total_fuel = total_fuel + fuel


print(f"Part 2: {total_fuel}")
