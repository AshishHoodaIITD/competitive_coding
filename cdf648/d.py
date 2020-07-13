
t = int(input())

def find_occur(grid):
    g_count = 0
    b_count = 0
    hash_count = 0
    for r in grid:
        for c in r:
            if c == "G": 
                g_count+=1
            elif c == "B":
                b_count+=1
            elif c == "#":
                hash_count+=1
    return g_count, b_count, hash_count

def bound_B(grid):
    flag = True
    hash_updates = 0
    updates = [(0,0), (-1,0), (1,0), (0,1),(0,-1)]
    update_list = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "B":
                for up in updates:
                    if r+up[0] >= 0 and r+up[0] < len(grid) and c+up[1] >= 0 and c+up[1] < len(grid[0]):
                        update_list.append((r+up[0], c+up[1]))
    for r,c in update_list:
        if grid[r][c] == "G":
            flag = False
            break
        else:
            grid[r][c] = "#"
            hash_updates+=1
    return flag, grid, hash_updates

def findch(grid, ch, depth):
    updates = [(-1,0), (1,0), (0,1),(0,-1)]
    queue = [(len(grid)-1, len(grid[0])-1)]
    visited = set()
    g_count = 0
    if grid[len(grid)-1][len(grid[0])-1] == "#":
        return g_count
    visited.add((len(grid)-1, len(grid[0])-1))
    while(len(queue)>0):
        r,c = queue.pop(0)
        if grid[r][c] == ch: g_count+=1
        if depth == 0:
            continue
        for up in updates:
            if r+up[0] >= 0 and r+up[0] < len(grid) and c+up[1] >= 0 and c+up[1] < len(grid[0]):
                if grid[r+up[0]][c+up[1]] != "#":
                    if (r+up[0], c+up[1]) not in visited:
                        queue.append((r+up[0], c+up[1]))
                        visited.add((r+up[0], c+up[1]))
        depth -= 1
    return g_count
        
for i in range(t):
    n, m = [int(x) for x in input().split(" ")]
    grid = []
    for j in range(n):
        temp = list(input())
        grid.append(temp)
    g_count, b_count, hash_count = find_occur(grid)
    #print("g_count", g_count)
    #print("b_count", b_count)
    if g_count == 0:
        if grid[-1][-1] == "#" or grid[-1][-1]==".":
            print("Yes")
            continue
        b_found = findch(grid, "B", 1)
        if b_found > 0:
            print("No")
            continue
        print("Yes")
        continue
    if grid[-1][-1] == "#":
        print("No")
        continue
    status, grid, hash_updates = bound_B(grid)
    if status == False:
        print("No")
        continue
    hash_count+=hash_updates
    if hash_count==0:
        print("Yes")
        continue
    g_found = findch(grid, "G", 10000)
    if g_count == g_found:
        print("Yes")
    else:
        print("No")