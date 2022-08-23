import generate_binary_tree

def No_of_leaf(root):
    if root==None:
        return 0
    left_leaf=No_of_leaf(root.left)
    right_leaf=No_of_leaf(root.right)

    if root.left==None and root.right==None:
        return 1+left_leaf+right_leaf
    else:
        return left_leaf+right_leaf


tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print("No of leafs",No_of_leaf(root))