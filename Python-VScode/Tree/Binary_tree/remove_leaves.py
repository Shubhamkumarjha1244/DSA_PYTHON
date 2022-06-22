import generate_binary_tree

def remove_leaf(root):
    if root==None:
        return
    if root.left==None and root.right==None:  #yaha last case milega aur yaha se null laut jayega
        return
    root.left=remove_leaf(root.left) #baki sara case normal chalega
    root.right=remove_leaf(root.right)
    return root


tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
root=remove_leaf(root)
print("--------------------------------")
tree.print_binary_tree(root)
