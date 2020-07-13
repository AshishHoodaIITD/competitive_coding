t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    count_odd = 0
    count_even = 0
    count_irr = 0
    for j, aa in enumerate(a):
        if aa%2==0:
            count_even+=1
            if j%2!=0: count_irr+=1
        else:
            count_odd+=1
            if j%2==0: count_irr+=1
    if n%2==0:
        if count_even!=count_odd:
            print(-1)
        else:
            print(int(count_irr/2))
    else:
        if count_even!=count_odd+1:
            print(-1)
        else:
            print(int(count_irr/2))