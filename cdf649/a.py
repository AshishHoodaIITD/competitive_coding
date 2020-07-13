import math
t = int(input())

def findFromStart(arr,x):
    currSum = 0
    max_size = 0
    for i in range(len(arr)):
        currSum += arr[i]
        if currSum%x != 0:
            max_size = max(max_size, i+1)
    return max_size

for i in range(t):
    inp = input().split(" ")
    n, x = int(inp[0]), int(inp[1])
    arr = [int(xx) for xx in input().split(' ')]

    ans = max(findFromStart(arr, x), findFromStart(arr[::-1], x))
    if ans==0:
        print(-1)
    else:
        print(ans)
