import math
import datetime
t = 1#int(input())
def findSubarraySum(arr, n, ps):  
    prevSum = {}
    res = 0  
    currsum = 0 
    pSum = 0
    for i in range(0, n):   
        currsum += arr[i]  
        if arr[i]>0: pSum+=arr[i]
        up = int(math.sqrt(100*i))+100 
        if currsum in ps[:up]:   
            res += 1 
        for Sum in ps[:up]:  
            if Sum > pSum:
                break     
            if (currsum - Sum) in prevSum: 
                res += prevSum[currsum - Sum]  
        if currsum not in prevSum:
            prevSum[currsum] = 0
        prevSum[currsum] += 1    
    return res  
ps = []
for j in range(10000):
    ps.append(j*j)
inp = []
for j in range(1000):
    inp.append(j%100)
init = datetime.datetime.now()
for i in range(t):
    #n = int(input())
    #nums = [int(x) for x in input().split(" ")]
    nums = inp
    count = 0
    up = int(math.sqrt(100*len(nums)))+100
    count+=findSubarraySum(nums, len(nums), ps[:up]) 
    print("Case #"+str(i+1)+": "+str(count))
print(datetime.datetime.now() - init)