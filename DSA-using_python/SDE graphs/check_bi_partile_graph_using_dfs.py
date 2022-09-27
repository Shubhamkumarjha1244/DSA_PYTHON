class graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjMatrix=[[0 for i in range(vertex)] for j in range(vertex)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeedge(self,v1,v2):
        if self.containEdge(v1,v2)!=True:return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0






def dfs_helper(st,adj,total_vertex,color):
    for i in range(total_vertex):
        if adj[st][i]==1:
            if color[i]==-1:
                color[i]=1-color[st]
                if dfs_helper(i,adj,total_vertex,color)==False:return False
            else:
                if color[i]==color[st]:return False
    return True

def checkBipartileGraphUsingdfs(adj,total_vertex):
    color=[-1 for i in range(total_vertex)]
    for i in range(total_vertex):
        if color[i]==-1:
            color[i]=0
            if dfs_helper(i,adj,total_vertex,color)==False:return False
    return True



g=graph(4)
g.addEdge(0,1)
g.addEdge(1,2)    
g.addEdge(2,3)
g.addEdge(0,2)
g.addEdge(0,3)

print(checkBipartileGraphUsingdfs(g.adjMatrix,g.vertex))

    