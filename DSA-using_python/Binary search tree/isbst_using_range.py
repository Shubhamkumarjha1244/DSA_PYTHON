import class_level_wise_trasversal

def isbst(root,min_range=-100000,max_range=100000):
    if root==None:return True
    if root.data <= min_range or root.data > max_range:
        return False
    return isbst(root.left,min_range,root.data) and isbst(root.right,root.data,max_range) 


bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
bst.print_tree_levelwise(root)
print(isbst(root))