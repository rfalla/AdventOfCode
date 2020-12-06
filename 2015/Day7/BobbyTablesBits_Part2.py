# Day 7
# given a list of bitwise operations, find the signal given to a
# this time start with b = 956 (from Part a)

def gate(line,signalMap,gateType,input):
    parts = line.split(' ')
    key = 'key'
    x = 0
    y = 0
    z = 0
    if gateType == 'NOT':
        if parts[1].isdigit():
            x = int(parts[1])
        elif parts[1] in signalMap.keys():
            x = signalMap[parts[1]]
        else:
            #print '{} not in signal map yet'.format(parts[1])
            return
        z = ~x
        key = parts[3].rstrip('\n')
    else:
        key = parts[4].rstrip('\n')
        if parts[0].isdigit() and parts[2].isdigit():
            x = int(parts[0])
            y = int(parts[2])
        elif parts[0].isdigit() and parts[2] in signalMap.keys():
            x = int(parts[0])
            y = signalMap[parts[2]]
        elif parts[0] in signalMap.keys() and parts[2].isdigit():
            x = signalMap[parts[0]]
            y = int(parts[2])
        elif parts[0] in signalMap.keys() and parts[2] in signalMap.keys():
            x = signalMap[parts[0]]
            y = signalMap[parts[2]]
        else:
            #print '{0} or {1} not in signal map yet'.format(parts[0],parts[2])
            return
        print 'x = {0}, y = {1}'.format(x,y)
        if gateType == 'AND':
            z = x & y
        elif gateType == 'OR':
            z = x | y
        elif gateType == 'LSHIFT':
            z = x << y
        elif gateType == 'RSHIFT':
            z = x >> y
    print 'initial z = {}'.format(z)
    while z < 0:
        z += 65536
    while z > 65535:
        z -= 65536
    print 'signalMap[{0}] = {1}'.format(key,z)
    signalMap[key] = z
    input.remove(line)
            

if __name__ == '__main__':
    instructions = open('input.txt')
    input = instructions.readlines()
    signalMap = {}
    signalMap['b'] = 956
    # put inside a while loop for signalMap['a']
    while 'a' not in signalMap.keys():
        for i in input:
            #print i
            if i.find('AND') >= 0:
                gate(i,signalMap,'AND',input)
            elif i.find('NOT') >= 0:
                gate(i,signalMap,'NOT',input)
            elif i.find('LSHIFT') >= 0:
                gate(i,signalMap,'LSHIFT',input)
            elif i.find('RSHIFT') >= 0:
                gate(i,signalMap,'RSHIFT',input)
            elif i.find('OR') >= 0:
                gate(i,signalMap,'OR',input)
            elif i.find('->') >= 0:
                parts = i.split(' -> ')
                key = parts[1].rstrip('\n')
                if key == 'b': # don't want to repeat Part 1
                    continue
                if parts[0].isdigit():
                    signalMap[key] = int(parts[0])
                    print 'signalMap[{0}] = {1}'.format(key,int(parts[0]))
                    input.remove(i)
                elif parts[0] in signalMap.keys():
                    print 'signalMap[{0}] = {1}'.format(key,signalMap[parts[0]])
                    signalMap[key] = signalMap[parts[0]]
                    input.remove(i)
                #else:
                    #print '{} not in signalMap yet'.format(key)
            else:
                print 'Warning: instruction unclear, skipping: {}'.format(i)
    print signalMap['a']
