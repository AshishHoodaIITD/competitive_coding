t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    flag = 0
    for i in range(len(a)):
        if i+1!=a[i] and flag == 0:
            flag = 1
        if i+1==a[i] and flag == 1:
            flag = 2
        if i+1!=a[i] and flag == 2:
            flag = 3
    if flag == 0:
        print(0)
    elif flag == 1 or flag == 2:
        print(1)
    else:
        print(2)