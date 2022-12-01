import array
import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    cal_array = array.array('i',[])
    max_elf_cal = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne-by-line
    with open(filepath) as fp:
        for calories in fp.readlines():
            calories = calories.strip()
            ## Check if a lne is empty
            if calories == "":
                cal_array.append(int(max_elf_cal))
                max_elf_cal = 0
            else:
                max_elf_cal += int(calories)
    ## Add the last group of values
    cal_array.append(int(max_elf_cal))
            
    ## Find the maximum value in the array
    max_cal = 0
    for calories in cal_array:
        if calories > max_cal:
            max_cal = calories
    
    ## Ouput the final result
    print("Max Calories in array: {}".format(max_cal))

if __name__ == '__main__':
    main()
