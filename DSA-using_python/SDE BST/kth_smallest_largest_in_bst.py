import class_level_wise_trasversal

class solution:
    def __init__(self):            #vvi
        self.k_lar=self.k_small=int(input('Enter k value'))
        self.Ksmall=None
        self.kbig=None
    def kth_smallest(self,root):
        if root==None:return
        self.kth_smallest(root.left)
        self.k_small-=1
        if self.k_small==0: 
            self.ksmall=root.data
            return self.ksmall
        self.kth_smallest(root.right)
    def kth_largest(self,root):
        if root==None:return
        self.kth_largest(root.right)
        self.k_lar-=1
        if self.k_lar==0: 
            self.kbig=root.data
            return self.kbig
        self.kth_largest(root.left)   


bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
bst.print_tree_levelwise(root)
sol=solution()
sol.kth_smallest(root)
sol.kth_largest(root)
print("kth smallest : ",sol.ksmall)
print("kth biggest : ",sol.kbig)





