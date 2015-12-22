# Day15
# have 100 teaspoons to use up
# want to maximize cookie score
# score = sum(c)*sum(d)*sum(f)*sum(t)
# if any of the sums <= 0, total score = 0

#Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
#Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
#Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
#Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8

import numpy as NP
properties = NP.matrix("3,0,0,-3,2;-3,3,0,0,9;-1,0,4,0,1;0,0,-2,2,8")
amounts = NP.matrix("0,0,0,0")
max_score = 0
for i in range(0,100):
    for j in range(0,100-i): # need sprinkles or durability = 0
        if i+j > 100:
            continue
        for k in range(0,100-i-j):
            if i+j+k > 100:
                continue
            l = 100-i-j-k
            amounts[0,0] = i
            amounts[0,1] = j
            amounts[0,2] = k
            amounts[0,3] = l
            score_matrix = amounts*properties
            if score_matrix[0,4] != 500:
                continue
            if (score_matrix[0,0] <= 0 or score_matrix[0,1] <=0 or score_matrix[0,2] <=0 or score_matrix[0,3] <=0):
                continue
            else:
                score = score_matrix[0,0]*score_matrix[0,1]*score_matrix[0,2]*score_matrix[0,3]
            if score > max_score:
                max_score = score
print max_score
