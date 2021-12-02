with open("2021/day2/input.txt", "r") as file:
    _input = [x.strip().split(" ") for x in file.readlines()]

# Part 1
x = 0
y = 0
for command in _input:
    direction = command[0]
    value = int(command[1])
    if direction == "forward":
        x = x + value
    elif direction == "up":
        y = y - value
    elif direction == "down":
        y = y + value
    print(f"x: {x} y: {y}")

print(f"day1: {x*y}")


# Part 2 
x = 0
y = 0
aim = 0
for command in _input:
    direction = command[0]
    value = int(command[1])
    if direction == "forward":
        x = x + value
        y = y + (aim * value)
    elif direction == "up":
        aim = aim - value
    elif direction == "down":
        aim = aim + value
    print(f"x: {x} y: {y} aim: {aim}")

print(f"day2: {x*y}")
