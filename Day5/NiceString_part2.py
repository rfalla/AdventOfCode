# Day 5
# given a list of strings
# given some arbitrary rules, find out how many strings pass

def isNiceString(string):
    print string
    repeatMiddle = False
    pairRepeat = False
    for i in range(0,len(string)-2):
        if string[i] == string[i+2]:
            repeatMiddle = True
        pair = string[i:i+2]
        print pair
        string_noPair = string[:i] + string[i+2:]
        print string_noPair
        if string_noPair.find(pair,i) > -1:
            pairRepeat = True
    if repeatMiddle == False:
        print 'fail: no letters repeating with one in the middle'
        return False
    if pairRepeat == False:
        print 'fail: no repeating pair'
        return False
    return True

if __name__ == '__main__':
    input_file = open('input.txt')
    counter = 0
    for line in input_file:
        if (isNiceString(line)):
            counter += 1
    print 'There are {} nice strings'.format(counter)
