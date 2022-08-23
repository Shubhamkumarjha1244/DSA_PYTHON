import class_level_wise_trasversal

def mirror(node1,node2):
    if node1==None and node2==None:return True
    if node1==None or node2==None:return False
    return node1.data==node2.data and mirror(node1.left,node2.right) and mirror(node1.right,node2.left)

def check_symmetric(root):
    if root==None:return True
    return mirror(root.left,root.right)

tree=class_level_wise_trasversal.level_wise_trans()
root=tree.input_level_wise()
tree.print_tree_levelwise(root)
print(check_symmetric(root))
