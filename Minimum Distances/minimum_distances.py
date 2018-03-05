#!/bin/python3

import sys

def minimumDistances(arr):
    ##############
    # Solution 1 #
    ##############
    
    # Concise and correct but O(n**2) running time because we are looping over all elements in arr
    # and then performing both the 'in' containment check and the index method for each element
    """
    # For every element in arr, find the next instace of it in the portion of arr that is after
    # the current element. Calculate and store that distance and return the minimum.
    
    dist = [arr[i+1:].index(arr[i]) + 1 for i in range(len(arr)-1) if arr[i] in arr[i+1:]]
    return min(dist) if dist else -1
    """    
    
    ##############
    # Solution 2 #
    ##############
    
    # So instead we can store the values of each element as we determine it's location
    # The 'furthest' location we have seen so far being the only required one for memory
    # This converts our solution to O(n) running time as we only need to traverse the list once
    
    d, m = [{}, -1]
    for i, a in enumerate(arr):
        if a in d:
            #Find distance from previous reference
            dist = i - d[a]
            
            #If that distance is 1, we are done
            if dist == 1: return 1
            
            #Update the dict with the new location
            d[a] = i
            
            #Update the minimum distance if required
            m = dist if m == -1 or m > dist else m
        
        else:
            #If there is no previously recorded distance, create one
            d[a] = i
    
    return m


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
