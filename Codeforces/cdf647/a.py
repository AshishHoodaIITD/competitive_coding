import math
import sys
t = int(input())

def two_ana(num):
    count = 0
    while(num%2==0):
        num = num >> 1
        count+=1
    return num, count
for i in range(t):
    inp = input().split(" ")
    a, b = int(inp[0]), int(inp[1])
    a_rem, a_pow = two_ana(a)
    b_rem, b_pow = two_ana(b)
    if a_rem!=b_rem:
        print(-1)
        continue
    diff = abs(a_pow - b_pow)
    print(int(diff/3) + int(int(diff%3)/2) + int(int(diff%3)%2))