import queue
import class_graph



def detectCycle(vertex,adj):
    visited=[False for i in range(vertex)]
    qu=queue.Queue()
    start=0
    qu.put(start)
    visited[0]=True
    while qu.empty()!=True:
        pts=qu.get()
        for j in range(vertex):
            if adj[pts][j]==1:
                if visited[j]==True:
                    return True
                qu.put(j)
                visited[j]=True
    return False


    
g=class_graph.graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(1,3)
g.addEdge(4,3)
g.addEdge(4,2)
print(g.connected_component())
print(detectCycle(g.vertex,g.adjMatrix))