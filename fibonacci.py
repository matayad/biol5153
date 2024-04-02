#! /usr/bin/env python3

def get_input():
    # get the input
    number = int(input("enter the number: "))

    # initialize our variables for calculating the fibonacci number at this position in the sequence
    a, b = 0, 1

    return number, a, b

def calculate_fib(number, a, b):

    #this is one way to calculate the Fibonacci number
    for i in range(number):
        a,b = b,a+b

    fibonacci_number = a

    return a, number

def print_table(fibonacci_number, number):
    #print the output
    print(f'The fibonacci number for {number} is: {fibonacci_number}')


def main():
    number, a, b = get_input()
    calculate_fib(number, a, b)

    fibonacci_number, number = calculate_fib(number, a, b)
    print_table(fibonacci_number,number)

#set the environment for this script
#is it main, or is this a module being called by another script?
if __name__ == '__main__':
    main()
