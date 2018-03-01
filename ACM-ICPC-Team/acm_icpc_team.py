#!/bin/python3

import sys

def acmTeam(topic):
    top = [0,0]
    
    #Convert the topic strings into integers based on their binary representation
    topic = [int(t, 2) for t in topic]
    
    #Compare each topic
    for i in range(len(topic)):
        #To the topics listed after it
        for ii in range(i+1, len(topic)):
            #Perform an OR operation between the two topics
            #Convert the result to a binary representation
            #Count the number of 1's to determine the total topics covered by the pair
            known = bin(topic[i]|topic[ii]).count('1')
            
            #If it is the highest seen so far or tied for it
            #update appropriately
            if known > top[0]: top = [known, 1]
            elif known == top[0]: top[1]+=1
    
    return top
            
            

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    topic = []
    topic_i = 0
    for topic_i in range(n):
       topic_t = str(input().strip())
       topic.append(topic_t)
    result = acmTeam(topic)
    print ("\n".join(map(str, result)))