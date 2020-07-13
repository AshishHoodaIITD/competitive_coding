import math
t = int(input())
for i in range(t):
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    x = int(inp[0]/inp[2])
    if x>=inp[1]:
        print(inp[1])
    else:
        ans = x - math.ceil(float(inp[1]-x)/float(inp[2]-1))
        print(ans)
