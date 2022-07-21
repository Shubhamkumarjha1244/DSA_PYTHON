import class_level_wise_trasversal

def Search_node_Bst(root,val):
    if root==None:return False
    if root.data==val:return True
    if root.data<val:
       return  Search_node_Bst(root.right,val)
    else:
       return Search_node_Bst(root.left,val)
    

bst=class_level_wise_trasversal.level_wise_trans()
root=bst.input_level_wise()
val=int(input('Enter value to be search'))
bst.print_tree_levelwise(root)
print(Search_node_Bst(root,val))