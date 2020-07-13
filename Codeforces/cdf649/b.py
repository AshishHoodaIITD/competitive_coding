import math

def printans(arr):
    print(" ".join([str(x) for x in arr]))
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    if len(arr)==2:
        print(2)
        printans(arr)
        continue
    dir = 0
    curr = arr[0]
    ans = [arr[0]]
    for a in arr[1:]:
        if a == curr:
            continue
        elif a > curr:
            if dir == 0:
                dir = 1
                ans.append(a)
                curr = a
            elif dir == 1:
                ans.pop(-1)
                ans.append(a)
                curr = a
            elif dir == -1:
                ans.append(a)
                curr = a
                dir = 1
        elif a < curr:
            if dir == 0:
                dir = -1
                ans.append(a)
                curr = a
            elif dir == 1:
                ans.append(a)
                curr = a
                dir = -1
            elif dir == -1:
                ans.pop(-1)
                ans.append(a)
                curr = a
    print(len(ans))
    printans(ans)

