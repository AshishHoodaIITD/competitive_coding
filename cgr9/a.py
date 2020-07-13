t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    for j in range(len(a)):
        if j%2==0:
            if a[j]>0: a[j] = a[j]*(-1)
        else:
            if a[j]<0: a[j] = a[j]*(-1)
    print(" ".join([str(x) for x in a]))