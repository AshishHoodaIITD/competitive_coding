t = int(input())

for i in range(t):
    n,m = [int(x) for x in input().split(" ")]
    mat = []
    for j in range(n):
        tt = [int(x) for x in input().split(" ")]
        mat.append(tt)
    ends = [2]+[3]*(m-2)+[2]
    middle = [3] + [4]*(m-2)+[3]
    max_mat = [ends]+[middle]*(n-2)+[ends]
    flag = 0
    for p in range(len(mat)):
        for q in range(len(mat[0])):
            if mat[p][q] > max_mat[p][q]:
                flag = 1
                break
    if flag==1:
        print("NO")
    else:
        print("YES")
        for m in max_mat:
            print(' '.join([str(x) for x in m]))
