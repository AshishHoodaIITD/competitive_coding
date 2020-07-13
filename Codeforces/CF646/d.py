import math
import sys
t = int(input())

def make_query(arr):
    str_q = " ".join([str(x) for x in arr])
    print("? "+str(len(arr))+ " " +str_q)
    sys.stdout.flush()
    ans = int(input())
    if ans == -1:
        return None
    return ans

def solve_subsets(arr, half):
    lh = set([])
    for ar in arr[:half]:
        lh = lh.union(ar)
    rh = set([])
    for ar in arr[half:]:
        rh = rh.union(ar)
    lm = make_query(lh)
    rm = make_query(rh)
    return lm, rm

def getarr(v, s):
    arr = []
    for i in range(s):
        arr.append(v)
    return arr

def solve(arr):
    half = int(len(arr)/2)
    lm, rm  = solve_subsets(arr, half)
    lh = arr[half:]
    rh = arr[:half]
    if lm < rm:
        if len(rh) == 1:
            ans = getarr(rm,len(lh)) + getarr(make_query(lm), len(rh))
        else:
            ans = getarr(rm,len(lh)) + solve(rh)
    elif rm < lm:
        if len(lh) == 1:
            ans = getarr(make_query(lh[0]),len(lh)) + getarr(lm,len(rh))
        else:
            ans = solve(lh) + getarr(lm,len(rh))
    else:
        if len(lh) == 1:
            lans = getarr(make_query(lh[0]),len(lh))
        else:
            rans = solve(lh)
        if len(rh) == 1:
            rans = getarr(make_query(rh[0]),len(rh))
        else:
            lans = solve(rh)
        ans = lans + rans
    return ans

for i in range(t):
    inp = input().split(" ")
    n, k = int(inp[0]), int(inp[1])

    subsets = []
    for j in range(k):
        inp = [int(x) for x in input().split(" ")]
        subsets.append(inp[1:])

    ans = solve(subsets)
    ans_st = " ".join([str(x) for x in ans])
    print("! "+ans_st)
    sys.stdout.flush()
    res = input()
    if res != "Correct":
        break

