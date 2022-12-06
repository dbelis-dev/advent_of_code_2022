import sys
import os
 
def main():
    ## Set the variables/constants
    filepath = './input_file'
    num_crates = 0
    from_crate = 0
    to_crate = 0
    result = ''
    ## Initializing the stacks
    temp_stack = []
    all_stacks = []
    # one_stack = ['Z', 'N']
    # all_stacks.append(one_stack)
    # one_stack = ['M', 'C', 'D']
    # all_stacks.append(one_stack)
    # one_stack = ['P']
    # all_stacks.append(one_stack)
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
    one_stack = ['G', 'F', 'V', 'H', 'P', 'S']
    all_stacks.append(one_stack)
    one_stack = ['G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M']
    all_stacks.append(one_stack)
    one_stack = ['G', 'M', 'L', 'J', 'N']
    all_stacks.append(one_stack)
    one_stack = ['N', 'G', 'Z', 'V', 'D', 'W', 'P']
    all_stacks.append(one_stack)
    one_stack = ['V', 'R', 'C', 'B']
    all_stacks.append(one_stack)
    one_stack = ['V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z']
    all_stacks.append(one_stack)
    one_stack = ['T', 'H', 'P']
    all_stacks.append(one_stack)
    one_stack = ['Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V']
    all_stacks.append(one_stack)
    one_stack = ['F', 'L', 'G', 'P', 'V', 'Q', 'J']
    all_stacks.append(one_stack)
    print(all_stacks)
#     [M]             [Z]     [V]    
#     [Z]     [P]     [L]     [Z] [J]
# [S] [D]     [W]     [W]     [H] [Q]
# [P] [V] [N] [D]     [P]     [C] [V]
# [H] [B] [J] [V] [B] [M]     [N] [P]
# [V] [F] [L] [Z] [C] [S] [P] [S] [G]
# [F] [J] [M] [G] [R] [R] [H] [R] [L]
# [G] [G] [G] [N] [V] [V] [T] [Q] [F]
#  1   2   3   4   5   6   7   8   9 

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, line-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            temp_stack= []
            line = line.rstrip()
            ## Parse the input
            moves = line.split()
            num_crates = int(moves[1])
            from_crate = int(moves[3]) - 1
            to_crate   = int(moves[5]) - 1
            ## Pick N number of crates
            for i in range(num_crates):
                temp_stack.append(all_stacks[from_crate].pop())
            ## Reverse the order of the crates
            temp_stack = list(reversed(temp_stack))
            ## Move the crates to the other stack
            all_stacks[to_crate] += (temp_stack)
    
    ## Iterate over all the stacks and pick the last value
    for stack in all_stacks:
        result += stack.pop()
    
    ## Ouput the final result
    print("Top Crates: {}".format(result))

if __name__ == '__main__':
    main()
