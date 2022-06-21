import generate_binary_tree

def find_node_without_sibling(root):
    if root==None:
        return 
    if (bool(root.left)^bool(root.right)):
        if root.left:
            print(root.left.data,end=' ')
        else:print(root.right.data,end=' ')
    find_node_without_sibling(root.right)
    find_node_without_sibling(root.left)

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
find_node_without_sibling(root)



