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
    


n1=genericTree(6)
n2=genericTree(2)
n3=genericTree(8)
n4=genericTree(7)
n5=genericTree(1)
n6=genericTree(11)
n7=genericTree(15)
n8=genericTree(9)
n9=genericTree(6)
n10=genericTree(5)
n11=genericTree(3)
n12=genericTree(12)
n1.children=[n2,n3,n4,n5]
n3.children=[n6,n7,n11]
n6.children=[n8,n9,n10]
n10.children=[n12]
gt=generic_tree_class()
gt.printgenericTree(n1)

