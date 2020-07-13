import math
t = int(input())

dp = {0:1,1:3,2:7}

def get_total(num):
    if num in dp:
        return dp[num]
    total=0
    for i in range(0,num):
        total+=get_total(i)
    dp[num] = total + num + 1
    return dp[num]

def get_binary(x):
    return "{0:b}".format(x)

for i in range(t):
    n = int(input())
    x = get_binary(n)
    x = x[::-1]
    total = 0
    for i in range(len(x)):
        if x[i]=="1":
            total+=get_total(i)
    print(total)
