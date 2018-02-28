#!/bin/python3

import sys

def extraLongFactorials(n):
    prod, count = [1, 0]
    #For every factorial if we pair the largest number with the smallest e.g. n and 1
    #then n-1 and 2, we can observe a pattern where (n*1)+n-2 = (n-1)*2 meaning the distance between any two pairs of products
    # is the previous pairing prodct + n-2x where x is the step number. This cuts the number of calculations in half.
    for i in range(n, 1, -2):
        count +=i
        prod *= count
    
    #As expected of any method that folds a list in half, there is a caveat for odd numbered n's.
    #We must multiply by the unpaired number as we have missed it with our previous method.
    #This number is the exact center of the list so we divide by 2 and round up to find it.
    if n%2 == 1:
        prod*= (n//2)+1
    
    print(prod)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
