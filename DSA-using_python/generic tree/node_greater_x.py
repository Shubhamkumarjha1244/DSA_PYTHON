import class_generic_tree

def node_greater_x(root,x):
    if root==None:return 0
    total=0
    for child in root.children:
        total+=node_greater_x(child,x)
    if root.data>x:total+=1
    return total



gt=class_generic_tree.generic_tree_class()
root=gt.level_wise_input()
gt.print_levelwise(root)
x=int(input('Enter value of x :'))
print(node_greater_x(root,x))