import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    input_array = []
    winning_set = {'AY', 'BZ', 'CX'}
    draw_set = {'AX', 'BY', 'CZ'}
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
        me = input_array[i+1]
        round = opponent+me
        shape_score = 1     ## assume 'rock'
        outcome_score = 0   ## assume lost
        ## check if it's a draw or a win
        if round in winning_set:
            outcome_score = 6
        if round in draw_set:
            outcome_score = 3
        ## check the shape score
        if me == 'Y':
            shape_score = 2
        elif me == 'Z':
            shape_score = 3
        ## calculate the round score and add to total 
        score += outcome_score + shape_score
        i += 2
    
    ## Ouput the final result
    print("Max score: {}".format(score))

if __name__ == '__main__':
    main()
