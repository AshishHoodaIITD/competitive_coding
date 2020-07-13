t = int(input())
for i in range(t):
    a,b,c = [int(x) for x in input().split(" ")]
    ans1 = -1
    if a<c:
        ans1 = 1
    ans2 = -1
    if a*b>c:
        ans2 = b
    print(ans1," ",ans2)