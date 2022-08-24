import queue
class genericTree:
    def __init__(self,val):
        self.data=val
        self.children=[]


class generic_tree_class:
    def printgenericTree(self,root):
        if root==None:return #this for edge case not base case
        print(root.data,end=':')
        for child in root.children:
            print(child.data,end=',')
        print()
        for child in root.children: #this is base case as At leaf loof will not run and it automatically return
            self.printgenericTree(child)
    
    def inputgenericTree_without_num_children(self):
        val=int(input())
        if val==-1:return
        root=genericTree(val)
        while True:
            child=self.inputgenericTree_without_num_children() #for that generic sub_tree
            if child==None:break  #jab none aane laga matlab aab aur child nahi hai
            root.children.append(child)
        return root
    def inputgenericTree(self):
        root_val=int(input('Enter value : '))
        if root_val==-1:return
        root=genericTree(root_val)

        no_children=int(input('Enter number of children of '+str(root_val)+':'))
        for i in range(no_children):
            print("Enter value of",i+1 ,"th child of ",root_val,' : ')
            child=self.inputgenericTree()
            root.children.append(child)
        return root
    
    def no_of_node(self,root):
        if root==None:return 0
        child_no=0
        for child in root.children:
            child_no+=self.no_of_node(child)
        return 1+child_no
    def sum_of_children(self,root):
        if root==None:return 0
        child_sum=root.data
        for  child in root.children:
            child_sum+=self.sum_of_children(child)
        return child_sum

    def height_of_generic_tree(self,root):
        if root==None:return 0
        child_height=0
        for child in root.children:
            child_height=max(child_height,self.height_of_generic_tree(child))
        return 1+child_height

    def largest_node(self,root):
        if root==None:return 0
        largest=root.data
        for child in root.children:
            largest=max(largest,self.largest_node(child))
        return largest
    def level_wise_input(self):
        root_val=int(input('Enter value of root'))
        if root_val==-1:return
        root=genericTree(root_val)
        qu=queue.Queue()
        qu.put(root)
        while qu.empty()!=True:
            node=qu.get()
            no_children=int(input('Enter no of children of '+str(node.data)+' : '))
            for i in range(no_children):
                child_val=int(input('Enter value of child of '+str(node.data)+' : '))
                child=genericTree(child_val)
                node.children.append(child)
                qu.put(child)
        return root

    def print_levelwise(self,root):
        if root==None:return
        qu=queue.Queue()
        qu.put(root)
        while qu.empty()!=True:
            node=qu.get()
            print(node.data,end=' : ')
            for child in node.children:
                print(child.data,end=',')
                qu.put(child)
            print()
        
            



            



    


n1=genericTree(6)
n2=genericTree(2)
n3=genericTree(8)
n4=genericTree(7)
n5=genericTree(1)
n6=genericTree(11)
n7=genericTree(20543)
n8=genericTree(9)
n9=genericTree(6)
n10=genericTree(5)
n11=genericTree(3)
n12=genericTree(12)
n1.children=[n2,n3,n4,n5]
n3.children=[n6,n7,n11]
n6.children=[n8,n9,n10]
n10.children=[n12]

# root=gt.inputgenericTree()
gt=generic_tree_class()
root=gt.level_wise_input()
gt.printgenericTree(root)
print(gt.no_of_node(root))
print(gt.sum_of_children(root))
print(gt.height_of_generic_tree(root))
print(gt.largest_node(root))
gt.print_levelwise(root)




