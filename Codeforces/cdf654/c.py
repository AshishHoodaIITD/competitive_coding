t = int(input())

for i in range(t):
    a,b,n,m = [int(x) for x in input().split(" ")]
    if a+b < n+m:
        print("No")
        continue
    if min(a,b) < m:
        print("No")
        continue
    print("Yes")