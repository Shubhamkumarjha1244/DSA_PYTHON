import generate_binary_tree
import queue
def level_wise():
    root_data=int(input("Enter Root->"))
    if root_data==-1:
        return
    qu=queue.Queue()
    root=generate_binary_tree.BinaryTreeNode(int(root_data))
    qu.put(root)
    while qu.empty()!=True:
        node=qu.get()
        print("Enter right data of->",node.data)
        right_node_data=int(input())
        print("Enter left data of->",node.data)
        left_node_data=int(input())
        if right_node_data!=-1:
            node.right=generate_binary_tree.BinaryTreeNode(right_node_data)
            qu.put(node.right)
        if left_node_data!=-1:
            node.left=generate_binary_tree.BinaryTreeNode(left_node_data)
            qu.put(node.left)
    return root

def print_tree_levelwise(root):
    if not(root):return
    qu=queue.Queue()
    qu.put(root)
    while not(qu.empty()):
        node=qu.get()
        print(node.data,end=':')
        if node.right:
            print('R:',node.right.data,end=' ')
            qu.put(node.right)
        if node.left:
            print('L:',node.left.data,end='')
            qu.put(node.left)
        print()
    
        


tree=generate_binary_tree.Binary_tree()
root=level_wise()
print('----------------BINARY--TREE-levelwise--Printing------------')
print_tree_levelwise(root)
