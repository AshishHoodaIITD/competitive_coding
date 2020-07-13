import sys
t = int(input())

def generate_tree(parent):
    N = len(parent)+1
    dp = [set() for i in range(N+1)]
    for i in range(len(parent)):
        dp[parent[i]].add(i+2)
    return dp

def get_node_count(parent, x):
    N = len(parent)+1
    count = [[0 for i in range(x)] for j in range(N+1)]
    for i in range(N,1,-1):
        count[i][0] += 1
        for j in range(x):
            count[parent[i-2]][(j+1)%x]+=count[i][j]
    count[1][0]+=1
    print(sys.getsizeof(count[0])*len(count))
    return [x[0] for x in count[1:]]

def get_node_count2(parent, x):
    N = len(parent)+1
    cache_p = [0 for j in range(N+1)]
    count = [0 for j in range(N+1)]
    for i in range(N,1,-1):
        count[i] += 1
        if cache_p[i]!=-1: count[cache_p[i]]+=count[i]
        if cache_p[i]!=0: continue
        c = []
        cur = i
        while True:
            if len(c)==x:
                if cache_p[c[0]]!=0: 
                    c = []
                    break
                cache_p[c[0]] = cur
                c.pop(0)
            c.append(cur)
            if cur==1: break
            cur = parent[cur-2]
        for cc in c: cache_p[cc] = -1
        if cache_p[i]!=-1: count[cache_p[i]]+=count[i]
    count[1]+=1
    return [x for x in count[1:]]

for i in range(t):
    n,a,b = [int(x) for x in input().split(' ')]
    #n,a,b = 100000,1000,1000
    if n<2:
        input()
        ans = 1
    else:
        parent = [int(x) for x in input().split(' ')]
        #parent = [x+1 for x in range(n-1)]
        A = get_node_count2(parent, a)
        B = get_node_count2(parent, b)
        S = sum(A)+sum(B)
        P = sum([A[i]*B[i] for i in range(len(A))])
        ans = float(S*n - P)/float(n*n)
    print('Case #'+str(i+1)+': '+str(ans))