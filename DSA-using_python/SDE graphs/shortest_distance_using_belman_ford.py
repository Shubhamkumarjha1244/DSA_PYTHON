import sys
class directed_graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjMatrix=[[0 for i in range(vertex)] for j in range(vertex)]

    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt

    def removeedge(self,v1,v2):
        if self.containEdge(v1,v2)!=True:return
        self.adjMatrix[v1][v2]=0



def belman_ford(adj,vertex_no):
    in_degree={}
    for i in range(vertex_no):in_degree[i]=[]
    for i in range(vertex_no):
        for j in range(vertex_no):
            if adj[i][j]!=0:in_degree[j].append(i)
    distance=[sys.maxsize for i in range(vertex_no)]
    distance[0]=0
    for i in range(vertex_no-1):
        for j in range(vertex_no):
            for ele in in_degree[j]:
                if distance[ele]+adj[ele][j]<distance[j]:distance[j]=distance[ele]+adj[ele][j]
    return distance




g=directed_graph(6)
g.addEdge(0,1,5)
g.addEdge(1,2,-2)
g.addEdge(2,4,3)
g.addEdge(3,4,-2)
g.addEdge(5,3,-2)
g.addEdge(1,5,-3)
print(belman_ford(g.adjMatrix,g.vertex))
    

