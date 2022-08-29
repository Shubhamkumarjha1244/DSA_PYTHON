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




g=graph(7)
g.addEdge(0,1)
g.addEdge(2,3)
g.addEdge(4,3)
g.addEdge(1,6)
g.printgraph()