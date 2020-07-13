import math
t = int(input())

for i in range(t):
    ii = input().split(" ")
    ii = [int(iii) for iii in ii]
    a = ii[0]
    b = ii[1]
    c = ii[2]
    d = ii[3]
    if a <= b:
        print(b)
        continue
    if d >= c:
        print("-1")
        continue
    time_taken = b + c*math.ceil((a-b)/(c-d))
    print(time_taken)