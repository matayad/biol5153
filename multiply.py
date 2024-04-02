#! /usr/bin/env python3

def get_input():
    #ask for the size of the multiplication matrix
    x = int(input("Enter a number: "))
    # specify range for loop
    n = range(1, (x+1), 1)

    return x, n

def print_table(x, n):

    # calculate how many spaces we'll need for each cell matrix
    truewidth = len(str(x * x)) + 1

    #nested for loop to calculate row * col
    for row in n:
        for col in n:
            # nice formatted print statement for each cell
            print(('{:>{truewidth}}'.format(row*col, truewidth = truewidth)), end = "")
        #print a newline character at the end of each row
        print()

def main():
    input_num, width = get_input()

    print_table(input_num, width)


#set the environment for this script
#is it main, or is this a module being called by another script?
if __name__ == '__main__':
    main()
