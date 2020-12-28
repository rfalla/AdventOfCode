# input is a series of mathematical operations, perform them in order of l->r rather than bodmas.
# Brackets still take precendence.
# Part 1: Evaluate the expression on each line of the input; what is the sum of the resulting values?
# Part 2: Now instead of l->r, addition takes precedence over multiplication.
from functools import reduce
def parse(line, operations):
    tally = [0]
    operator = ['+']
    line = line.replace(' ','')
    for i in range(len(line)):
        if line[i] == '(':
            tally.append(0)
            operator.append('+')
        elif line[i] == ')':
            end_bracket = tally.pop()
            operator.pop()
            tally[-1] = operations[operator[-1]](tally[-1], end_bracket)
        elif line[i].isdigit():
            tally[-1] = operations[operator[-1]](tally[-1], int(line[i]))
        else:
            operator[-1] = line[i]
    return tally[0]

def parse_new_rules(line, operations):
    # deal with brackets
    while True:
        next_close = line.find(')',0)
        if next_close < 0:
            break
        open_prev = line.find('(',0)
        open_curr = line.find('(', open_prev+1)
        if open_curr > next_close or open_curr < 0:
            open_curr = open_prev
        line = line[0:open_curr] + str(parse_new_rules(line[open_curr+1:next_close], operations)) + line[next_close+1:]
    # process addition
    tally = [0]
    operator = '+'
    for i in line.split():
        if i == '*':
            tally.append(1)
            operator = '*'
        elif i.isdigit():
            tally[-1] = operations[operator](tally[-1], int(i))
        else:
            operator = i
    return reduce(lambda x, y: x*y, tally)

if __name__=="__main__":
    lines = [x.strip('\n') for x in open('input_18.txt')]
    operations = {'+': lambda x, y: x+y, '*': lambda x, y: x*y}
    part1 = sum([parse(x, operations) for x in lines])
    part2 = sum([parse_new_rules(x, operations) for x in lines])
    print('Part 1: {}, Part 2: {}'.format(part1, part2))
