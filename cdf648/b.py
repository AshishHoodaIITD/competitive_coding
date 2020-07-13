import math
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    if sum(b) == len(b) or sum(b) == 0:
        flag = 0
        if(all(a[i] <= a[i + 1] for i in range(len(a)-1))): 
            flag = 1
        if flag == 1:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
