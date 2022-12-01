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
            
    ## Find the maximum 3 values in the array
    top_1 = 0
    top_2 = 0
    top_3 = 0
    for calories in cal_array:
        # print(calories)
        if calories > top_1:
            top_3 = top_2
            top_2 = top_1
            top_1 = calories
        elif calories > top_2:
            top_3 = top_2
            top_2 = calories
        elif calories > top_3:
            top_3 = calories

    ## Ouput the final result
    print("Max Calories of Top 3 in array: {}".format(top_1 + top_2 + top_3))

if __name__ == '__main__':
    main()
