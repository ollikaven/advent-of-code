lines = list(map(str.strip, open("input.txt").readlines()))

capa = [0]
elf_number = 0
for x in lines:
    if x != '':
       capa[elf_number] += int(x) 
    else:
        elf_number += 1
        capa.append(0)

# Part 1
print(max(capa))

# Part 2
print(sum(sorted(capa, reverse=True)[0:3]))
