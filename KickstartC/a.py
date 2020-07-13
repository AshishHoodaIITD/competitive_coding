t = int(input())

for i in range(t):
    ii = input().split(" ")
    ii = [int(iii) for iii in ii]
    k = ii[1]
    nums = input().split(" ")
    nums = [int(nn) for nn in nums]
    count = 0
    flag = 0
    for n in nums:
        if n == k:
            flag = k
        else:
            if flag!=0:
                if flag==n+1:
                    flag-=1
                    if flag==1:
                        count+=1
                        flag = 0
                else:
                    flag = 0
    print("Case #"+str(i+1)+": "+str(count))