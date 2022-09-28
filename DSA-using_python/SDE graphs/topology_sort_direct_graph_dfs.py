import collections
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





def dfs_helper(start,adj,vertex,visited,st):
    visited[start]=True
    for i in range(vertex):
        if adj[start][i]==1 and visited[i]==False:
            dfs_helper(i,adj,vertex,visited,st)
    st.appendleft(start)
    return

def topology_sort_dfs(adj,vertex):
    st=collections.deque()
    visited=[False for i in range(vertex)]
    for i in range(vertex):
        if visited[i]==False:
            dfs_helper(i,adj,vertex,visited,st)
    return list(st)






g=directed_graph(5)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(1,0)
g.addEdge(1,3)
g.addEdge(4,3)
topo=topology_sort_dfs(g.adjMatrix,g.vertex)
print(topo)