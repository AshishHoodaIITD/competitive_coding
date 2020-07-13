t = int(input())

for i in range(t):
    rc = [int(x) for x in input().split(" ")]
    columns = []
    for j in range(rc[1]):
        columns.append([])
    for k in range(rc[0]):
        for si, s in enumerate(input()):
            columns[si].append(s)
    d = {}
    for col in columns:
        for c in range(len(col)):
            if c != len(col)-1:
                if col[c] not in d:
                    d[col[c]] = set()
                if col[c+1]!=col[c]:
                    d[col[c]].add(col[c+1])
            else:
                if col[c] not in d:
                    d[col[c]] = set()
    visited = set()
    ans = ""
    while(len(visited)<len(d.keys())):
        prior = len(visited)
        for key in d:
            if key in visited: continue
            if len(d[key].intersection(visited)) == len(d[key]):
                ans = ans + key
                visited.add(key)
        if prior == len(visited):
            ans = "-1"
            break
    
    print("Case #"+str(i+1)+": "+ans)
        