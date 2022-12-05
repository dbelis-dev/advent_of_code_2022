import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    count_overlaps = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, line-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.rstrip()
            ## Parse the input
            elf_ranges = line.split(',')
            elem1 = elf_ranges[0].split('-')
            elem2 = elf_ranges[1].split('-')
            ## Check whether the min/max values of a range
            ## are within the other range 
            if int(elem1[0]) >= int(elem2[0]) and int(elem1[1]) <= int(elem2[1]):
                count_overlaps += 1
            elif int(elem2[0]) >= int(elem1[0]) and int(elem2[1]) <= int(elem1[1]):
                count_overlaps += 1

    ## Ouput the final result
    print("Counter of Overlapping Sections: {}".format(count_overlaps))

if __name__ == '__main__':
    main()
