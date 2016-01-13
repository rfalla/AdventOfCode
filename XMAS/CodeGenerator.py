# Day 25 AKA XMAS
# need to enter the code at (2978,3083)
# first need to figure out what iteration that is
# then need to work out what value it is
#
# code goes in order:
#     | 1   2   3   4   5   6   7
#  ---+---+---+---+---+---+---+---+
#   1 |  1   3   6  10  15  21  28
#   2 |  2   5   9  14  20  27
#   3 |  4   8  13  19  26
#   4 |  7  12  18  25
#   5 | 11  17  24
#   6 | 16  23
#   7 | 22
# etc. going to infinity
# this follows a patter using trianguler numbers where the iteration in (r,c) is as follows:
# for (r,c) iteration = 0.5(c)(c+1) + (r-1)(c) + 0.5(r-2)(r-1)
# e.g (1,1) = 0.5(1)(2) +(0)(1) + 0.5(-1)(0) = 1 + 0 + 0
#     (6,2) = 0.5(2)(3) +(5)(2) + 0.5(4)(5) = 3 + 10 + 10
#     (5,3) = 0.5(3)(4) +(4)(3) + 0.5(3)(4) = 6 + 12 + 6
# therefore at (2978,3083) the iteration is: 0.5(3083)(3084) + (2977)(3083) + 0.5(2976)(2977)
# which is equal to: 4753986 + 9178091 + 4429776 = 18361853
# actual code generated for nth iteration = [(code_{n-1})*252533]%33554393
# where the starting value (n = 1) is 20151125
# therefore answer:

r = 2978
c = 3083
iteration = 0.5*c*(c+1)
iteration += (r-1)*c
iteration += 0.5*(r-2)*(r-1)
print iteration
code = 20151125
i = 0
while i < iteration-1:
    code *= 252533
    code %= 33554393
    i += 1
print code
