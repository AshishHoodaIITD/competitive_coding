import math
def primeFactors(n): 
    ans = set()
    on = n
    while (n % 2) == 0: 
        ans.add(2)
        n = int(n / 2)

    for i in range(3,int(math.sqrt(n))+1,2): 
        if len(ans)>=3:
            return ans
        while (n % i) == 0: 
            ans.add(i) 
            n = int(n / i) 
    if n > 2 and n!=on: 
        ans.add(n)   
    return ans
n = int(input())

nums = [int(x) for x in input().split(" ")]
first, second = [], []
for n in nums:
    ans = list(primeFactors(n))
    if len(ans)==2:
        if math.gcd(ans[0]+ans[1],n)==1:
            first.append(ans[0])
            second.append(ans[1])
            continue
    if len(ans)>=3:
        first.append(ans[-1])
        second.append(ans[-2])
    else:
        first.append(-1)
        second.append(-1)
print(" ".join([str(f) for f in first]))
print(" ".join([str(s) for s in second]))

