import math
t = int(input())
for i in range(t):
    inp = input()
    count0 = 0
    count1 = 0
    dp0 = [0]
    dp1 = [0]
    for inpp in inp:
        if inpp == "1":
            count1+=1
        elif inpp == "0":
            count0+=1
        dp0.append(count0)
        dp1.append(count1)
    minop = len(inp)
    for i in range(len(inp)+1):
        l1 = dp1[i]
        l0 = dp0[i]
        r1 = dp1[-1] - dp1[i]
        r0 = dp0[-1] - dp0[i]
        minop = min(minop, l1+r0, l0+r1, l1+r1, l0+r0)
    print(minop)
