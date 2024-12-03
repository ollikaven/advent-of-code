import re

with open("input.txt", "r") as file:
    input_string = file.read()

pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
instructions = [
    (int(x), int(y)) if x and y else ("do()" if do else "don't()")
    for x, y, do, dont in re.findall(pattern, input_string)
]

print(instructions)

enabled = True
total = 0
for instruction in instructions:
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif enabled:
        total += instruction[0] * instruction[1]

print(total)
