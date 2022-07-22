import class_level_wise_trasversal

def search_print(root,val):
    if root==None:return
    if root.data==val:
        key=[]
        key.append(val)
        return key
    if root.data>val:
        le=search_print(root.left,val)
    else:
        le=search_print(root.right,val)
    if le:
        le.append(root.data)
        return le
    else:return

bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
bst.print_tree_levelwise(root)
val=int(input('Enter value to be search  :'))
path=search_print(root,val)
print(path)
