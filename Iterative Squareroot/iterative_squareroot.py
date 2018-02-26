import sys
sys.setrecursionlimit(10000)

#Perform Binary Search
def find(g, l, h, c = -1, count = 0):

    #If we are larger than the threshold, check between the lower-bound and our current value
    if c*c - g > .0000001: return find(g, l, c, (c+l)/2, count+1)
    #If we are smaller than the threshold, check between the upper-bound and our current value    
    if c*c - g < -.0000001: return find(g, c, h, (c+h)/2, count+1)

    #If we are neither larger, nor smaller we're done!
    return count, c



if __name__ == "__main__":

    q = ""
    #Ask for a "digit" that is not negative
    while (not q.isdigit()) or (q[0] == '-'):
        q = input("Take the square root of which number? ")

    #count the digits in the number
    count = len(q.split('.')[0])
    
    #if the number has 1 digit, check between 0 and the digit for the squareroot
    if count == 1:
        l = 0
        h = float(q)
    else:
    #If the number has >1 digit, the lower bound = 10^(d/2) the upper bound = 10^d for it's squareroot
        h, l = [.1, .1]
        for i in range(count):
            if i%2 == 0:
                l *=10
            h*=10

    #Output
    print("\nChecking range %d - %d.." %(l, h))
    print("It took %d recursions to find the answer:  %f" %(find(float(q), l, h, (l+h)/2)))

    #Verification
    from math import sqrt
    print("\nmath.sqrt says: %f" %(sqrt(float(q))))
