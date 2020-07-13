t = int(input())

for i in range(t):
    n = int(input())
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    inp = sorted(inp)
    max_index = 0
    for i in range(len(inp)):
        if i+1>=inp[i]:
            max_index = i+1
    print(max_index + 1)