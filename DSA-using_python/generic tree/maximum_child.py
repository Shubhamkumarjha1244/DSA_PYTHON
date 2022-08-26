import class_generic_tree


def maximum_no_of_child(root):
    if root==None:return 0
    maxi=0
    sum=root.data
    for child in root.children:
        sum+=child.data
        maxi=max(maximum_no_of_child(child),maxi)
    maxi=max(sum,maxi)
    return maxi

gt=class_generic_tree.generic_tree_class()
root=gt.level_wise_input()
gt.print_levelwise(root)
print(maximum_no_of_child(root))