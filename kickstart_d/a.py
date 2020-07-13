t  = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    max_cur = -1
    count = 0
    for j in range(len(a)):
        if a[j]>max_cur:
            if j<len(a)-1:
                if a[j]>a[j+1]:
                    count+=1
            else:
                count+=1
        max_cur = max(max_cur,a[j])
    print('Case #'+str(i+1)+': '+str(count))