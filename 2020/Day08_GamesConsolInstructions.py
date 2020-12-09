# Part 1: Input is a list of instructions:
# acc increases or decreases a single global value called the accumulator by the value given in the argument.
# After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# What is the value of acc before an instruction is repeated?
#
# Part 2: By changing exactly one jmp to a nop (or vice-versa) the program will stop infinitely looping and terminate. Fix this and print out the acc value when it terminates.
#
# Comments: Quite happy with part 1, think part 2 could be done more elegantly (i.e. not brute force).
import copy
def run_game(operations, instructions):
    acc, i = 0, 0
    used_instructions = set()
    while True:
        if i == len(instructions):
            return True, acc
        acc, i = operations[instructions[i][0]](acc, i, int(instructions[i][1]))
        if i in used_instructions:
            break
        else:
            used_instructions.add(i)
    return False, acc

operations = {'acc': lambda acc, x, y: (acc+y, x+1), 'jmp': lambda acc, x, y: (acc, x+y), 'nop': lambda acc, x, y: (acc, x+1)}
instructions = [x.strip('\n').split() for x in open('input_08.txt')]
print('Part 1: {}'.format(run_game(operations, instructions)[1]))

for i in range(len(instructions)):
    if instructions[i][0] != 'acc':
        test_instructions = copy.deepcopy(instructions)
        if test_instructions[i][0] == 'jmp':
            test_instructions[i][0] = 'nop'
        else:
            test_instructions[i][0] = 'jmp'
        terminated, acc = run_game(operations, test_instructions)
        if terminated == True:
            print('Part 2: {}'.format(acc))
            
