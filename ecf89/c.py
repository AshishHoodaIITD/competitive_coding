import math
t = int(input())

def travel_up(mat, n, m, r, c):
    temp = []
    while(r>=0 and c<=m-1):
        temp.append(mat[r][c])
        r-=1
        c+=1
    return temp

def count(x):
    c = len([xx for xx in x if xx==1])
    return len(x)-c, c

for i in range(t):
    inp = input().split(" ")
    n, m= int(inp[0]), int(inp[1])
    mat = []
    for j in range(n):
        mat.append([int(x) for x in input().split(" ")])
    palind = []
    palind.append([mat[0][0]])
    for j in range(1,n):
        palind.append(travel_up(mat, n, m, j, 0))
    for j in range(1,m):
        palind.append(travel_up(mat, n, m, n-1, j))
    
    changes = 0
    path_len = len(palind)
    for j in range(int(path_len/2)):
        countl = count(palind[j])
        countr = count(palind[path_len-1-j])

        changes = changes + min(countl[0] + countr[0], countl[1] + countr[1])

    print(changes)
    
