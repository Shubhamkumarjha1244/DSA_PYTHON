import generate_binary_tree

def mirror(root):
    if root==None:
        return
    root.left,root.right=root.right,root.left
    mirror(root.left)
    mirror(root.right)
    return root
def mirror2(root):
    if root==None:
        return
    root.left,root.right=root.right,root.left
    mirror(root.right)
    mirror(root.left)
    return root


tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
root=mirror(root)
print("----------------")
tree.print_binary_tree(root)
print("----------------")
root=mirror2(root)
tree.print_binary_tree(root)