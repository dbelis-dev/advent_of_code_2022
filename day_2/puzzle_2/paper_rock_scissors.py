import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    input_array = []
    score = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, line-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            for value in line.split(' '):
                input_array.append(value.rstrip())
    
    ## Iterate over the array, picking 2 elements at a time
    i = 0
    while i < len(input_array):
        opponent = input_array[i]
        outcome = input_array[i+1]
        round = opponent + outcome
        if round in {'AY', 'BX', 'CZ'}: ## assume 'rock'
            shape_score = 1
        if round in {'AZ', 'BY', 'CX'}: ## assume 'paper'
            shape_score = 2
        if round in {'AX', 'BZ', 'CY'}: ## assume 'scissors'
            shape_score = 3
        ## check the outcome
        outcome_score = 6       ## win
        if outcome == 'X':      ## lose
            outcome_score = 0
        elif outcome == 'Y':    ## draw
            outcome_score = 3

        ## calculate the round score and add to total 
        score += outcome_score + shape_score
        i += 2
    
    ## Ouput the final result
    print("Max score: {}".format(score))

if __name__ == '__main__':
    main()
