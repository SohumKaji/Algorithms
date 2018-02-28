#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    i = 0
    while(i < len(alice)):
        if scores:
            if alice[i] < scores[-1]:
                print(len(scores)+1)
                i+=1
            else:
                scores.pop()
        else:
            print(1)
            i+=1
            

    

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    scores = list(set(scores))
    scores.sort(reverse=True)
    climbingLeaderboard(scores, alice)
