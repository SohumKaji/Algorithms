#!/bin/python3

import sys

def organizingContainers(container):
    #Find how many balls each container can hold
    container_size = sorted([sum(c) for c in container])
    #Find out how the balls are distributed
    ball_counts = sorted([sum([c[i] for c in container]) for i in range(len(container))])

    #If the distributions don't match up, with 1 for 1 switching we cannot place each ball in
    #a container of its own type
    return "Possible" if container_size == ball_counts else "Impossible"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        print(result)
