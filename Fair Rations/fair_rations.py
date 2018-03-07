#!/bin/python3

import sys

def fairRations(B):
    
    loaves = 0

    # If we want all of the elements in the set to be even
    # and our only tool is to add +2 to the set each time
    # the set must have an even sum or we will always have 
    # at least 1 odd element left
    
    if sum(B) % 2 == 1: return "NO"

    # For each element, if it is odd
    # Give it and the following element a loaf
    # The next iteration will address if that element is odd or not
    # This way the "oddness" is passed down the list until it is 
    # anteceded by another odd number, then both become even and that
    # instance of "oddness" is resolved
    
    for i in range(len(B)-1):
        if B[i]%2 == 1:
            loaves +=2
            B[i] += 1
            B[i+1] += 1
    
        # I figured we should check if the whole list is even
        # on each iteration and to quit when we had found achieved that.
        # However since we can solve this problem in O(n) time anyway
        # this optimization is actually detrimental 
        """
        
        if all(map(lambda x: x % 2 == 0, B)):
            break
        
        """

    return loaves
            
        

if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)