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

    def dfs(self):                         
        self.visited_dfs=[False for i in range(self.vertex)]
        for start in range(self.vertex):        #logic for all disconnected graph
            if self.visited_dfs[start]==False:
                self.dfs_helper(start)



    def bfs_helper(self,start):
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
    def bfs(self):
        self.visited_bfs=[False for i in range(self.vertex)]
        for start in range(self.vertex): #logic for all disconnected graph
            if self.visited_bfs[start]==False:
                self.bfs_helper(start)



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

    def has_path_helper(self,v1,v2):
        if v1>=self.vertex or v2>=self.vertex:return False
        if self.adjMatrix[v1][v2]==1 :
            return True
        self.visited[v1]=True
        ans=False
        for i in range(self.vertex):
            if self.adjMatrix[v1][i]==1 and self.visited[i]==False:
                ans=(self.has_path_helper(i,v2) or ans)
        return ans
        
    def has_path(self,v1,v2):
        self.visited=[False for i in range(self.vertex)]
        return  self.has_path_helper(v1,v2)

    def get_path_helper_up_to_down(self,v1,v2,ans):
        if self.adjMatrix[v1][v2]==1:
            ans.append(v1)
            ans.append(v2)
            self.out.append(ans)
            return
        self.visited_getPath[v1]=True
        for i in range(self.vertex):
            if self.adjMatrix[v1][i]==1 and self.visited_getPath[i]==False:
                self.get_path_helper_up_to_down(i,v2,ans+[v1])





    def dfs_path_helper(self,v1,v2):
        if self.adjMatrix[v1][v2]==1:
                ans=[]
                ans.append(v2)
                ans.append(v1)
                self.visited[v2]=True
                self.visited[v1]=True
                return ans
        self.visited[v1]=True
        for i in range(self.vertex):
            if self.adjMatrix[v1][i]==1 and self.visited[i]==False:
                self.visited[i]=True
                temp=self.dfs_path_helper(i,v2)
                if temp:
                    temp.append(v1)
                    return temp
    def dfs_path(self,v1,v2):
        self.visited=[False for i in range(self.vertex)]
        return self.dfs_path_helper(v1,v2)

    def bfs_get_path(self,v1,v2):
        dic={}
        qu=queue.Queue()
        visited=[False for i in range(self.vertex)]
        qu.put(v1)
        while qu.empty()!=True:
            vertex=qu.get()
            visited[vertex]=True
            for i in range(self.vertex):
                if self.adjMatrix[vertex][i]==1 and visited[i]==False:
                    if i not in dic.keys():dic[i]=vertex
                    qu.put(i)
                    if i==v2:break
        ans=[]
        ans.append(v2)
        key=v2
        while True:
            key=dic[key]
            ans.append(key)
            if key==v1:break
        return ans
    def is_Connected_graph_helper(self,start):
        self.visited[start]=True
        for i in range(self.vertex):
            if self.adjMatrix[start][i]==1 and self.visited[i]==False:
                self.is_Connected_graph_helper(i)
    def is_Connected_graph(self):
        self.visited=[False for i in range(self.vertex)]
        self.is_Connected_graph_helper(0)
        if all(self.visited):return True
        else:return False
    
    def connected_component(self):
        visited=[False for ele in range(self.vertex)]
        ans=[]
        for i in range(self.vertex):
            if visited[i]==False:
                qu=queue.Queue()
                graph=[]
                qu.put(i)
                visited[i]=True
                graph.append(i)
                while qu.empty()!=True:
                    vertex=qu.get()
                    for j in range(self.vertex):
                        if self.adjMatrix[vertex][j]==1 and visited[j]==False:
                            qu.put(j)
                            visited[j]=True
                            graph.append(j)
                ans.append(graph)
        return ans

        


    





    


 




g=graph(7)
# g.addEdge(0,1)
g.addEdge(0,2)
# g.addEdge(0,3)
g.addEdge(1,5)
g.addEdge(2,4)
# g.addEdge(5,6)
g.addEdge(4,6)
g.printgraph()
g.dfs()
print('----*******-----')
g.bfs()
print('----****has_path***-----')
print(g.has_path(5,7))
print('----****get_path***-----')
# print(g.dfs_path(0,3))
# print(g.bfs_get_path(0,3))
print(g.is_Connected_graph())
print(g.connected_component())