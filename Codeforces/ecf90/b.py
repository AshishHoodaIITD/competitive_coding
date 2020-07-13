t = int(input())
for i in range(t):
    s = input()
    one_count = len([x for x in s if x=='1'])
    zero_count = len([x for x in s if x=='0'])
    m = min(one_count, zero_count)
    if m%2==0:
        print("NET")
    else:
        print("DA")