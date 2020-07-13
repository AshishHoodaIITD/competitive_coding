import sys

def readKth(k):
    print(k)
    sys.stdout.flush()
    return input()

def submitAns(ans):
    print(ans)
    sys.stdout.flush()
    output = input()
    assert output == 'Y'

def main():
    inp = input().split(" ")
    t = int(inp[0])
    b = int(inp[1])
    for i in range(t):
        output = ""
        s_k, d_k = -1, -1
        s_v, d_v = -1, -1
        b_val = [""]*b
        it = 1
        j=0
        while(j<=150):
            if j!=0 and j%10==0:
                if s_k==-1: readKth(1)
                else:   s_v = readKth(s_k)
                if d_k==-1: readKth(1)
                else:   d_v = readKth(d_k)
                j+=2
            f = readKth(it)
            r = readKth(b-it+1)
            j+=2
            if f == r:
                if s_k == -1: 
                    s_k = it
                    s_v = f
                if f == s_v: 
                    b_val[it-1]="s1"
                    b_val[b-it]="s1"
                else:   
                    b_val[it-1]="s2"
                    b_val[b-it]="s2"
            else:
                if d_k == -1: 
                    d_k = it
                    d_v = f
                if f == d_v: 
                    b_val[it-1]="d1"
                    b_val[b-it]="d2"
                else:   
                    b_val[it-1]="d2"
                    b_val[b-it]="d1"
            it+=1
            if it>int(b/2): break
        if s_v==-1: s_v="0"
        if d_v==-1: d_v="0"
        complement = {"1":"0","0":"1"}
        mapper = {"s1":s_v,"s2":complement[s_v], "d1":d_v, "d2":complement[d_v]}
        output = "".join([mapper[x] for x in b_val])
        submitAns(output)
if __name__ == '__main__':
    main()
