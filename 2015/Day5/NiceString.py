# Day 5
# given a list of strings
# given some arbitrary rules, find out how many pass

def containsBadString(letterA, letterB):
    if letterA == 'a' and letterB == 'b':
        return True
    elif letterA == 'c' and letterB == 'd':
        return True
    elif letterA == 'p' and letterB == 'q':
        return True
    elif letterA == 'x' and letterB == 'y':
        return True
    else:
        return False
    
def isVowel(letter):
    if letter == 'a':
        return True
    elif letter == 'e':
        return True
    elif letter == 'i':
        return True
    elif letter == 'o':
        return True
    elif letter == 'u':
        return True
    else:
        return False
    
def isNiceString(string):
    print string
    vowel = 0
    doubleLetter = False
    for i in range(0,len(string)):
        if i < (len(string)-1):
            if containsBadString(string[i],string[i+1]):
                print 'fail: ab, cd, pq, or xy'
                return False
            elif string[i] == string[i+1]:
                doubleLetter = True
        if isVowel(string[i]):
            vowel += 1
    if vowel < 3:
        print 'fail: vowel'
        return False
    if doubleLetter == False:
        print 'fail: no double letter'
        return False
    return True

if __name__ == '__main__':
    input_file = open('input.txt')
    counter = 0
    for line in input_file:
        if (isNiceString(line)):
            counter += 1
    print 'There are {} nice strings'.format(counter)
