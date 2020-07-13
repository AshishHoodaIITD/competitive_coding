import math
def findholes(arr):
    holes = [False]*100005
    for a in arr:
        holes[a] = True
    ret = []
    for i,h in enumerate(holes):
        if h == False:
            ret.append(i)
    return ret

def findb(arr):
    holes = findholes(arr)
    holes = holes[::-1]
    b_array = []
    for i,a in enumerate(arr):
        if i>0 and arr[i]>arr[i-1]:
            holes.append(arr[i-1])
        currhole = holes.pop(-1)
        b_array.append(currhole)
        if a < 0:
            return []
        if a != 0:
            if len(holes)>0:
                if holes[-1]<=a-1:
                    return []
    return b_array
n = int(input())
a = [int(x) for x in input().split(" ")]
ans = findb(a)
if len(ans)==0:
    print(-1)
else:
    print(" ".join([str(x) for x in ans]))