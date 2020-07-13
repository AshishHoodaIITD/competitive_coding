import math
t = int(input())

def smallestDivisor(n): 
  
    # if divisible by 2 
    if (n % 2 == 0): 
        return 2; 
  
    # iterate from 3 to sqrt(n) 
    i = 3;  
    while(i * i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
  
    return n; 

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) / gcd(a,b)

def maxPrimeFactor(n):
   # number must be even
   while n % 2 == 0:
      max_Prime = 2
      n /= 1
   # number must be odd
   for i in range(3, int(math.sqrt(n)) + 1, 2):
      while n % i == 0:
         max_Prime = i
         n = n / i
   # prime number greator than two
   if n > 2:
      max_Prime = n
   return int(max_Prime)

def opt_pair(n):
    if n%2==0:
        return int(n/2), int(n/2)
    else:
        smallest_prime = smallestDivisor(n)
        #print(smallest_prime)
        rest = int(n/smallest_prime)
        return rest, rest*(smallest_prime-1)

for i in range(t):
    n = int(input())
    a,b = opt_pair(n)
    print(str(a)+" "+str(b))