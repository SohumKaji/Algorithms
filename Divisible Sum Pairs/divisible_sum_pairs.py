#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    
    #Create a dictionary with a key for every possible value of %k
    d = {i: [] for i in range(k)}
    
    #Populate dictionary with the values whose modulo k equals the key
    for a in ar:
        d[a%k].append(a)
    
    pairs = 0
    #For every modulo in group i and it's complementary modulo group k-i, find all combinations of pairs between i and k-i
    #That is because the sum of one item from each group will results in a modulo of 0
    for i in range(1, k//2 +1):
        
        #In the special scenario where i == k-i (in odd numbers at the center of the list)
        #Count how man combinations can happen between the items in this group and terminate the loop as we have 
        #checked all other pairs
        if i == k-i:
            pairs += (len(d[i]) * (len(d[i])-1))//2
            break
            
        #Find the number of all combinations between sets    
        pairs += len(d[i]) * len(d[k-i])
        
    #For the index 0, find all combination between elements in that set 
    #(the sum of two elements from this set will have a modulo of 0)
    pairs += (len(d[0]) * (len(d[0])-1))//2
    
    return pairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
