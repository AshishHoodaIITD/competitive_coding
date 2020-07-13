import math
T = int(input())
for i in range(T):
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    h, c, t = inp[0], inp[1], inp[2]
    x = float(h+c)/2
    least_count = 2*float(1/x)
    num = math.floor(float(x)/float(t))
    print("num",num)
    vol = []
    if num % 2==0:
        vol.append((num-1, x/float(num-1)))
        vol.append((num+1, x/float(num-1)))
    else:
        vol.append((num-2, x/float(num-2)))
        vol.append((num+2, x/float(num+2)))
        vol.append((num, x/float(num)))
    min_index = -1
    min_val = 10000000
    for v in vol:
        if v[0] < 0: continue
        print(v[0], v[1])
        if math.fabs(v[1]-t) < min_val:
            min_index = v[0]
            min_val = math.fabs(v[1]-t)
    if min_index == 1:
        min_index = 2
    print(min_index)


