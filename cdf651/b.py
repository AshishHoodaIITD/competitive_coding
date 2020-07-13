t = int(input())

def swap(a,b):
    if len(a)>len(b):
        return b,a 
    else:
        return a,b

def printcomb(a,b):
    a, b = swap(a,b)
    for i in range(0,len(a),2):
        print(a[i]+1, a[i+1]+1)
    
    for i in range(0,len(b),2):
        print(b[i]+1, b[i+1]+1)
        

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    odd_index = [j for j,x in enumerate(a) if x%2==1]
    even_index = [j for j,x in enumerate(a) if x%2==0]
    if len(odd_index)%2==0:
        if len(odd_index)>=2:
            printcomb(odd_index[:-2], even_index)
        else:
            printcomb(odd_index, even_index[:-2])
    else:
        printcomb(odd_index[:-1], even_index[:-1])
