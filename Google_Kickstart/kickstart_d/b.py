t  = int(input())

def max_range(a,i,sk):
    count = 1
    for j in range(i+1,len(a)):
        if a[j]>a[j-1]:
            sk+=1
        elif a[j]==a[j-1]:
            pass
        elif a[j]<a[j-1]:
            sk-=1
        if sk<=4 and sk>=1:
            count+=1
        else:
            break
    return count

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    j = 1
    break_count = 0
    idir = 0
    ccount = 0
    while j<len(a):
        if a[j]>a[j-1]:
            if idir == 0: idir = 1
            elif idir == -1:
                idir = 1
                ccount = 0
        elif a[j]<a[j-1]:
            if idir == 0: idir = -1
            elif idir == 1:
                idir = -1
                ccount = 0
        if a[j]!=a[j-1]: ccount += 1
        if ccount==4:
            break_count+=1
            idir = 0
            ccount = 0
        j+=1
    print('Case #'+str(i+1)+': '+str(break_count))