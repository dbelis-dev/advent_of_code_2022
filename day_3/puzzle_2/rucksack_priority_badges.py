import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    priority_list = ""
    sum_priority = 0
    input_array = []

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, line-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.rstrip()
            input_array.append(line)

    ## Iterate over the array, picking 2 elements at a time
    i = 0
    while i < len(input_array):
        elf1 = input_array[i]
        elf2 = input_array[i+1]
        elf3 = input_array[i+2]
        ## Find the common chars from the 3 strings
        intersection = list(set(list(elf1)) & set(list(elf2)) & set(list(elf3)))
        ## Discard the duplicates 
        priority_list += ''.join(set(intersection))
        i += 3

    ## Iterate over the char list and calculate its order
    for char in priority_list:
        if char.isupper() is True:
            sum_priority += ord(char) - 38
        else:
            sum_priority += ord(char) - 96
    
    ## Ouput the final result
    print("Sum of Badge Priorities: {}".format(sum_priority))

if __name__ == '__main__':
    main()
