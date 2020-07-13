import math
t = int(input())

def find_element(ajmat, ele, done):
    count = 0
    for ch in ajmat[ele-1]:
        if ch in done:
            continue
        count+= find_element(ajmat, ch, done.union(set([ele])))
    return count+1

for i in range(t):
    inp = input().split(" ")
    n, x = int(inp[0]), int(inp[1])
    ajmat = []
    for j in range(n):
        ajmat.append([])
    for j in range(n-1):
        inp = [int(x) for x in input().split(" ")]
        ajmat[inp[0]-1].append(inp[1])
        ajmat[inp[1]-1].append(inp[0])
    nums = []
    for ch in ajmat[x-1]:
        nums.append(find_element(ajmat, ch, set([x])))
    nodds = 0
    for nn in nums:
        if nn%2==1:
            nodds+=1
    if nodds%2==1 or len(nums)==1:
        print("Ayush")
    else:
        print("Ashish")