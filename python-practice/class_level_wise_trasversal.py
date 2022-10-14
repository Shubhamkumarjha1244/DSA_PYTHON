import collections
import queue

class BinaryTreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class level_wise_trans:
    def input_level_wise(self):
        root_data=int(input("Enter Root->"))
        if root_data==-1:
            return
        qu=queue.Queue()
        root=BinaryTreeNode(int(root_data))
        qu.put(root)
        while qu.empty()!=True:
            node=qu.get()
            print("Enter left data of->",node.data)
            left_node_data=int(input())
            print("Enter right data of->",node.data)
            right_node_data=int(input())
            if left_node_data!=-1:
                node.left=BinaryTreeNode(left_node_data)
                qu.put(node.left)
            if right_node_data!=-1:
                node.right=BinaryTreeNode(right_node_data)
                qu.put(node.right)
        return root

    def print_tree_levelwise(self,root):
        if not(root):return
        qu=queue.Queue()
        qu.put(root)
        while not(qu.empty()):
            node=qu.get()
            print(node.data,end=':')
            if node.left:
                print('L:',node.left.data,end=' ')
                qu.put(node.left)
            if node.right:
                print('R:',node.right.data,end='')
                qu.put(node.right)
            print()

# from sympy import *
# def min_func(z):
#     x=sympy.symbols('x')
#     f=x+(z-(2*x)/3)
#     return (minimum(f,x))

# t=int(input())
# for i in range(t):
#     z=int(input())
#     print(min_func(z))
