lines = list(map(str.strip, open("input.txt").readlines()))

rounds = [x.split(' ') for x in lines]

elf = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
you = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

shape_score = {'rock': 1, 'paper': 2, 'scissors': 3}

total_score = 0
for x,y in rounds:
    elf_choice = elf.get(x)
    your_choice = you.get(y)
    if elf_choice == your_choice:
        total_score += shape_score.get(your_choice)+3
    elif elf_choice == 'rock' and your_choice == 'paper':
        total_score += shape_score.get(your_choice)+6
    elif elf_choice == 'paper' and your_choice == 'scissors':
        total_score += shape_score.get(your_choice)+6
    elif elf_choice == 'scissors' and your_choice == 'rock':
        total_score += shape_score.get(your_choice)+6
    else:
        total_score += shape_score.get(your_choice)+0

# Part1
print(f"Part1: {total_score}")

total_score = 0
for x,y in rounds:
    elf_choice = elf.get(x)
    if y == 'Y':
        total_score += shape_score.get(elf_choice)+3
    elif y == 'X':
        if elf_choice == 'rock':
            total_score += shape_score.get('scissors')
        elif elf_choice == 'paper':
            total_score += shape_score.get('rock')
        else:
            total_score += shape_score.get('paper')
    else:
        if elf_choice == 'rock':
            total_score += shape_score.get('paper')+6
        elif elf_choice == 'paper':
            total_score += shape_score.get('scissors')+6
        else:
            total_score += shape_score.get('rock')+6

# Part2
print(f"Part2: {total_score}")
