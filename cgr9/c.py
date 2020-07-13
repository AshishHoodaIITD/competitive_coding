
t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    
    if a[-1] <= a[0]:
        #print(base)
        print("NO")
    else:
        #print(base)
        print("YES")
            
