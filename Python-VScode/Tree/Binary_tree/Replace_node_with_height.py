from numpy import right_shift
import generate_binary_tree

def replace_node_with_height(root,d=0):
    if root==None:
        return
    root.data=d
    replace_node_with_height(root.left,d+1)
    replace_node_with_height(root.right,d+1)

tree=generate_binary_tree.Binary_tree()
root=tree.generate_binary_tree()
print('------Old tree-------')
tree.print_binary_tree(root)
replace_node_with_height(root)
print('------New tree-------')
tree.print_binary_tree(root)