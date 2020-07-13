t = int(input())

def process_array(b):
    partial_sum = [0 for i in range(len(b))]
    placement = [0 for i in range(len(b))]
    for i in range(len(b)):
        matches = [j for j in range(len(b)) if b[j]==partial_sum[j]]
        if len(matches)==0:
            break
        for m in matches:
            partial_sum[m] = -1
            placement[m] = i
        for j in range(len(b)):
            if partial_sum[j]>=0:
                for m in matches:
                    partial_sum[j] += abs(j-m)
    return placement

for i in range(t):
    s = input()
    m = int(input())
    b = [int(x) for x in input().split(" ")]

    placement = process_array(b)
    #print("placement",placement)
    dic = {}
    for ss in range(len(s)):
        if s[ss] not in dic:
            dic[s[ss]]=1
        else:
            dic[s[ss]]+=1
    #print("dic",dic)
    d_k = list(dic.keys())
    d_k = sorted(d_k, reverse=True)
    b_d = {}
    for bb in placement:
        if bb not in b_d:
            b_d[bb]=1
        else:
            b_d[bb]+=1
    #print("b_d",b_d)
    b_k = list(b_d.keys())
    b_k = sorted(b_k)
    count_list = [b_d[x] for x in b_k]
    #print("count_list",count_list)
    ans_k = []
    d_iter = 0
    for c in count_list:
        while dic[d_k[d_iter]]<c:
            d_iter+=1
        ans_k.append(d_k[d_iter])
        d_iter+=1
    
    ans = [0 for j in range(len(placement))]
    for j in range(len(ans)):
        ans[j] = ans_k[placement[j]]
    print("".join(ans))

