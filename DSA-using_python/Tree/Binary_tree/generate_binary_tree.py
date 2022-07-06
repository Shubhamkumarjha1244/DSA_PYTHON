class BinaryTreeNode:                  #class and constructor for making binary tree node
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class Binary_tree:
    def generate_binary_tree(self):
        root=int(input())
        if root==-1: return 
        root=BinaryTreeNode(root)
        root.right=self.generate_binary_tree()
        root.left=self.generate_binary_tree()
        return root    #step need to process

    def print_binary_tree(self,root):
        if root is None: #step need to process
            return
        print(root.data,end=':')
        if root.right:
            print('R:',root.right.data,end=' ')
        if root.left:
            print('L:',root.left.data,end=' ')
        print()
        self.print_binary_tree(root.right)
        self.print_binary_tree(root.left)

    def Total_num_node(self,root):
        if root is None:
            return 0
        left_sum=self.Total_num_node(root.left)
        right_sum=self.Total_num_node(root.right)
        return 1+left_sum+right_sum #step need to process
# tr=Binary_tree()
# root=tr.generate_binary_tree()
# print("---------------------binary Tree------------------")
# tr.print_binary_tree(root)
# print("total Nodes--",tr.Total_num_node(root))
