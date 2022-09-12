class edge_class:
    def __init__(self,v1,v2,edge):
        self.v1=v1
        self.v2=v2
        self.edge=edge


class Kruskal_alo:
    def __init__(self,edge_no,vertex_no):
        self.edge_arr=[]
        self.edge_no=edge_no
        self.vertex_no=vertex_no
        self.union=[i for i in range(self.vertex_no)]


    def edge_add(self,edge):
        self.edge_arr.append(edge) 


    def findparent(self,i):
        if self.union[i]==i:return i
        return self.findparent(self.union[i])

    def kruskal_alo(self):
        self.edge_arr.sort(key=lambda k:k.edge,reverse=True)
        count=0
        ans=[]
        while count<(self.vertex_no-1):
            temp=self.edge_arr.pop()
            v1=temp.v1
            v2=temp.v2
            weight=temp.edge
            if self.findparent(v1)!=self.findparent(v2):
                print(self.findparent(v1),self.findparent(v2))
                count+=1
                if v1>v2:
                    ans.append([v2,v1,weight])
                else:ans.append([v1,v2,weight])
                self.union[self.findparent(v1)]=self.findparent(v2) 
        return ans


k=Kruskal_alo(4,4)
k.edge_add(edge_class(0,1,3))
k.edge_add(edge_class(0,3,5))
k.edge_add(edge_class(1,2,1))
k.edge_add(edge_class(2,3,8))
print(k.kruskal_alo())
        

