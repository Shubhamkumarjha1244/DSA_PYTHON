import generate_binary_tree

def Height_of_tree(root):
    if root==None:
        return 0
    left_height=Height_of_tree(root.left)
    right_height=Height_of_tree(root.right)
    return 1+max(left_height,right_height)

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print("Height of tree-",Height_of_tree(root))