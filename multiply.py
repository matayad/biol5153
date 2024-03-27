#! /usr/bin/env python3

x = int(input("Enter a number: "))
n = range(1, (x+1), 1)
longest = x * x
#print(longest)
width = len(str(longest))
truewidth = width + 1
#print(truewidth)

for row in n:
    for col in n:
        print(('{:>{truewidth}}'.format(row*col, truewidth = truewidth)), end = "")
    print()

#{:>{length}s}'.format(s, length=length)
