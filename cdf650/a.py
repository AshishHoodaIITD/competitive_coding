t = int(input())
def halfs(s):
    ans = ""
    for ss in range(len(s)):
        if ss%2==0:
            ans = ans + s[ss]
    return ans
for i in range(t):
    s = input()
    ans = s[0]+halfs(s[1:-1])+s[-1]
    print(ans)