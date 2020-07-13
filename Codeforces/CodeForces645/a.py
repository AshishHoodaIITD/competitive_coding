t = int(input())

for i in range(t):
    inp = input().split(" ")
    a = int(inp[0])
    b = int(inp[1])
    if a%2 == 0 or b%2==0:
        if a%2==0:
            aa = a/2
        else:
            aa = int(a/2) + 1
        if b%2==0:
            bb = b/2
        else:
            bb = int(b/2) + 1
        print(min(int(aa*b), int(a*bb)))
    else:
        aa = (a-1)/2
        bb = (b-1)/2
        print(min(int(aa*b + bb + 1) , int(a*bb + aa + 1)))