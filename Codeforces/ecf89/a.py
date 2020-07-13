import math
t = int(input())

def equalans(a):
    ans = int(math.floor(a/3))*2
    if a%3==2:
        ans+=1
    return ans

for i in range(t):
    inp = input().split(" ")
    a, b = int(inp[0]), int(inp[1])

    if a==0 or b==0: 
        print(0)
        continue
    if a == b:
        print(equalans(a))
        continue

    if b > a:
        t = a
        a = b
        b = t
    
    if a>=2*b:
        print(b)
        continue

    ex = a%b
    a -= 2*ex
    b -= ex
    print(equalans(a)+ex)


