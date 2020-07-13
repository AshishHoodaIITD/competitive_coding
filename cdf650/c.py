t = int(input())

def givezero(s):
    ans = []
    k = n
    for ss in range(len(s)):
        if s[ss]=="0":
            k+=1
            ans.append(k)
        else:
            k=0
            ans.append(k)
    return ans
        
for i in range(t):
    n, k = [int(x) for x in input().split(" ")]
    s = input()
    f_a = givezero(s)
    f_b = givezero(s[::-1])
    f_b = f_b[::-1]
    ans = 0
    j = 0
    while j < len(f_a):
        if f_a[j]>k and f_b[j]>k:
            ans+=1
            j+=k
        j+=1
    print(ans)