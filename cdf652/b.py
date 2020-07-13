t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    pre_zero = 0
    post_one = 0
    rem = ""
    j = 0
    while j<len(s) and s[j]=='0':
        j+=1
    pre_zero = j
    j = len(s)-1
    while j>=0 and s[j]=='1':
        j-=1
    post_one = len(s)-1-j
    rem = s[pre_zero:len(s)-post_one]
    #print(pre_zero, post_one, rem)
    if len(rem)>0:
        rem = '0'
    else:
        rem = ''
    print(''.join(['0']*pre_zero)+rem+''.join(['1']*post_one))