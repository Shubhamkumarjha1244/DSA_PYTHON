import generate_binary_tree

def largest_node(root):
    if root==None:
        return -1
    left_large=largest_node(root.left)
    right_large=largest_node(root.right)
    return max(left_large,right_large,root.data)



tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print("Largest Nodes-->",largest_node(root))