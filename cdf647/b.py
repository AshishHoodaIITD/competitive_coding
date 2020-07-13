import math
t = int(input())

def get_binary(x):
    return "{0:b}".format(x)

for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    dp = [False for i in range(1025)]
    for ii in inp:
        dp[ii] = True
    if n%2!=0:
        print(-1)
        continue
    binp = [get_binary(x) for x in inp]
    binp = ["0"*(10-len(x))+x for x in binp]
    check = [0]*10
    for b in binp:
        for bb in range(10):
            if b[bb]=="1":
                check[bb]+=1
            else: check[bb]-=1
    sinp = set(inp)
    ans = 0

    for a in range(1,1025):
        binary_a = get_binary(a)
        binary_a = "0"*(10-len(binary_a))+binary_a
        flag = 0
        for j in range(10):
            if binary_a[j]=="1" and check[j]!=0:
                flag = 1
                break
        if flag == 1:
            continue
        flag = 0
        for tt in inp:
            if dp[a^tt]==False:
                flag=1
        if flag==0:
            ans = a
            break
    if ans==0:
        print(-1)
    else:
        print(ans)