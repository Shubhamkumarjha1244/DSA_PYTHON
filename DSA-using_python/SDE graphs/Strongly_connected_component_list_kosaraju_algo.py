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



def dfs_topo(start,adj,vertex_no,visited,st):
    visited[start]=True
    for i in range(vertex_no):
        if adj[start][i]==1 and visited[i]==False:
            dfs_topo(i,adj,vertex_no,visited,st)
    st.appendleft(start)
    return
def losely_topo_sort(adj,vertex_no):
    visited=[False for i in range(vertex_no)]
    st=collections.deque()
    for i in range(vertex_no):
        if visited[i]==False:
            dfs_topo(i,adj,vertex_no,visited,st)
    return list(st)






def transpose_graph(adj,vertex_no):
    trans=[[adj[j][i] for j in range(vertex_no)] for i in range(vertex_no)]
    return trans





def dfs_helper(start,adj,vertex_no,visited,ans):
    visited[start]=True
    for i in range(vertex_no):
        if adj[start][i]==1 and visited[i]==False:
            dfs_helper(i,adj,vertex_no,visited,ans)
    ans.append(start)
    return

def strongly_connected_component(adj,vertex_no):            ##kosaRaju algo
    topo_sort=losely_topo_sort(adj,vertex_no)
    transpose_grap=transpose_graph(adj,vertex_no)
    visited=[False for i in range(vertex_no)]
    for i in topo_sort:
        if visited[i]==False:
            ans=[]
            dfs_helper(i,transpose_grap,vertex_no,visited,ans)
            print(ans)


g=directed_graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(3,1)
g.addEdge(3,4)
strongly_connected_component(g.adjMatrix,g.vertex)