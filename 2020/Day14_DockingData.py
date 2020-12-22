# Part 1: Input can either update the bitmask or write a value to memory.
# Values and memory addresses are both 36-bit unsigned integers. e.g., ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.
# The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0) on the right.
# The current bitmask is applied to values immediately before they are written to memory:
#     0 or 1 overwrites the corresponding bit in the value
#     X leaves the bit in the value unchanged.
# What is the sum of the values in memory at the end of the sequence?
#
# Part 2: Instead of masking the value, mask the address in the following way:
#     If the bitmask bit is 0, the corresponding memory address bit is unchanged.
#     If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
#     If the bitmask bit is X, the corresponding memory address bit is floating.
#
# After looking through some comments/answers online I think it would be good to rewrite this using a generator for applying the mask to binary numbers.
def swap_str_char(input_string, i, new_char):
    if i == 0:
        return new_char + input_string[1:]
    elif i == len(input_string):
        return input_string[0:-1] + new_char
    else:
        return input_string[0:i] + new_char + input_string[i+1:]

def apply_mask_val(mask, val):
    binary_val = "{:0>36b}".format(val)
    for i in range(len(mask)):
        if mask[i] != 'X':
            binary_val = swap_str_char(binary_val, i, mask[i])
    return int(binary_val,2)

def apply_mask_address(mask, address, val, part2):
    binary_address = "{:0>36b}".format(address)
    # swap 1s
    n1 = mask.count('1')
    k = -1
    for i in range(n1):
        k = mask.find('1',k+1)
        binary_address = swap_str_char(binary_address, k, '1')
    # swap Xs
    nX = mask.count('X')
    format_string = "{:0>" + str(nX) + "b}"
    for i in range(2**nX):
        to_swap = format_string.format(i)
        new_address = binary_address
        k=-1
        for j in to_swap:
            k = mask.find('X',k+1)
            new_address = swap_str_char(new_address, k, j)
        part2[new_address] = val
    return part2

def process_line(line, mask, part1, part2):
    line = line.strip('\n').split(' = ')
    if line[0] == 'mask':
        mask = line[1]
    else:
        mem_address = int(line[0].replace('mem[','').replace(']',''))
        mem_val = int(line[1])
        part1[mem_address] = apply_mask_val(mask, mem_val)
        part2 = apply_mask_address(mask, mem_address, mem_val, part2)
    return mask, part1, part2

if __name__=="__main__":
    mask = ''
    part1 = {}
    part2 = {}
    file = open('input_14.txt','r')
    for line in file.readlines():
        mask, part1, part2 = process_line(line, mask, part1, part2)
        file.close()
    print('Part 1: {}, Part 2: {}'.format(sum(part1.values()), sum(part2.values())))
    
