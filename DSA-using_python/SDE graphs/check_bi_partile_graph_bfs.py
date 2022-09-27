
import queue


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



def check_bi_partile_graph_bfs(adj,total_vertex):
    colour=[-1 for i in range(total_vertex)]
    qu=queue.Queue()
    
    for j in range(len(colour)):
        if colour[j]==-1:
            qu.put(j)
            colour[j]=0
            while qu.empty()!=True:
                vertex=qu.get()
                for i in range(total_vertex):
                    if adj[vertex][i]==1:
                        if colour[i]==-1:
                            if colour[vertex]==0:colour[i]=1
                            if  colour[vertex]==1:colour[i]=0
                            qu.put(i)
                        else:
                            if colour[vertex]==colour[i]:return False
                print(colour)
    return True

g=graph(7)
g.addEdge(0,1)
g.addEdge(1,2)    
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(5,6)
g.addEdge(0,4)

print(check_bi_partile_graph_bfs(g.adjMatrix,g.vertex))


