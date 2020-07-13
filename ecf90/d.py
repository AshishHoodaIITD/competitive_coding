t = int(input())

def forward_pass(x):
    n_a = [x[i+1]-x[i] for i in range(0,len(x)-1,2)]
    m = 0
    c = 0
    for n in n_a:
        c += n
        if c<0: c=0
        m = max(m,c)
    return m

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]

    ans = sum([x for i,x in enumerate(a) if i%2==0])
    if len(a)%2==0:
        rev = a[:-1]
    else:
        rev = a
    ans += max(forward_pass(a), forward_pass(rev[::-1]))
    print(ans)