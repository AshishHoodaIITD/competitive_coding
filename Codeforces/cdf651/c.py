def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
    return True

t = int(input())
for i in range(t):
    n = int(input())
    win = "Ashishgup"
    loss = "FastestFinger"
    if n==1:
        print(loss)
    elif n==2:
        print(win)
    elif isPowerOfTwo(n):
        print(loss)
    elif n%2==1:
        print(win)
    elif n%4==0:
        print(win)
    elif isPrime(int(n/2)):
        print(loss)
    else:
        print(win)