def travel_1(r, c):
    if c!=1:
        for k in range(c,0,-1):
            print(str(r)+" "+str(k))
        c = 0
    else:
        for k in range(1,r+1):
            print(str(r)+" "+str(k))
        c = r
    return r+1, c+1

def travel_skip_n(r,c,sk):
    if c!=1:
        delta=1
        for j in range(sk):
            for i in range(sk-j):
                print(str(r)+" "+str(c))
                if i!=(sk-j-1):
                    c+=delta
                    r+=delta
            if j!=(sk-1):
                if delta == -1:
                    delta = 1
                    r+=1
                else:
                    c-=1
                    delta = -1
        r+=1
        while(1):
            print(str(r)+" "+str(c))
            if c==1: break
            c-=1
        return r+1, c
    else:
        delta = 1
        for j in range(sk):
            for i in range(sk-j):
                print(str(r)+" "+str(c))
                if i!=(sk-j-1):
                    r+=delta
            if j!=(sk-1):
                if delta == -1:
                    delta = 1
                    r+=1
                    c+=1
                else:
                    c+=1
                    delta = -1
        r+=1
        c+=1
        while(1):
            print(str(r)+" "+str(c))
            if c==r: break
            c+=1
        return r+1,c+1

t= int(input())
for p in range(t):
    n = int(input())
    print("Case #"+str(p+1)+":")
    binary_rep = "{0:b}".format(n)
    binary_rep = binary_rep[::-1]
    r,c = 1,1
    i=0
    while(i<len(binary_rep)):
        if binary_rep[i]=='1':
            r,c = travel_1(r,c)
            i+=1
        else:
            k=0
            while(binary_rep[i+k]=='0'):
                k=k+1
            r,c = travel_skip_n(r,c,k)
            i+=(k+1)


