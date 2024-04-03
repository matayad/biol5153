#! /usr/bin/env python3

import argparse

def get_args():
    #create and ArgumentParser object
    parser = argparse.ArgumentParser(description = 'This script returns the Fibonacci number at \
        a specified location in the Fibonacci sequence')

    #add positional arguments (these are the ones that are absolutely essential/reguired)
    parser.add_argument("num", help="The Fibonacci number you wish to calculate", type=int)

    #add optionl arguments
    #if 'store_true', this means assign 'True' if the argument is specified on the command line, so the defacult for 'store_true' is false
    parser.add_argument("-v", "--verbose", help = "Print verbose output or not?", action = 'store_true')

    #parse the actual arguments
    args = parser.parse_args()

    return args



def calculate_fib(number):

    # initialize our variables for calculating the fibonacci number at this position in the sequence
    a, b = 0, 1

    #this is one way to calculate the Fibonacci number
    for i in range(int(number)):
        a,b = b,a+b

    fibonacci_number = a

    return a, number

def print_output(fibonacci_number, number):
    #print the output
    if args.verbose:
        print(f'The fibonacci number for {number} is: {fibonacci_number}')
    else:
        print(fibonacci_number)


def main():
    # calculate fibonacci number
    fibonacci_number, number = calculate_fib(args.num)

    #print the output
    print_output(fibonacci_number,number)

#get the command line arguments
args = get_args()

#set the environment for this script
#is it main, or is this a module being called by another script?
if __name__ == '__main__':
    main()
