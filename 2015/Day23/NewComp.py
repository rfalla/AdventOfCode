# Day 23
# have 6 instructions
# 2 registers
# find value of register b
# once completed instructions
# instructions are completed when they are undefined
registers = {}
registers['a'] = 0#1
registers['b'] = 0
input = open('input.txt')
instructions = []
for line in input:
    instructions.append(line.replace('\n',''))
counter = 0
while registers['a'] >= 0 and registers['b'] >= 0 and counter < len(instructions) and counter > -1:
    parts = instructions[counter].split()
    print parts,counter,registers
    if parts[0] == 'hlf':
        registers[parts[1]] //= 2
        counter += 1
    elif parts[0] == 'tpl':
        registers[parts[1]] *= 3
        counter += 1
    elif parts[0] == 'inc':
        registers[parts[1]] += 1
        counter += 1
    elif parts[0] == 'jmp':
        counter += int(parts[1])
    elif parts[0] == 'jie':
        if registers[parts[1][0]] % 2 == 0:
            counter += int(parts[2])
        else:
            counter += 1
    elif parts[0] == 'jio':
        if registers[parts[1][0]] == 1:
            counter += int(parts[2])
        else:
            counter += 1
print registers['b']
