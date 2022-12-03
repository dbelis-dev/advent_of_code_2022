import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    priority_list = ""
    sum_priority = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, line-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.rstrip()
            length = len(line)
            ## Slice the string into 2 equal parts
            s1 = slice(0,length//2)
            s2 = slice(length//2,length)
            ## Find the common chars
            intersection = [item for item in list(line[s1]) if item in list(line[s2])]
            ## Discard the duplicates
            priority_list += ''.join(set(intersection))

    ## Iterate over the char list and calculate its order
    for char in priority_list:
        if char.isupper() is True:
            sum_priority += ord(char) - 38
        else:
            sum_priority += ord(char) - 96
    
    ## Ouput the final result
    print("Sum of Priorities: {}".format(sum_priority))

if __name__ == '__main__':
    main()
