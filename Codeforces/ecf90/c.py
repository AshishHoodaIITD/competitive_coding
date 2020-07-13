t = int(input())

def get_cumm(s):
    cur = 0
    ans = []
    for ss in s:
        if ss=="-":
            cur-=1
        else: cur+=1
        ans.append(cur)
    return ans

for i in range(t):
    s = input()
    cum = get_cumm(s)
    min_stack = []
    for j,c in enumerate(cum):
        if len(min_stack)==0:
            if c<0:
                min_stack.append([j,c])
        elif c<min_stack[-1][1]:
            min_stack.append([j,c])
    
    ans = 0
    cur = 0
    for v in min_stack:
        ans += (v[0]+1)*(abs(v[1])-cur)
        cur = abs(v[1])
    print(ans+len(s))
    