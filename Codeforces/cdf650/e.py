import heapq

def maxheappush(x,xx):
    heapq.heapify(x)
    heapq.heappush(x,-1*xx)

def maxheappop(x):
    heapq.heapify(x)
    ans = -1*heapq.heappop(x)
    return ans

class Graph: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 

def returncount(l):
    dic = {}
    for ss in range(len(l)):
        if l[ss] not in dic:
            dic[l[ss]]=1
        else:
            dic[l[ss]]+=1
    val = list(dic.values())
    val = sorted(val, reverse=True)
    return val

def modlist(x,k):
    vals = []
    it = 1
    g = Graph(x)
    for i in range(x):
        g.addEdge(i, (i+k)%x)
    cc = g.connectedComponents()

    for c in cc:
        vals.append(len(c))
    vals = sorted(vals, reverse = True)
    return vals



def findfeas(b,s):
    c = []
    heapq.heapify(c)
    for bb in b:
        maxheappush(c, bb)
    ans = maxheappop(c)
    while ans >= s[0]:
        ans = ans - s[0]
        s.pop(0)
        maxheappush(c, ans)
        ans = maxheappop(c)
        if len(s)==0: break
    if len(s)==0:
        return True
    else:
        return False

t = int(input())

for i in range(t):
    n,k = [int(x) for x in input().split(" ")]
    s = input()
    rc = returncount(s)
    for j in range(n,0,-1):
        gg = modlist(j,k)
        if findfeas(rc,gg):
            print(j)
            break