#!/bin/python3

import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    #O(n) time solution
    #We find the number of possible open squares for the queen in each direction

    #Rather than looking though the squares on the board we look through the obstacles, treating the end of the board as
    #a perimeter of obstacles. Subtracting the nearst obstacle's coordinates in any of the 8 directions from the  
    #queen coordinate yields the correct number of open squares the queen can access - given that the obstacle is directly
    #in the path of the direction we are checking. That is what we are looking for.

    #The first list comphrehension in each direction finds the nearest object
    #We add the edge of the board to this list comprehension and take the min or max depending on the direction
    #If we took the max we subtract that from the queen corrdinates to find the available squares
    #If we took the min then our reference point was 0 so we do not need to subtract
    
    a = [0]*8
    #Above
    a[0] = min([o[0]-1 for o in obstacles if o[1] == c_q and o[0]>r_q]+[n]) - (r_q)
    
    #Below
    a[1] = (r_q - max([o[0]+1 for o in obstacles if o[1] == c_q and o[0]<r_q]+[1])) 
    
    #Right
    a[2] = min([o[1]-1 for o in obstacles if o[0] == r_q and o[1]>c_q]+[n]) - (c_q)
    
    #Left
    a[3] = (c_q - max([o[1]+1 for o in obstacles if o[0] == r_q and o[1]<c_q]+[1])) 
    
    #Top Right Diag
    a[4] = min( [(o[0] - r_q)-1 for o in obstacles if o[0] - r_q == o[1] - c_q and o[0]>r_q and o[1]>c_q] + [min([n-r_q, n-c_q]) ])
    
    #Top Left Diag
    a[5] = min( [(o[0] - r_q)-1 for o in obstacles if o[0] - r_q == c_q - o[1] and o[0]>r_q and c_q>o[1]] + [min([n-r_q, c_q-1]) ])
    
    #Bottom Right Diag
    a[6] = min([(r_q - o[0])-1 for o in obstacles if r_q - o[0] == o[1] - c_q and r_q>o[0] and o[1]>c_q] + [min([r_q-1, n-c_q])]) 
    
    #Bottom Left Diag
    a[7] = min([(r_q- o[0])-1 for o in obstacles if o[0] - r_q == o[1] - c_q and r_q>o[0] and c_q>o[1]] + [min(r_q-1, c_q-1)])
    
    return sum(a)
    
    
    
    return squares

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
       obstacles.append(obstacles_t)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
