import generate_binary_tree

def print_node_at_height(root,height):
    if root==None:
        return None
    if height==0:
        print(root.data,end=' ')
        return
    print_node_at_height(root.right,height-1)
    print_node_at_height(root.left,height-1)


tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print('-------Nodes---------')
print_node_at_height(root,2)