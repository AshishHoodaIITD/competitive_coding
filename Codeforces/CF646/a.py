import math
t = int(input())
for i in range(t):
    inp = input().split(" ")
    n, x = int(inp[0]), int(inp[1])
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    neven = 0
    nodd = 0
    for xx in inp:
        if xx%2==0:
            neven+=1
        else:
            nodd+=1
    if x==n:
        if nodd%2==0:
            print("No")
        else:
            print("Yes")
        continue
    if neven>0:
        if x > neven:
            if nodd > 0:
                print("Yes")
            else: print("No")
        else:
            if nodd > 0:
                print("Yes")
            else:
                print("No")
    else:
        if x%2==0:
            print("No")
        else:
            print("Yes")
