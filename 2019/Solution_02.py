with open('input_02.txt') as f:
    InputIntcode = [int(x) for x in f.readline().split(',')]

#replace position 1 with the value noun and replace position 2 with the value verb

def IntcodeProgram(Intcode, noun, verb):
    NewList = Intcode[:]
    NewList[1] = noun
    NewList[2] = verb

    for i in range(0,len(NewList),4):
        if NewList[i] == 1:
            NewList[NewList[i+3]] = NewList[NewList[i+1]] + NewList[NewList[i+2]]
        elif NewList[i] == 2:
            NewList[NewList[i+3]] = NewList[NewList[i+1]] * NewList[NewList[i+2]]
        elif NewList[i] == 99:
            break
        else:
            print('ERROR')
    
    return NewList[0]

for i in range(100):
    for j in range(100):
        if IntcodeProgram(InputIntcode,i,j) == 19690720:
            print(100 * i + j)
    
        
    
