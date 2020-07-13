t = int(input())

def load_dp():
    dp = [0,0,4,4,12]
    mod = 1000000007
    wr = [False,False,True,False,False]
    for j in range(2000000-5):
        if wr[-1]==False and wr[-2]==False:
            dp.append((((2*dp[-2])%mod)+dp[-1]+4)%mod)
            wr.append(True)
        else:
            dp.append((((2*dp[-2])%mod)+dp[-1])%mod)
            wr.append(False)
    return dp

dp = load_dp()
for i in range(t):
    n = int(input())
    print(dp[n-1])


