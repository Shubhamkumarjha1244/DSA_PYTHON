import generate_binary_tree

def print_node_at_depth(root,depth):
    if root==None:
        return None
    if depth==0:
        print(root.data,end=' ')
        return
    print_node_at_depth(root.right,depth-1)
    print_node_at_depth(root.left,depth-1)


tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print('-------Nodes---------')
print_node_at_depth(root,2)