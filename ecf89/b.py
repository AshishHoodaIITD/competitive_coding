import math
t = int(input())
for i in range(t):
    inp = input().split(" ")
    n, x, m= int(inp[0]), int(inp[1]), int(inp[2])
    ops = []
    for j in range(m):
        inp = input().split(" ")
        l,r= int(inp[0]), int(inp[1])
        ops.append((l,r))
    min_index = x
    max_index = x
    for op in ops:
        if (min_index>op[1] or max_index<op[0])==False:
            min_index = min(min_index, op[0])
            max_index = max(max_index, op[1])
    print(max_index-min_index+1)