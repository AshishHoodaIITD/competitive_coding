import math
t = int(input())
for i in range(t):
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    n, m, x, y = inp[0], inp[1], inp[2], inp[3]
    numOfDot = 0
    numOfTwo = 0
    for j in range(n):
        r = input()
        numOfDot += (len(r.split(".")) - 1)
        numOfTwo += (len(r.split("..")) - 1)
    
    if y >= 2*x:
        print(numOfDot*x)
    else:
        print(numOfTwo*y + (numOfDot - 2*numOfTwo)*x)