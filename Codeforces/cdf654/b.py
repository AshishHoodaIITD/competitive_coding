t = int(input())

def sum_c(x):
    ans = x*(x+1)
    return ans/2

for i in range(t):
    n,r = [int(x) for x in input().split(" ")]
    if n==1 and r == 1:
        print(1)
        continue
    if n>r: print(int(sum_c(r)))
    else: print(int(sum_c(n-1)+1))