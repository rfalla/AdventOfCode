# Crytographic handshake stuff - copying & pasteing from AoC here because the definition is a bit tricky!
#The handshake used by the card and the door involves an operation that transforms a subject number. To transform a subject number, start with the value 1. Then, a number of times called the loop size, perform the following steps:
#
#Set the value to itself multiplied by the subject number.
#Set the value to the remainder after dividing the value by 20201227.
#The card always uses a specific, secret loop size when it transforms a subject number. The door always uses a different, secret loop size.
#
#The cryptographic handshake works like this:
#
#The card transforms the subject number of 7 according to the card's secret loop size. The result is called the card's public key.
#The door transforms the subject number of 7 according to the door's secret loop size. The result is called the door's public key.
#The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device. Now, the card has the door's public key, and the door has the card's public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.
#The card transforms the subject number of the door's public key according to the card's loop size. The result is the encryption key.
#The door transforms the subject number of the card's public key according to the door's loop size. The result is the same encryption key as the card calculated.
#
# Part 1: Given two public keys, work out the encryption key.
# Part 2: No part 2 :D
#
# pow(subject_number, loop_number, 20201227) could be used in place of find_val but I find it to be much slower.
def find_val(val, subject_number):
    val *= subject_number
    return val % 20201227

def find_loop(subject_number, target):
    loop_number = 0
    val = 1
    while val != target:
        loop_number += 1
        val = find_val(val, subject_number)
    return loop_number

def main():
    public_card = 14205034
    public_door = 18047856
    subject_number = 7
    loop_card = find_loop(subject_number, public_card)
    encryption_key = pow(public_door, loop_card, 20201227)
    print('Part 1: {}'.format(encryption_key))

main()
