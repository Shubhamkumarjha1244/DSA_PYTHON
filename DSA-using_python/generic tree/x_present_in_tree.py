import class_generic_tree

def check_presence(root,x):
    if root==None:return False
    if root.data==x:return True
    child_present=False
    for child in root.children:
        child_present=(check_presence(child,x) or child_present)
    return child_present


gt=class_generic_tree.generic_tree_class()
root=gt.level_wise_input()
x=int(input('Enter value of x: '))
print(check_presence(root,x))

