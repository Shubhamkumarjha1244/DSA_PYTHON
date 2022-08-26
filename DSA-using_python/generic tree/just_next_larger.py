import class_generic_tree


def just_next_larger(root,x):
    if root==None:return 0
    mini=1e10
    for child in root.children:
            mini=min(mini,just_next_larger(child,x))
    if root.data>x:mini=min(mini,root.data)
    return mini



gt=class_generic_tree.generic_tree_class()
root=gt.level_wise_input()
x=int(input('enter value of x: '))
print(just_next_larger(root,x))
