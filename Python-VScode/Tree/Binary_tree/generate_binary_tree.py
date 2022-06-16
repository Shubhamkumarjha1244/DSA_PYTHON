class BinaryTreeNode:                  #class and constructor for making binary tree node
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def generate_binary_tree():
    root=int(input())
    if root==-1: return 
    root=BinaryTreeNode(root)
    root.right=generate_binary_tree()
    root.left=generate_binary_tree()
    return root    #step need to process

def print_binary_tree(root):
    if root is None: #step need to process
        return
    print(root.data,end=':')
    if root.right:
        print('R:',root.right.data,end=' ')
    if root.left:
        print('L:',root.left.data,end=' ')
    print()
    print_binary_tree(root.right)
    print_binary_tree(root.left)

def Total_num_node(root):
    if root is None:
        return 0
    left_sum=Total_num_node(root.left)
    right_sum=Total_num_node(root.right)
    return 1+left_sum+right_sum #step need to process

root=generate_binary_tree()
print("---------------------binary Tree------------------")
print_binary_tree(root)
print("total Nodes--",Total_num_node(root))
