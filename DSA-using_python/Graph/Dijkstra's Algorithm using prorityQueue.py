import heapq
import queue,sys


class weight_graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjMatrix=[[0 for i in range(vertex)] for j in range(vertex)]
        self.edge=0

    def addEdge(self,v1,v2,weight):
        self.adjMatrix[v1][v2]=weight
        self.adjMatrix[v2][v1]=weight
        self.edge+=1

    def removeedge(self,v1,v2):
        if self.containEdge(v1,v2)!=True:return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
        self.edge-=1


    def dijistra_algo(self):
        visited=[False for i in range(self.vertex)]
        distance=[sys.maxsize for i in range(self.vertex)]
        distance[0]=0
        heap=[(0,0)]
        for i in range(self.vertex-1):
            pop_vertex=heapq.heappop(heap)
            while visited[pop_vertex[1]]!=False:
                pop_vertex=heapq.heappop(heap)
            min_vertex=pop_vertex[1]
            visited[min_vertex]=True
            for j in range(self.vertex):
                if self.adjMatrix[min_vertex][j]!=0 and visited[j]!=True:
                    if distance[j]>self.adjMatrix[min_vertex][j]+distance[min_vertex]:
                        distance[j]=self.adjMatrix[min_vertex][j]+distance[min_vertex]
                        heapq.heappush(heap,(distance[j],j))     
        for i in range(1,len(distance)):print(str(i),str(distance[i]))

                    
        
                    



        


    





    


 




g=weight_graph(5)
g.addEdge(0,1,4)
g.addEdge(1,2,2)
g.addEdge(0,2,8)
g.addEdge(2,3,3)
g.addEdge(1,3,6)
g.addEdge(4,3,5)
g.addEdge(4,2,92)
g.dijistra_algo()