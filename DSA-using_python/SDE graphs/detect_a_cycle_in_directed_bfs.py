import queue
class directed_graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjMatrix=[[0 for i in range(vertex)] for j in range(vertex)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1

    def removeedge(self,v1,v2):
        if self.containEdge(v1,v2)!=True:return
        self.adjMatrix[v1][v2]=0

    def containEdge(self,v1,v2):
        return self.adjMatrix[v1][v2]==1

    def printgraph(self):
        print('     ',end='')
        for i in range(self.vertex):
            print(i,end='  ')
        print()
        print()
        i=0
        for ele in self.adjMatrix:
            print(i,end='   ')
            print(ele)
            print()
            i+=1


def detect_a_cycle_indirected_bfs(adj,vertex):
    in_degree=[0 for i in range(vertex)]
    for i in range(vertex):
        for j in range(vertex):
            if adj[i][j]==1:
                in_degree[j]+=1
    qu=queue.Queue()
    for i in range(vertex):
        if in_degree[i]==0:
            qu.put(i)
    if qu.empty()==True:return True

    while qu.empty()!=True:
        ele=qu.get()
        for j in range(vertex):
            if adj[ele][j]==1:
                in_degree[j]-=1
                if in_degree[j]==0:qu.put(j)
    if set(in_degree)=={0}:return False
    else:return True



g=directed_graph(6)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(5,1)
g.addEdge(3,4)
g.addEdge(4,0)
g.addEdge(2,3)
g.addEdge(4,1)
print(detect_a_cycle_indirected_bfs(g.adjMatrix,g.vertex))