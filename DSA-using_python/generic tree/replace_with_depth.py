import class_generic_tree

def replace_with_depth(root,depth):
    if root==None:return
    root.data=depth
    for child in root.children:
        replace_with_depth(child,depth+1)
    
    

gt=class_generic_tree.generic_tree_class()
root=gt.level_wise_input()
replace_with_depth(root,0)
gt.print_levelwise(root)