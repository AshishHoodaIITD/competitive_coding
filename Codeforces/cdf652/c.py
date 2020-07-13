t = int(input())
for i in range(t):
    n,k = [int(x) for x in input().split(" ")]
    a = [int(x) for x in input().split(" ")]
    w = [int(x) for x in input().split(" ")]
    ans = 0
    j = 0
    allotment = []
    a = sorted(a,reverse=True)
    w = sorted(w)
    while j<k:
        allotment.append([a[j]])
        j+=1
    for p,ww in enumerate(w):
        if ww>1:
            j+=(ww-2)
            allotment[p].append(a[j])
            j+=1
        if j==len(a):
            break
    for aa in range(len(allotment)):
        if len(allotment[aa])==1:
            allotment[aa].append(allotment[aa][0])
    ans = sum([sum(x) for x in allotment])
    print(ans)
        
    