#!/bin/python3

import sys
from math import sqrt

def column(matrix, i):
    return ''.join([row[i] for row in matrix if i < len(row)])  

def encryption(s):
    # Initialize L and use it to find the optimal values for the rows and columns
    # We take the squareroot of the length of the sentence
    # This way we can create a matrix where the rows are the floor of the square root and the ceiling of the square root
    # This guarantees that c >= r as well as c*r being as small as possible to hold all of the characters
    L = len(s)
    L_sq = sqrt(L)
    r = int(L_sq)
    c = int(L_sq) if L_sq.is_integer() else int(L_sq) + 1
    
    # We create the matrix with the dimensions we wanted
    encrypt = [s[i:i+c] for i in range(0, len(s), c)]

    # We create the final encrpted string by storing columns as words
    ans = ''
    for i in range(c):
        ans += column(encrypt, i) +' '

    return ans

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
