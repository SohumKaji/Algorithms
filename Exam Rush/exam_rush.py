#!/bin/python3

import sys

def examRush(tm, t):
    #Sort in ascending order
    tm = sorted(tm)
    ans = 0
    
    #While there is still a course to test
    while(len(tm) >0):
        t-=tm.pop(0)
        #Subtract the amount of time to study the current subject
        #from the total time
        if(t < 0):
            #If that takes our time below 0, we cannot study it
            break
        
        #Since we had time, we study it and move on to the next subject
        ans +=1
        
    return ans


if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
       tm_t = int(input().strip())
       tm.append(tm_t)
    result = examRush(tm, t)
    print(result)
