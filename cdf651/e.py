def stringToUpdate(s,t):
    ans = ""
    for ss in range(len(s)):
        if s[ss]!=t[ss]:
            ans = ans + s[ss]
    return ans

def checkvalid(s):
    one_c = 0
    zero_c = 0
    for ss in range(len(s)):
        if s[ss]=='0': zero_c+=1
        if s[ss]=='1': one_c+=1
    return one_c==zero_c

def maxcons(s,ch):
    maxc = 0
    curr_c = 0
    for ss in range(len(s)):
        if s[ss]==ch:
            curr_c+=1
        else:
            curr_c = 0
        maxc = max(maxc, curr_c)
    return maxc



n = int(input())
s = input()
t = input()
st = stringToUpdate(s,t)
if checkvalid(st):
    print(max(maxcons(st,'1'),  maxcons(st,'0')))
else:
    print(-1)