import bisect
inp = input().split(" ")
n = int(inp[0])
x = int(inp[1])
d_array = [int(x) for x in input().split(" ")]

def cal_cost(i, end_month):
    if i!=0:
        v = cost_cum[end_month-1]-cost_cum[i-1]
    else:
        v = cost_cum[end_month-1]
    return v

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    return -1

cost_cum = []
t = 0
max_val = 0
cummulative_d = [0]
for d in d_array:
    cummulative_d.append(cummulative_d[-1] + d)
    t = t+int((d*(d+1))/2)
    cost_cum.append(t)

for d in d_array:
    cummulative_d.append(cummulative_d[-1] + d)
    t = t+int((d*(d+1))/2)
    cost_cum.append(t)
print(cost_cum)
for i in range(len(cummulative_d)-1):
    print(cummulative_d, cummulative_d[i]+ x)
    end_month = find_ge(cummulative_d, cummulative_d[i]+ x)
    if end_month == -1:
        break
    #shift
    shift_dis = min(cummulative_d[i]-cummulative_d[i-1], cummulative_d[end_month] - cummulative_d[i] - x)
    shift_offset = cummulative_d[i]+ x - cummulative_d[end_month-1]

    max_val = max(max_val, cal_cost(i, end_month) + shift_dis*shift_offset)
    print(i, end_month, shift_dis, shift_offset, cal_cost(i, end_month) + shift_dis*shift_offset)
print(max_val)
