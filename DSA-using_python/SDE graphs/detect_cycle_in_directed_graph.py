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



def detect_cycle(adj,vertex):
    visited=[False for i in range(vertex)]
    neighbour_dfs=[False for i in range(vertex)]
    for i in range(vertex):
        if visited[i]==False:
            if detect_cycle_helper(i,adj,vertex,visited,neighbour_dfs)==True:
                return True
    return False
def detect_cycle_helper(start,adj,vertex,visited,neighbour_dfs):
    visited[start]=True
    neighbour_dfs[start]=True
    for j in range(vertex):
        if adj[start][j]==1 and visited[j]==False:
            if detect_cycle_helper(j,adj,vertex,visited,neighbour_dfs)==True:
                return True
        elif adj[start][j]==1 and neighbour_dfs[j]==True:
            return True
    neighbour_dfs[start]=False
    return False


g=directed_graph(6)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,5)
g.addEdge(3,4)
g.addEdge(0,4)
g.addEdge(2,3)
g.addEdge(4,1)
g.printgraph()
print(detect_cycle(g.adjMatrix,g.vertex))




        


    





    


 




