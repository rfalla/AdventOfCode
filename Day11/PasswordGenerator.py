# Day 11
# need to generate a password with requirements:
# a) No i,o,l
# b) 8 lowercase letters
# c) >= 1 increasing straight of 3 letters e.g. abc
# d) >= 2 different pairs of letters e.g. aabb
#
# Get password by incrementing old password
# e.g. ab->ac->ad->....->az->ba
# initial password = hxbxwxba

import string
def FindNextIncrement(password):
    l = 7
    l7 = alpha_no_iol.find(password[l])
    if l7 == 22:
        password[l] = alpha_no_iol[0]
        isZ = True
        while isZ == True:
            l -= 1
            if l  == -1:
                print 'Error: next increment means 9 character password'
                return 0
            lNext = alpha_no_iol.find(password[l])
            if lNext != 22:
                password[l] = alpha_no_iol[lNext+1]
                isZ = False
            else:
                password[l] = alpha_no_iol[0]
        #password[l-1] = alpha_no_iol[alpha_no_iol.find(password[l-1])+1]
    else:
        password[l] = alpha_no_iol[l7+1]
    return password

def OneStraight(password):
    for i in range(6):
        if alpha_no_iol.find(password[i])+1 == alpha_no_iol.find(password[i+1]) and alpha_no_iol.find(password[i])+2 == alpha_no_iol.find(password[i+2]):
            return True
    return False

def TwoPairs(password):
    pairs = []
    for i in range(7):
        if password[i] == password[i+1]:
            pairs.append(password[i])
    if len(pairs) < 2:
        return False
    while len(pairs) > 1:
        if pairs[0] != pairs[1]:
            return True
        else:
            pairs.remove(pairs[1])
    return False

def GoodPassword(password):
    goodPassword = False
    while goodPassword == False:
        password = FindNextIncrement(password)
        if TwoPairs(password) == True and OneStraight(password) == True:
            goodPassword = True
    print password
    return password

if __name__=="__main__":
    password = ['h','x','b','x','w','x','b','a'] 
    alphabet = string.lowercase
    # condition a
    alpha_no_i = alphabet.replace('i','')
    alpha_no_io = alpha_no_i.replace('o','')
    global alpha_no_iol
    alpha_no_iol = alpha_no_io.replace('l','') 
    for i in range(0,2):
        GoodPassword(password)
