def ends(strs, flag):
    sorted_str = sorted(strs, key=lambda x: len(x))
    final_str = ""
    for s in sorted_str:
        if flag==0:
            if s.startswith(final_str)==False:
                return -1
        elif flag==1:
            if s.endswith(final_str)==False:
                return -1
        final_str = s
    return final_str

t = int(input())
for i in range(t):
    n = int(input())
    p = []
    for j in range(n):
        p.append(input())
    p_split = []
    for j in range(n):
        p_split.append(p[j].split("*"))
    
    final_str = ""
    beg = []
    for j in range(n):
        beg.append(p_split[j][0])
    b = ends(beg,0)
    if b==-1:
        print("Case #"+str(i+1)+": *")
        continue
    final_str+=b

    for j in range(n):
        t = "".join(p_split[j][1:-1])
        final_str+=t
    end = []
    for j in range(n):
        end.append(p_split[j][-1])
    e = ends(end,1)
    if e==-1:
        print("Case #"+str(i+1)+": *")
        continue
    final_str+=e

    print("Case #"+str(i+1)+": "+final_str)


