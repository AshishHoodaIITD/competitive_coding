t = int(input())

def fill_right(mat,i,j,k):
    r = len(mat)
    c = len(mat[0])
    while i<r and j<c and k>0:
        mat[i][j] = 1
        i+=1
        j+=1
        k-=1
    if i<r and j<c:
        return mat, k, False
    return mat, k, True

for i in range(t):
    n,k = [int(x) for x in input().split(" ")]
    mat = [[0 for j in range(n)] for p in range(n)]
    min_val = 0
    for j in range(n):
        if k==0: break
        min_val = 2
        mat, k, comp= fill_right(mat, j, 0, k)
        if j==0 and comp==True:
            min_val = 0
        if j==0: continue
        if k==0: break
        mat, k, comp = fill_right(mat, 0, n-j, k)
        if comp: min_val = 0
        else: min_val = 2
    
    print(min_val)
    for m in mat:
        print(''.join([str(x) for x in m]))
    