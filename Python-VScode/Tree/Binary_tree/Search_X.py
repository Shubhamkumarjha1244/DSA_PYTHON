import generate_binary_tree

def find_x(root,val):
    if root==None:
        return False
    if root.data==val:
        return True
    return False or find_x(root.left,val) or find_x(root.right,val)

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
tree.print_binary_tree(root)
print(find_x(root,int(input())))