class edge:
    def __init__(self,v1,v2,weight):
        self.v1=v1
        self.v2=v2
        self.weight=weight

def find_parent(parent,i):
    if parent[i]==i:return i
    find_parent(parent,parent[i])


def kruskal_algo(edge_arr,vertex_no):
    edge_arr.sort(reverse=True,key=lambda a:a.weight)
    parent=[i for i in range(vertex_no)]
    count=0
    ans=[]
    while count<vertex_no-1:  #mst me edge ka no (vertex ka no -1) hota hai,iska matlab agar 5 vertex  hai to usko 4 edge se mst banaya jayega
        edge=edge_arr.pop()
        start=edge.v1
        end=edge.v2
        weight=edge.weight
        if find_parent(parent,start)!=find_parent(parent,end):
            parent[find_parent(parent,end)]=start
            if start<end:
                ans.append([start,end,weight])
            else:ans.append([end,start,weight])
            count+=1
    return ans
    
















ver_ed_arr=[int(ele) for ele in input().split(' ')]
vertex_no=ver_ed_arr[0]
edge_no=ver_ed_arr[1]
edge_arr=[]

for i in range(vertex_no):
    edge_input=[int(ele) for ele in input().split(' ')]
    edge_arr.append(edge(edge_input[0],edge_input[1],edge_input[2]))
print(kruskal_algo(edge_arr,vertex_no))

    
