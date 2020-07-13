import math

inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
edges = {}
for i in range(m):
    inp = input().split(" ")
    a, b = int(inp[0]), int(inp[1])
    if a not in edges:
        edges[a] = set([b])
    else:
        edges[a].add(b)
    if b not in edges:
        edges[b] = set([a])
    else:
        edges[b].add(a)
inp = [int(x) for x in input().split(" ")]
invalid = 0
for e in edges:
    #print(check)
    flag = 0
    for ch in edges[e]:
        if inp[ch-1] == inp[e-1]:
            flag = 1
            break
    if flag == 1:
        invalid = 1
        break
if invalid==1:
    print(-1)
else:
    ninp = [(x, i+1) for i,x in enumerate(inp)]
    ninp.sort()
    print(" ".join([str(x[1]) for x in ninp]))

