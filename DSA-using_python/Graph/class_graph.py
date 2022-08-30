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

    def containEdge(self,v1,v2):
        return self.adjMatrix[v1][v2]==1



    def dfs_helper(self,ver):
        print(ver)
        self.visited_dfs[ver]=True
        for i in range(self.vertex):
            if self.adjMatrix[ver][i]==1 and self.visited_dfs[i]==False:
                self.dfs_helper(i)

    def dfs(self,start):
        self.visited_dfs=[False for i in range(self.vertex)]
        self.dfs_helper(start)



    def bfs(self,start):
        self.visited_bfs=[False for i in range(self.vertex)]
        qu=queue.Queue()
        qu.put(start)
        self.visited_bfs[start]=True
        while qu.empty()!=True:
            ver=qu.get()
            print(ver)
            for i in range(self.vertex):
                if self.adjMatrix[ver][i]==1 and self.visited_bfs[i]==False:
                    qu.put(i)
                    self.visited_bfs[i]=True

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




g=graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(4,3)
g.addEdge(1,3)
g.printgraph()
g.dfs(0)
print('----*******-----')
g.bfs(0)