import math

PI = math.pi

def cot(x):
    return math.cos(x)/math.sin(x)

t = int(input())

for i in range(t):
    n = int(input())
    print(cot(PI/(2*n)))