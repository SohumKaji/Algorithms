#!/bin/python3

import sys

def nonDivisibleSubset(k, arr):
    
    #Initialize dict for all possible modulo of k
    d = {i: [] for i in range(k)}
    
    #Find the modulo of all numbers in arr and add them to their respective list
    for a in arr:
        mod = a%k
        d[mod].append(a)
    
    set_size = 0
    
    #Compare the lists that would sum to k and choose the one with the larger number of elements
    #This way, no pair will sum to k
    for i in range(1, len(d)//2 +1):
        if len(d[i]) > len(d[k-i]):
            #Special Case: the members of this set have a modulo equal to exactly 1/2 of k
            #We can only have 1 of those
            if k/i == 2.0:
                set_size += 1
            else:
                set_size += len(d[i])
        else:
            #Special Case again
            if k/(k-i) == 2.0:
                set_size +=1        
            else:
                set_size +=len(d[k-i])
            
    #We can have 1 element from the modulo == 0 set...if it exists      
    if len(d[0]) > 0:
        set_size +=1
            
    return set_size

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
