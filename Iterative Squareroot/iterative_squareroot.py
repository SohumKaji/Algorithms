import sys
sys.setrecursionlimit(10000)

def find(g, l, h, c = -1, count = 0):

    if c == -1: c = (l+h)/2
    
    if c*c - g > .0000001: return find(g, l, c, (c+l)/2, count+1)
    if c*c - g < -.0000001: return find(g, c, h, (c+h)/2, count+1)
    
    return count, c



if __name__ == "__main__":

    q = ""
    while (not q.isdigit()) or (q[0] == '-'):
        q = input("Take the square root of which number? ")

    count = len(q.split('.')[0])

    if count == 1:
        l = 0
        h = float(q)
    else:

        h, l = [.1, .1]
        for i in range(count):
            if i%2 == 0:
                l *=10
            h*=10

    print("\nChecking range %d - %d.." %(l, h))
    print("It took %d recursions to find the answer:  %f" %(find(float(q), l, h)))

    from math import sqrt
    print("\nmath.sqrt says: %f" %(sqrt(float(q))))
