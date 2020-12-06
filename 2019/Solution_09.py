# IntCode = list of numbers which follow a pattern of [Instruction, Parameter1, Parameter2, Parameter3, Instruction...]
# Each Instruction consists of 2 parts, the rightmost two digits are an OpCode.
# The leftover digits are what Parameter Mode we should run our parameters in (going right to left).
# ABCDE: A: Parameter3, B: Parameter2, C: Parameter1, DE: OpCode
# OpCodes:
#### 1 -> Add Parameter1 and Parameter2, put it at Parameter3
#### 2 -> Multiply Parameter1 and Parameter2, put it at Parameter3
#### 3 -> Input Parameter1
#### 4 -> Output Parameter1
#### 5 -> Jump-if-true: if Parameter1 <> 0, Next Instruction = Parameter2
#### 6 -> Jump-if-false: if Parameter1 = 0, Next Instruction = Parameter2
#### 7 -> Less than: if Parameter1 < Parameter2, it stores 1 in the position given by Parameter3. Otherwise, it stores 0.
#### 8 -> Equals: if Parameter1 Parameter2, it stores 1 in the position given by Parameter3. Otherwise, it stores 0.
#### 99 -> HALT

# Parameter Modes:
#### 0 -> Position: Address[Parameter]
#### 1 -> Immediate: Parameter
#### 2 -> Relative: Address[Parameter + Base]
#### Blank -> Position

class Amplifier:
    def __init__(self, intCode, phase):
        self.intCode = intCode
        self.phase = phase
        self.pos = 0
        self.phaseUsed = False
        self.Halted = False

    def RunIntCode(self, input):
        inputUsed = False
        while self.pos < len(self.intCode):
            Instruction = str(self.intCode[self.pos])
            OpCode = int(Instruction[-2:])
            if len(Instruction) == 4:
                Modes = list(Instruction[::-1][-2:])
                Modes = [int(x) for x in Modes]
            elif len(Instruction) == 3:
                Modes = [int(Instruction[0]),0]
            else:
                Modes = [0,0]

            p1, p2 = self.Find_Parameters(Modes)

            #print(Instruction, OpCode, self.pos, p1, p2)

            if OpCode == 1:
                self.intCode[self.intCode[self.pos+3]] = p1 + p2
                self.pos+=4
            elif OpCode == 2:
                self.intCode[self.intCode[self.pos+3]] = p1 * p2
                self.pos+=4
            elif OpCode == 3:
                if self.phaseUsed and inputUsed:
                    break
                elif self.phaseUsed:
                    self.intCode[self.intCode[self.pos+1]] = input
                    inputUsed = True
                else:
                    self.intCode[self.intCode[self.pos+1]] = self.phase
                    self.phaseUsed = True
                    self.pos+=2
            elif OpCode == 4:
                self.output = p1
                self.pos+=2
            elif OpCode == 5:
                if p1 != 0:
                    self.pos = p2
                else:
                    self.pos+=3
                elif OpCode == 6:
                    if p1 == 0:
                        self.pos = p2
                    else:
                        self.pos+=3
                elif OpCode == 7:
                    if p1 < p2:
                        self.intCode[self.intCode[self.pos+3]] = 1
                    else:
                        self.intCode[self.intCode[self.pos+3]] = 0
                        self.pos+=4
                elif OpCode == 8:
                    if p1 == p2:
                        self.intCode[self.intCode[self.pos+3]] = 1
                    else:
                        self.intCode[self.intCode[self.pos+3]] = 0
                        self.pos+=4
                elif OpCode == 99:
                    self.Halted = True
                    break
        return self.output

    def Find_Parameters(self, Modes):
        p1 = p2 = 0
        try:
            if Modes[0] == 1:
                p1 = self.intCode[self.pos+1]
            else:
                p1 = self.intCode[self.intCode[self.pos+1]]
        except:
            pass
        try:
            if Modes[1] == 1:
                p2 = self.intCode[self.pos+2]
            else:
                p2 = self.intCode[self.intCode[self.pos+2]]
            except:
                pass
        return p1, p2

with open('input.txt') as f:
    IntCode = [int(x) for x in f.readline().split(',')]

# Part1
perm = permutations(range(5))
maxThrust = 0
for p in perm:
    input = 0
    for i in p:
        ic = IntCode.copy()
        amp = Amplifier(ic, i)
        input = amp.RunIntCode(input)
        maxThrust = max(maxThrust,input)
#print(p, input)
print(maxThrust)

# Part2
perm = permutations(range(5,10))
maxThrust = 0
for p in perm:
    input = 0
    amps = []
    for i in p:
        ic = IntCode.copy()
        amp = Amplifier(ic, i)
        input = amp.RunIntCode(input)
        amps.append(amp)
        #print(i, p, input, amp.Halted)
    i = 0
    while amps[4].Halted == False:
        input = amps[i%5].RunIntCode(input)
        i+=1
        #print(p, input)
        maxThrust = max(maxThrust,input)
#print(p, input)
print(maxThrust)
